// SEO Assistant - Environment Configuration Example
// Copy this file to environment.js and configure your values

module.exports = {
  // Server Configuration
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || 'development',
  
  // Database Configuration
  databaseUrl: process.env.DATABASE_URL || './data/seo_assistant.db',
  
  // Security
  sessionSecret: process.env.SESSION_SECRET || 'dev-secret-key',
  
  // Puppeteer Configuration (for Vercel)
  puppeteer: {
    skipChromiumDownload: process.env.PUPPETEER_SKIP_CHROMIUM_DOWNLOAD === 'true',
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || null,
    headless: process.env.NODE_ENV === 'production' ? 'new' : true,
    args: process.env.NODE_ENV === 'production' ? [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-accelerated-2d-canvas',
      '--no-first-run',
      '--no-zygote',
      '--disable-gpu'
    ] : []
  },
  
  // CORS Configuration
  allowedOrigins: process.env.ALLOWED_ORIGINS ? 
    process.env.ALLOWED_ORIGINS.split(',') : 
    ['http://localhost:3000', 'http://localhost:4200'],
  
  // Rate Limiting
  rateLimit: {
    windowMs: parseInt(process.env.RATE_LIMIT_WINDOW_MS) || 900000, // 15 minutes
    maxRequests: parseInt(process.env.RATE_LIMIT_MAX_REQUESTS) || 100
  }
};
