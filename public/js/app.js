/**
 * SEO ASSISTANT - FRONTEND APPLICATION
 * Main JavaScript file
 */

// ============================================
// CONFIG
// ============================================

// Dynamic API URL based on environment
const API_BASE_URL = window.location.hostname === 'localhost' 
  ? 'http://localhost:3000/api'
  : '/api';

// ============================================
// DOM ELEMENTS
// ============================================

const auditForm = document.getElementById('auditForm');
const websiteUrl = document.getElementById('websiteUrl');
const resultsSection = document.getElementById('results');
const resultsContent = document.getElementById('resultsContent');

// ============================================
// EVENT LISTENERS
// ============================================

auditForm.addEventListener('submit', handleAuditSubmit);

// ============================================
// FUNCTIONS
// ============================================

/**
 * Handle audit form submission
 */
async function handleAuditSubmit(e) {
  e.preventDefault();
  
  const url = websiteUrl.value.trim();
  
  if (!url) {
    showAlert('Por favor ingresa una URL válida', 'warning');
    return;
  }
  
  try {
    // Show loading
    showLoading();
    
    // Start audit
    const response = await fetch(`${API_BASE_URL}/audit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url })
    });
    
    const data = await response.json();
    
    if (data.success) {
      // Get audit results
      await getAuditResults(data.data.auditId);
    } else {
      showAlert('Error al iniciar la auditoría', 'danger');
    }
  } catch (error) {
    console.error('Error:', error);
    showAlert('Error de conexión con el servidor', 'danger');
  } finally {
    hideLoading();
  }
}

/**
 * Get audit results with polling
 * Espera a que la auditoría se complete antes de mostrar resultados
 */
async function getAuditResults(auditId) {
  const maxAttempts = 20; // Máximo 20 intentos
  const interval = 1000; // Cada 1 segundo
  let attempts = 0;
  
  const checkStatus = async () => {
    try {
      attempts++;
      
      const response = await fetch(`${API_BASE_URL}/audit/${auditId}`);
      const data = await response.json();
      
      if (!data.success) {
        throw new Error('Error obteniendo resultados');
      }
      
      const audit = data.data;
      
      // Si está completada, mostrar resultados
      if (audit.status === 'completed') {
        hideLoading();
        displayResults(audit);
        return;
      }
      
      // Si falló, mostrar error
      if (audit.status === 'failed') {
        hideLoading();
        showAlert('La auditoría falló. Verifica la URL e intenta de nuevo.', 'danger');
        return;
      }
      
      // Si todavía está procesando
      if (audit.status === 'processing' || audit.status === 'pending') {
        if (attempts >= maxAttempts) {
          hideLoading();
          showAlert('La auditoría está tardando demasiado. Intenta de nuevo más tarde.', 'warning');
          return;
        }
        
        // Mostrar mensaje de progreso
        updateLoadingMessage(`Analizando... (${attempts}/${maxAttempts})`);
        
        // Reintentar después del intervalo
        setTimeout(checkStatus, interval);
        return;
      }
      
    } catch (error) {
      console.error('Error:', error);
      hideLoading();
      showAlert('Error al obtener los resultados', 'danger');
    }
  };
  
  // Iniciar polling
  await checkStatus();
}

/**
 * Display audit results
 */
function displayResults(data) {
  // Validar que data existe
  if (!data) {
    console.error('Error: data is null or undefined');
    showAlert('Error: No se recibieron datos del servidor.', 'danger');
    return;
  }
  
  // Validar estado de la auditoría
  if (data.status === 'failed') {
    showAlert('La auditoría falló. Por favor, verifica la URL e intenta de nuevo.', 'danger');
    return;
  }
  
  if (data.status === 'processing') {
    showAlert('La auditoría aún está en proceso. Espera unos segundos...', 'info');
    return;
  }
  
  // Validar que results existe
  if (!data.results) {
    console.error('Error: results is null', data);
    showAlert('La auditoría se completó pero no hay resultados disponibles. Intenta con otra URL.', 'warning');
    return;
  }
  
  // Parsear results si es string
  const results = typeof data.results === 'string' ? JSON.parse(data.results) : data.results;
  
  // Validar estructura de results
  if (!results || typeof results !== 'object') {
    console.error('Error: results no es un objeto válido', results);
    showAlert('Error: La estructura de resultados es inválida.', 'danger');
    return;
  }
  
  if (!results.metaTags || !results.headings || !results.images) {
    console.error('Error: faltan propiedades en results', results);
    showAlert('Los resultados están incompletos. Algunas secciones no pudieron analizarse.', 'warning');
    return;
  }
  
  const html = `
    <div class="alert alert-success mb-4">
      <h4><i class="fas fa-check-circle me-2"></i>Auditoría Completada</h4>
      <p class="mb-0"><strong>URL:</strong> ${data.url}</p>
      <p class="mb-0"><strong>Score General:</strong> ${data.overallScore}/100</p>
    </div>
    
    <div class="row g-4 mb-4">
      <div class="col-md-4">
        <div class="score-card ${getScoreClass(results.metaTags.score || 0)}">
          <div class="score-label">Meta Tags</div>
          <div class="score-value">${results.metaTags.score || 0}</div>
          <div class="traffic-light ${getTrafficLight(results.metaTags.score || 0)}"></div>
          <div class="score-description">/100</div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="score-card ${getScoreClass(results.headings.score || 0)}">
          <div class="score-label">Headings</div>
          <div class="score-value">${results.headings.score || 0}</div>
          <div class="traffic-light ${getTrafficLight(results.headings.score || 0)}"></div>
          <div class="score-description">/100</div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="score-card ${getScoreClass(results.images.score || 0)}">
          <div class="score-label">Imágenes</div>
          <div class="score-value">${results.images.score || 0}</div>
          <div class="traffic-light ${getTrafficLight(results.images.score || 0)}"></div>
          <div class="score-description">/100</div>
        </div>
      </div>
    </div>
    
    <div class="text-center mt-4">
      <button class="btn btn-primary btn-lg me-2" id="btnGenerateReport" data-audit-id="${data.auditId}">
        <i class="fas fa-download me-2"></i>
        Descargar Reporte
      </button>
      <button class="btn btn-outline-secondary btn-lg" id="btnNewAudit">
        <i class="fas fa-redo me-2"></i>
        Nueva Auditoría
      </button>
    </div>
  `;
  
  resultsContent.innerHTML = html;
  resultsSection.classList.remove('d-none');
  
  // Agregar event listeners a los botones
  document.getElementById('btnGenerateReport')?.addEventListener('click', function() {
    generateReport(this.dataset.auditId);
  });
  
  document.getElementById('btnNewAudit')?.addEventListener('click', function() {
    resultsSection.classList.add('d-none');
    websiteUrl.value = '';
    websiteUrl.focus();
  });
  resultsSection.classList.add('fade-in');
  
  // Scroll to results
  resultsSection.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Get score class based on value
 */
function getScoreClass(score) {
  if (score >= 90) return 'score-excellent';
  if (score >= 70) return 'score-good';
  if (score >= 50) return 'score-fair';
  return 'score-poor';
}

/**
 * Get traffic light color based on score
 */
function getTrafficLight(score) {
  if (score >= 80) return 'green';
  if (score >= 50) return 'yellow';
  return 'red';
}

/**
 * Generate report
 */
async function generateReport(auditId) {
  try {
    const response = await fetch(`${API_BASE_URL}/reports/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ auditId, format: 'pdf' })
    });
    
    const data = await response.json();
    
    if (data.success) {
      showAlert('Reporte generado exitosamente', 'success');
      // TODO: Implementar descarga real
    }
  } catch (error) {
    console.error('Error:', error);
    showAlert('Error al generar el reporte', 'danger');
  }
}

