/**
 * SEO ASSISTANT - FRONTEND APPLICATION
 * Main JavaScript file
 */

// ============================================
// CONFIG
// ============================================

const API_BASE_URL = 'http://localhost:3000/api';

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
 * Get audit results
 */
async function getAuditResults(auditId) {
  try {
    const response = await fetch(`${API_BASE_URL}/audit/${auditId}`);
    const data = await response.json();
    
    if (data.success) {
      displayResults(data.data);
    }
  } catch (error) {
    console.error('Error:', error);
    showAlert('Error al obtener los resultados', 'danger');
  }
}

/**
 * Display audit results
 */
function displayResults(data) {
  // Validar que data y results existen
  if (!data || !data.results) {
    console.error('Error: datos de auditoría inválidos', data);
    showAlert('Error: La auditoría no se completó correctamente. Por favor, intenta de nuevo.', 'warning');
    return;
  }
  
  const results = typeof data.results === 'string' ? JSON.parse(data.results) : data.results;
  
  // Validar que results tiene las propiedades necesarias
  if (!results.metaTags || !results.headings || !results.images) {
    console.error('Error: estructura de resultados inválida', results);
    showAlert('Error: Los resultados de la auditoría están incompletos.', 'warning');
    return;
  }
  
  const html = `
    <div class="row g-4">
      <div class="col-md-4">
        <div class="score-card ${getScoreClass(results.metaTags.score || 0)}">
          <div class="score-label">Meta Tags</div>
          <div class="score-value">${results.metaTags.score || 0}</div>
          <div class="traffic-light ${getTrafficLight(results.metaTags.score || 0)}"></div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="score-card ${getScoreClass(results.headings.score || 0)}">
          <div class="score-label">Headings</div>
          <div class="score-value">${results.headings.score || 0}</div>
          <div class="traffic-light ${getTrafficLight(results.headings.score || 0)}"></div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="score-card ${getScoreClass(results.images.score || 0)}">
          <div class="score-label">Imágenes</div>
          <div class="score-value">${results.images.score || 0}</div>
          <div class="traffic-light ${getTrafficLight(results.images.score || 0)}"></div>
        </div>
      </div>
    </div>
    
    <div class="mt-4">
      <button class="btn btn-primary btn-lg" onclick="generateReport('${data.auditId}')">
        <i class="fas fa-download me-2"></i>
        Descargar Reporte PDF
      </button>
    </div>
  `;
  
  resultsContent.innerHTML = html;
  resultsSection.classList.remove('d-none');
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
  const loadingDiv = document.createElement('div');
  loadingDiv.id = 'loadingSpinner';
  loadingDiv.className = 'position-fixed top-50 start-50 translate-middle';
  loadingDiv.style.zIndex = '9999';
  loadingDiv.innerHTML = `
    <div class="spinner-border text-primary" role="status">
      <span class="visually-hidden">Cargando...</span>
    </div>
  `;
  
  document.body.appendChild(loadingDiv);
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

