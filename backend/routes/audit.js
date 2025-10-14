/**
 * AUDIT ROUTES
 * Endpoints para auditorías SEO
 */

const express = require('express');
const router = express.Router();
const { startAudit, getAuditResults } = require('../controllers/auditController');

/**
 * POST /api/audit
 * Inicia una nueva auditoría SEO
 */
router.post('/', async (req, res) => {
  try {
    const { url } = req.body;

    if (!url) {
      return res.status(400).json({
        error: 'Bad Request',
        message: 'URL is required'
      });
    }

    const result = await startAudit(url);
    res.json(result);
  } catch (error) {
    res.status(500).json({
      error: 'Internal Server Error',
      message: error.message
    });
  }
});

/**
 * GET /api/audit/:id
 * Obtiene el estado de una auditoría
 */
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await getAuditResults(id);
    res.json(result);
  } catch (error) {
    res.status(500).json({
      error: 'Internal Server Error',
      message: error.message
    });
  }
});

module.exports = router;

