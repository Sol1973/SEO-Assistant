/**
 * INTEGRATION TESTS - API Endpoints
 * 
 * Fecha: 15 de Octubre de 2025 - 10:55 (Madrid)
 */

const request = require('supertest');
const app = require('../../server');
const { initDatabase } = require('../../models/database');

describe('API Integration Tests', () => {
  
  beforeAll(async () => {
    // Inicializar base de datos de prueba
    await initDatabase();
  });

  describe('Health Check', () => {
    test('GET /api/health should return OK status', async () => {
      const response = await request(app)
        .get('/api/health');
      
      expect(response.status).toBe(200);
      expect(response.body.status).toBe('OK');
      expect(response.body.version).toBe('0.1.0');
    });
  });

  describe('Audit Endpoints', () => {
    test('POST /api/audit should create new audit', async () => {
      const response = await request(app)
        .post('/api/audit')
        .send({ url: 'https://example.com' });
      
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data).toHaveProperty('auditId');
    });

    test('POST /api/audit without URL should fail', async () => {
      const response = await request(app)
        .post('/api/audit')
        .send({});
      
      expect(response.status).toBe(400);
      expect(response.body.success).toBe(false);
    });

    test('GET /api/audit/:id should return audit results', async () => {
      // Primero crear una auditoría
      const createResponse = await request(app)
        .post('/api/audit')
        .send({ url: 'https://example.com' });
      
      const auditId = createResponse.body.data.auditId;
      
      // Esperar a que se procese
      await new Promise(resolve => setTimeout(resolve, 5000));
      
      // Obtener resultados
      const response = await request(app)
        .get(`/api/audit/${auditId}`);
      
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data.status).toBe('completed');
      expect(response.body.data).toHaveProperty('overall_score');
    });

    test('GET /api/audit/:id with invalid ID should return 404', async () => {
      const response = await request(app)
        .get('/api/audit/99999');
      
      expect(response.status).toBe(404);
    });
  });

  describe('Report Endpoints', () => {
    test('POST /api/reports/generate should create report', async () => {
      // Primero crear auditoría
      const auditResponse = await request(app)
        .post('/api/audit')
        .send({ url: 'https://example.com' });
      
      const auditId = auditResponse.body.data.auditId;
      
      // Esperar procesamiento
      await new Promise(resolve => setTimeout(resolve, 5000));
      
      // Generar reporte
      const response = await request(app)
        .post('/api/reports/generate')
        .send({ auditId });
      
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data).toHaveProperty('reportId');
    });

    test('GET /api/reports/:id should return report', async () => {
      // Crear auditoría y reporte
      const auditResponse = await request(app)
        .post('/api/audit')
        .send({ url: 'https://example.com' });
      
      const auditId = auditResponse.body.data.auditId;
      await new Promise(resolve => setTimeout(resolve, 5000));
      
      const reportResponse = await request(app)
        .post('/api/reports/generate')
        .send({ auditId });
      
      const reportId = reportResponse.body.data.reportId;
      
      // Obtener reporte
      const response = await request(app)
        .get(`/api/reports/${reportId}`);
      
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data).toHaveProperty('report_data');
    });
  });

  describe('Error Handling', () => {
    test('Non-existent endpoint should return 404', async () => {
      const response = await request(app)
        .get('/api/nonexistent');
      
      expect(response.status).toBe(404);
    });

    test('Invalid method should return 404', async () => {
      const response = await request(app)
        .delete('/api/audit');
      
      expect(response.status).toBe(404);
    });
  });

});

