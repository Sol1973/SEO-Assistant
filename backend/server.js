/**
 * SEO ASSISTANT - SERVER PRINCIPAL
 * Servidor Express para aplicación local y deploy en Vercel
 */

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require('path');

// Solo cargar dotenv en desarrollo local
if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}

// Initialize database
require('./models/database');

const app = express();
const PORT = process.env.PORT || 3000;

// ============================================
// MIDDLEWARE
// ============================================

// Seguridad con CSP configurado para permitir CDNs
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net", "https://cdnjs.cloudflare.com"],
      scriptSrc: ["'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net", "https://cdnjs.cloudflare.com"],
      fontSrc: ["'self'", "https://cdnjs.cloudflare.com"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "https://cdn.jsdelivr.net"] // Permite source maps
    }
  }
}));

// CORS
app.use(cors());

// Logging
app.use(morgan('dev'));

// Body parser
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Archivos estáticos
app.use(express.static(path.join(__dirname, '../frontend')));

// ============================================
// RUTAS
// ============================================

// Ruta principal
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

// API Health Check
app.get('/api/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'SEO Assistant API is running',
    version: '0.1.0',
    timestamp: new Date().toISOString()
  });
});

// API Routes (placeholder)
app.use('/api/audit', require('./routes/audit'));
app.use('/api/keywords', require('./routes/keywords'));
app.use('/api/reports', require('./routes/reports'));

// ============================================
// ERROR HANDLING
// ============================================

// 404 Handler
app.use((req, res) => {
  res.status(404).json({
    error: 'Not Found',
    message: `Route ${req.url} not found`
  });
});

// Global Error Handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Internal Server Error',
    message: err.message
  });
});

// ============================================
// START SERVER
// ============================================

app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════════╗
║   SEO ASSISTANT - Server Running 🚀       ║
╠════════════════════════════════════════════╣
║   Port: ${PORT}                              ║
║   URL: http://localhost:${PORT}              ║
║   Environment: ${process.env.NODE_ENV || 'development'}           ║
╚════════════════════════════════════════════╝
  `);
});

// Export app for Vercel
module.exports = app;

// Solo iniciar servidor si no estamos en Vercel
if (process.env.NODE_ENV !== 'production' || !process.env.VERCEL) {
  app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════╗
║   SEO ASSISTANT - Server Running 🚀       ║
╠════════════════════════════════════════════╣
║   Port: ${PORT}                              ║
║   URL: http://localhost:${PORT}              ║
║   Environment: ${process.env.NODE_ENV || 'development'}           ║
╚════════════════════════════════════════════╝
    `);
  });
}

