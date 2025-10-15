# 🖥️ SEO ASSISTANT - ELECTRON APP

**Fecha:** 15 de Octubre de 2025 - 11:00 (Madrid)  
**Versión:** 0.2.0  
**Plataformas:** Windows, macOS, Linux

---

## 📦 APLICACIÓN DESKTOP PORTABLE

SEO Assistant ahora está disponible como aplicación de escritorio independiente gracias a Electron.

### ✨ Características:
- ✅ **100% Offline** - Funciona sin conexión a internet
- ✅ **Portable** - Ejecuta desde USB sin instalación
- ✅ **Multi-plataforma** - Windows, macOS y Linux
- ✅ **Base de datos local** - SQLite integrado
- ✅ **Servidor incluido** - Express embebido

---

## 🚀 INICIO RÁPIDO

### **Opción 1: Descargar Ejecutable** (Recomendado)

#### Windows:
```bash
# Descargar SEO-Assistant-Portable.exe
# Doble click para ejecutar
# No requiere instalación
```

#### macOS:
```bash
# Descargar SEO-Assistant.dmg
# Abrir DMG y arrastrar a Aplicaciones
# Cmd+Space → "SEO Assistant"
```

#### Linux:
```bash
# Descargar SEO-Assistant.AppImage
chmod +x SEO-Assistant.AppImage
./SEO-Assistant.AppImage
```

### **Opción 2: Ejecutar desde Código**

```bash
# Clonar repositorio
git clone https://github.com/Sol1973/SEO-Assistant.git
cd SEO-Assistant

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run electron:dev

# O en modo producción
npm run electron
```

---

## 🔨 BUILD - GENERAR EJECUTABLES

### **Build para Windows (Portable):**
```bash
npm run build:win

# Output: dist/SEO-Assistant-Portable.exe
# Tamaño: ~150-200 MB
# No requiere instalación
```

### **Build para macOS (DMG):**
```bash
npm run build:mac

# Output: dist/SEO-Assistant.dmg
# Requiere: macOS 10.13+
# Incluye: Auto-update
```

### **Build para Linux (AppImage):**
```bash
npm run build:linux

# Output: dist/SEO-Assistant.AppImage
# Compatible: Ubuntu 18.04+, Fedora, Debian
# Portable: Sí
```

### **Build para Todas las Plataformas:**
```bash
npm run build

# Genera: Windows, macOS y Linux
# Requiere: Configuración específica por plataforma
```

---

## ⚙️ CONFIGURACIÓN

### **Arquitectura de la App:**

```
SEO-Assistant.exe/app
├── main.js              # Proceso principal Electron
├── backend/             # Servidor Express
│   ├── server.js
│   ├── controllers/
│   ├── models/
│   └── routes/
├── frontend/            # Interfaz web
│   ├── index.html
│   ├── css/
│   └── js/
├── data/                # Base de datos SQLite
│   └── seo-assistant.db
└── node_modules/        # Dependencias empaquetadas
```

### **Variables de Entorno:**

La app Electron usa las mismas variables que la versión web:

```env
NODE_ENV=production
PORT=3000
DATABASE_PATH=./data/seo-assistant.db
PUPPETEER_HEADLESS=true
PUPPETEER_TIMEOUT=30000
```

---

## 🎯 FUNCIONALIDADES

### **✅ Implementado:**
- Ventana de aplicación nativa
- Servidor Express integrado
- Base de datos SQLite local
- Auditoría SEO completa
- DevTools en modo desarrollo
- Multi-ventana soporte

### **🔄 En Desarrollo:**
- Auto-update (actualizaciones automáticas)
- Menu nativo personalizado
- Notificaciones de escritorio
- Tray icon (icono en bandeja del sistema)
- Deep links (abrir URLs en la app)

---

## 📊 VENTANAS Y PROCESOS

### **Main Process** (`main.js`):
- Gestiona el ciclo de vida de la app
- Crea y controla ventanas
- Inicia el servidor Express
- Maneja eventos del sistema

