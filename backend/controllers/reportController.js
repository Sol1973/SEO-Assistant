/**
 * REPORT CONTROLLER - Generación de Reportes PDF
 * 
 * Fecha: 15 de Octubre de 2025 - 10:35 (Madrid)
 */

const { get } = require('../models/database');

/**
 * Generar reporte PDF de auditoría
 * Nota: Implementación con jsPDF (se instalará en Sesión 5)
 */
const generatePDFReport = async (auditId) => {
  try {
    // Obtener datos de auditoría
    const audit = await get('SELECT * FROM audits WHERE id = ?', [auditId]);
    
    if (!audit) {
      throw new Error('Auditoría no encontrada');
    }
    
    const results = JSON.parse(audit.results);
    
    // TODO: Implementar generación PDF con jsPDF
    // Por ahora, retornamos estructura de datos
    const reportData = {
      title: 'SEO Audit Report',
      url: audit.url,
      date: new Date(audit.created_at).toLocaleDateString('es-ES'),
      overallScore: audit.overall_score,
      sections: [
        {
          name: 'Meta Tags',
          score: results.metaTags?.score || 0,
          status: getStatus(results.metaTags?.score || 0),
          details: results.metaTags
        },
        {
          name: 'Headings',
          score: results.headings?.score || 0,
          status: getStatus(results.headings?.score || 0),
          details: results.headings
        },
        {
          name: 'Images',
          score: results.images?.score || 0,
          status: getStatus(results.images?.score || 0),
          details: results.images
        }
      ]
    };
    
    return reportData;
    
  } catch (error) {
    console.error('Error generando reporte:', error);
    throw error;
  }
};

/**
 * Obtener estado basado en score
 */
const getStatus = (score) => {
  if (score >= 80) return { text: 'Excelente', color: 'green', icon: '✅' };
  if (score >= 60) return { text: 'Bueno', color: 'orange', icon: '⚠️' };
  return { text: 'Necesita Mejoras', color: 'red', icon: '❌' };
};

/**
 * Guardar reporte en base de datos
 */
const saveReport = async (auditId, reportType, reportData) => {
  const { run } = require('../models/database');
  
  try {
    const result = await run(
      `INSERT INTO reports (audit_id, report_type, report_data) 
       VALUES (?, ?, ?)`,
      [auditId, reportType, JSON.stringify(reportData)]
    );
    
    return result.lastID;
  } catch (error) {
    console.error('Error guardando reporte:', error);
    throw error;
  }
};

/**
 * Obtener reporte por ID
 */
const getReport = async (reportId) => {
  try {
    const report = await get('SELECT * FROM reports WHERE id = ?', [reportId]);
    
    if (report && report.report_data) {
      report.report_data = JSON.parse(report.report_data);
    }
    
    return report;
  } catch (error) {
    console.error('Error obteniendo reporte:', error);
    throw error;
  }
};

module.exports = {
  generatePDFReport,
  saveReport,
  getReport,
  getStatus
};

