/**
 * AUDIT TESTS
 * Unit tests para la funcionalidad de auditoría
 */

const { startAudit, getAuditResults } = require('../../backend/controllers/auditController');

describe('Audit Controller', () => {
  describe('startAudit', () => {
    test('debe iniciar una auditoría con URL válida', async () => {
      const url = 'https://example.com';
      const result = await startAudit(url);
      
      expect(result.success).toBe(true);
      expect(result.data.url).toBe(url);
      expect(result.data.status).toBe('pending');
      expect(result.data.auditId).toBeDefined();
    });

    test('debe retornar auditId numérico', async () => {
      const url = 'https://example.com';
      const result = await startAudit(url);
      
      expect(typeof result.data.auditId).toBe('number');
      expect(result.data.auditId).toBeGreaterThan(0);
    });
  });

  describe('getAuditResults', () => {
    test('debe retornar error para ID inexistente', async () => {
      await expect(getAuditResults(99999)).rejects.toThrow('Audit not found');
    });

    test('debe retornar resultados para auditoría existente', async () => {
      // Primero crear una auditoría
      const createResult = await startAudit('https://example.com');
      const auditId = createResult.data.auditId;
      
      // Esperar un momento para procesamiento
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Obtener resultados
      const result = await getAuditResults(auditId);
      
      expect(result.success).toBe(true);
      expect(result.data.auditId).toBe(auditId);
      expect(result.data.status).toBeDefined();
    });
  });

  describe('Scoring System', () => {
    test('los scores deben estar entre 0 y 100', async () => {
      const result = await startAudit('https://example.com');
      const auditId = result.data.auditId;
      
      // Esperar procesamiento
      await new Promise(resolve => setTimeout(resolve, 3000));
      
      const auditResult = await getAuditResults(auditId);
      
      if (auditResult.data.results) {
        const { metaTags, headings, images } = auditResult.data.results;
        
        expect(metaTags.score).toBeGreaterThanOrEqual(0);
        expect(metaTags.score).toBeLessThanOrEqual(100);
        
        expect(headings.score).toBeGreaterThanOrEqual(0);
        expect(headings.score).toBeLessThanOrEqual(100);
        
        expect(images.score).toBeGreaterThanOrEqual(0);
        expect(images.score).toBeLessThanOrEqual(100);
      }
    });
  });
});

