/**
 * E2E TESTS - End-to-End Testing
 * 
 * Fecha: 15 de Octubre de 2025 - 11:05 (Madrid)
 */

const puppeteer = require('puppeteer');

describe('SEO Assistant E2E Tests', () => {
  let browser;
  let page;
  const APP_URL = 'http://localhost:3000';

  beforeAll(async () => {
    browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    page = await browser.newPage();
  });

  afterAll(async () => {
    await browser.close();
  });

  describe('Homepage', () => {
    test('Should load homepage successfully', async () => {
      await page.goto(APP_URL);
      const title = await page.title();
      expect(title).toContain('SEO');
    });

    test('Should display main heading', async () => {
      await page.goto(APP_URL);
      const heading = await page.$eval('h1', el => el.textContent);
      expect(heading).toBeTruthy();
    });

    test('Should have audit form', async () => {
      await page.goto(APP_URL);
      const form = await page.$('#auditForm');
      expect(form).toBeTruthy();
    });
  });

  describe('Audit Flow', () => {
    test('Should submit audit and get results', async () => {
      await page.goto(APP_URL);
      
      // Ingresar URL
      await page.type('#urlInput', 'https://example.com');
      
      // Click en analizar
      await page.click('#submitBtn');
      
      // Esperar resultados (máximo 10 segundos)
      await page.waitForSelector('#results', { timeout: 10000 });
      
      // Verificar que muestra resultados
      const results = await page.$('#results');
      expect(results).toBeTruthy();
    });

    test('Should show error for invalid URL', async () => {
      await page.goto(APP_URL);
      
      // Ingresar URL inválida
      await page.type('#urlInput', 'not-a-url');
      
      // Click en analizar
      await page.click('#submitBtn');
      
      // Esperar mensaje de error
      await page.waitForSelector('.alert-danger', { timeout: 3000 });
      
      const error = await page.$('.alert-danger');
      expect(error).toBeTruthy();
    });

    test('Should show loading state during audit', async () => {
      await page.goto(APP_URL);
      
      // Ingresar URL
      await page.type('#urlInput', 'https://example.com');
      
      // Click en analizar
      await page.click('#submitBtn');
      
      // Verificar loading
      const loading = await page.$('.spinner-border');
      expect(loading).toBeTruthy();
    });
  });

  describe('Navigation', () => {
    test('Should navigate to different sections', async () => {
      await page.goto(APP_URL);
      
      // Verificar que existen links de navegación
      const navLinks = await page.$$('nav a');
      expect(navLinks.length).toBeGreaterThan(0);
    });
  });

  describe('Responsive Design', () => {
    test('Should work on mobile viewport', async () => {
      await page.setViewport({ width: 375, height: 667 });
      await page.goto(APP_URL);
      
      const body = await page.$('body');
      expect(body).toBeTruthy();
    });

    test('Should work on tablet viewport', async () => {
      await page.setViewport({ width: 768, height: 1024 });
      await page.goto(APP_URL);
      
      const body = await page.$('body');
      expect(body).toBeTruthy();
    });

    test('Should work on desktop viewport', async () => {
      await page.setViewport({ width: 1920, height: 1080 });
      await page.goto(APP_URL);
      
      const body = await page.$('body');
      expect(body).toBeTruthy();
    });
  });

  describe('Performance', () => {
    test('Should load page in reasonable time', async () => {
      const startTime = Date.now();
      await page.goto(APP_URL, { waitUntil: 'networkidle0' });
      const loadTime = Date.now() - startTime;
      
      // Debe cargar en menos de 3 segundos
      expect(loadTime).toBeLessThan(3000);
    });
  });

  describe('API Integration', () => {
    test('Should call API endpoints', async () => {
      // Interceptar requests
      const requests = [];
      page.on('request', request => {
        if (request.url().includes('/api/')) {
          requests.push(request.url());
        }
      });
      
      await page.goto(APP_URL);
      await page.type('#urlInput', 'https://example.com');
      await page.click('#submitBtn');
      
      // Esperar un momento
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Verificar que se llamó a la API
      expect(requests.length).toBeGreaterThan(0);
    });
  });

});

