/**
 * SEO ASSISTANT - VERCEL SERVERLESS FUNCTION
 * Punto de entrada para Vercel
 */

// Importar la aplicación Express
const app = require('../backend/server');

// Exportar para Vercel
module.exports = app;
