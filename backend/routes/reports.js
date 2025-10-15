/**
 * REPORTS ROUTES
 * Endpoints para generación y descarga de reportes
 * 
 * Fecha: 15 de Octubre de 2025 - 10:35 (Madrid)
 */

const express = require('express');
const router = express.Router();
const { 
  generatePDFReport, 
  saveReport, 
  getReport 
} = require('../controllers/reportController');

/**
 * POST /api/reports/generate
 * Generar reporte PDF de auditoría
 */
router.post('/generate', async (req, res) => {
  try {
    const { auditId } = req.body;
    
    if (!auditId) {
      return res.status(400).json({
        success: false,
        error: 'auditId es requerido'
      });
    }
    
    // Generar reporte
    const reportData = await generatePDFReport(auditId);
    
    // Guardar en BD
    const reportId = await saveReport(auditId, 'pdf', reportData);
    
    res.json({
      success: true,
      message: 'Reporte generado exitosamente',
      data: {
        reportId,
        auditId,
        reportData
      }
    });
  } catch (error) {
    console.error('Error generando reporte:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/reports/:id
 * Obtener reporte por ID
 */
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    const report = await getReport(id);
    
    if (!report) {
      return res.status(404).json({
        success: false,
        error: 'Reporte no encontrado'
      });
    }
    
    res.json({
      success: true,
      data: report
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/reports/download/:id
 * Descargar reporte PDF
 * TODO: Implementar generación real de PDF con jsPDF en Sesión 5
 */
router.get('/download/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    const report = await getReport(id);
    
    if (!report) {
      return res.status(404).json({
        success: false,
        error: 'Reporte no encontrado'
      });
    }
    
    // Por ahora retornar JSON, en Sesión 5 será PDF
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Content-Disposition', `attachment; filename=report-${id}.json`);
    res.json(report.report_data);
    
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

module.exports = router;