### **Renderer Process** (Frontend):
- Interfaz de usuario (HTML/CSS/JS)
- Comunicación con API REST
- No tiene acceso directo a Node.js (seguridad)

---

## 🔐 SEGURIDAD

### **Configuración Segura:**
```javascript
webPreferences: {
  nodeIntegration: false,      // ✅ No exponer Node.js al frontend
  contextIsolation: true,      // ✅ Aislar contextos
  enableRemoteModule: false    // ✅ Deshabilitar módulo remote
}
```

### **Buenas Prácticas:**
- ✅ No usar `require()` en el renderer
- ✅ Validar todas las entradas de usuario
- ✅ Usar Content Security Policy (CSP)
- ✅ Mantener Electron actualizado

---

## 🐛 TROUBLESHOOTING

### **App no inicia:**
```bash
# Windows
# - Verificar que no esté bloqueado por antivirus
# - Ejecutar como Administrador

# macOS
# - Verificar permisos: Sistema > Seguridad
# - Permitir apps de desarrolladores identificados

# Linux
# - chmod +x SEO-Assistant.AppImage
# - Instalar FUSE si es necesario
```

### **Puerto 3000 en uso:**
La app intentará usar el puerto 3000. Si está ocupado:
```bash
# Matar proceso en puerto 3000
# Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:3000 | xargs kill -9
```

### **Base de datos corrupta:**
```bash
# Eliminar y reiniciar
# La app recreará la BD automáticamente
rm -rf data/seo-assistant.db
```

---

## 📦 TAMAÑOS DE DESCARGA

| Plataforma | Tamaño | Comprimido |
|------------|--------|------------|
| Windows    | ~180 MB | ~65 MB     |
| macOS      | ~200 MB | ~70 MB     |
| Linux      | ~175 MB | ~60 MB     |

**Nota:** Los tamaños incluyen:
- Electron runtime
- Chromium embebido
- Node.js runtime
- Todas las dependencias

---

## 🔄 ACTUALIZACIONES

### **Manual:**
1. Descargar nueva versión
2. Reemplazar ejecutable
3. La BD se migra automáticamente

### **Automático (Próximamente):**
- La app verificará actualizaciones al iniciar
- Descarga en segundo plano
- Instalación al reiniciar

---

## 🎨 PERSONALIZACIÓN

### **Cambiar Icono:**
```bash
# Colocar archivos en frontend/assets/
# - icon.ico (Windows)
# - icon.icns (macOS)
# - icon.png (Linux)

# Rebuild
npm run build
```

### **Cambiar Título de Ventana:**
```javascript
// main.js
const mainWindow = new BrowserWindow({
  title: 'Mi SEO Assistant'
});
```

---

## 📚 RECURSOS

### **Electron Documentation:**
- https://www.electronjs.org/docs
- https://www.electronjs.org/docs/latest/tutorial/quick-start

### **Electron Builder:**
- https://www.electron.build/
- https://www.electron.build/configuration/configuration

### **Auto-Update:**
- https://www.electron.build/auto-update

---

## 🤝 CONTRIBUIR

Para contribuir al desarrollo de la app Electron:

1. Fork el repositorio
2. Crear rama: `git checkout -b feature/electron-mejora`
3. Hacer cambios
4. Test: `npm run electron:dev`
5. Build: `npm run build`
6. Commit y PR

---

## 📝 CHANGELOG

### v0.2.0 (15 de Octubre de 2025)
- ✅ Electron integration completa
- ✅ Build scripts para todas las plataformas
- ✅ Configuración de seguridad
- ✅ DevTools en desarrollo

### v0.1.0 (14 de Octubre de 2025)
- ✅ MVP web funcional
- ✅ Backend y Frontend base

---

**Repositorio:** https://github.com/Sol1973/SEO-Assistant  
**Issues:** https://github.com/Sol1973/SEO-Assistant/issues  
**Releases:** https://github.com/Sol1973/SEO-Assistant/releases

**¡Disfruta de SEO Assistant en tu escritorio!** 🚀