/**
 * Show alert
 */
function showAlert(message, type = 'info') {
  const alertDiv = document.createElement('div');
  alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
  alertDiv.style.zIndex = '9999';
  alertDiv.innerHTML = `
    ${message}
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
  `;
  
  document.body.appendChild(alertDiv);
  
  setTimeout(() => {
    alertDiv.remove();
  }, 5000);
}

/**
 * Show loading
 */
function showLoading() {
  // Eliminar overlay existente
  hideLoading();
  
  const loadingDiv = document.createElement('div');
  loadingDiv.id = 'loadingSpinner';
  loadingDiv.className = 'loading-overlay';
  loadingDiv.innerHTML = `
    <div class="text-center">
      <div class="spinner-custom mb-3"></div>
      <h4 class="text-primary" id="loadingTitle">Analizando sitio web...</h4>
      <p class="text-muted" id="loadingMessage">Esto puede tardar algunos segundos</p>
      <div class="mt-3">
        <small class="text-muted">No cierres esta ventana</small>
      </div>
    </div>
  `;
  
  document.body.appendChild(loadingDiv);
}

/**
 * Update loading message
 */
function updateLoadingMessage(message) {
  const loadingMessage = document.getElementById('loadingMessage');
  if (loadingMessage) {
    loadingMessage.textContent = message;
  }
}

/**
 * Hide loading
 */
function hideLoading() {
  const loadingDiv = document.getElementById('loadingSpinner');
  if (loadingDiv) {
    loadingDiv.remove();
  }
}

// ============================================
// INITIALIZATION
// ============================================

console.log('SEO Assistant Frontend Loaded ✓');

