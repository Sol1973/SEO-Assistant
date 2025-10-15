/**
 * SEO ASSISTANT - ELECTRON MAIN PROCESS
 * Aplicación Desktop Portable
 * 
 * Fecha: 15 de Octubre de 2025 - 10:30 (Madrid)
 */

const { app, BrowserWindow } = require('electron');
const path = require('path');

let mainWindow;
let serverProcess;

// Iniciar servidor Express
function startServer() {
  const server = require('./backend/server');
  console.log('✅ Servidor Express iniciado desde Electron');
  return server;
}

// Crear ventana principal
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 800,
    minHeight: 600,
    icon: path.join(__dirname, 'frontend', 'assets', 'icon.png'),
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false
    },
    backgroundColor: '#f8f9fa',
    show: false
  });

  // Esperar a que el servidor esté listo
  setTimeout(() => {
    mainWindow.loadURL('http://localhost:3000');
    
    mainWindow.once('ready-to-show', () => {
      mainWindow.show();
      
      // Abrir DevTools solo en desarrollo
      if (process.env.NODE_ENV === 'development') {
        mainWindow.webContents.openDevTools();
      }
    });
  }, 2000);

  // Manejar cierre de ventana
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// Inicializar aplicación
app.whenReady().then(() => {
  console.log(`
╔════════════════════════════════════════════╗
║   SEO ASSISTANT - Electron App 🚀         ║
╠════════════════════════════════════════════╣
║   Versión: 0.1.0                           ║
║   Plataforma: ${process.platform}                        ║
║   Inicializando...                         ║
╚════════════════════════════════════════════╝
  `);
  
  serverProcess = startServer();
  createWindow();
  
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// Cerrar app cuando todas las ventanas están cerradas
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// Cleanup al salir
app.on('will-quit', () => {
  console.log('🛑 Cerrando SEO Assistant...');
});

// Manejo de errores
process.on('uncaughtException', (error) => {
  console.error('Error no capturado:', error);
});

