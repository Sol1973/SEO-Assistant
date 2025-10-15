# 📸 GUÍA PARA CAPTURAR SCREENSHOTS

**Fecha:** 15 de Octubre de 2025 - 12:15 (Madrid)  
**Versión:** 0.3.0

---

## 🎯 OBJETIVO

Capturar screenshots profesionales de la aplicación SEO Assistant para la documentación y promoción del proyecto.

---

## 📋 SCREENSHOTS NECESARIOS

### 1. **Homepage / Hero Section**
**Archivo:** `screenshot-01-homepage.png`  
**Resolución:** 1920x1080  
**Contenido:**
- Navbar completo
- Hero section con formulario
- Quick stats (100% Offline, <5s, 0€)

**Cómo capturar:**
```bash
# Iniciar app
npm run dev
# o
npm run electron:dev

# Abrir: http://localhost:3000
# Capturar pantalla completa (Cmd+Shift+4 en Mac, Win+Shift+S en Windows)
```

---

### 2. **Features Section**
**Archivo:** `screenshot-02-features.png`  
**Resolución:** 1920x1080  
**Contenido:**
- 6 cards de funcionalidades
- Iconos y badges
- Diseño responsive visible

**Scroll:** Hacer scroll hasta la sección de features

---

### 3. **Audit Form con URL de Ejemplo**
**Archivo:** `screenshot-03-audit-form.png`  
**Resolución:** 1200x800  
**Contenido:**
- Formulario con URL ingresada
- Botón "Analizar Ahora"
- Links de ejemplo visibles

**Instrucciones:**
- Ingresar: `https://google.com` en el campo
- Capturar antes de hacer click en Analizar

---

### 4. **Loading State**
**Archivo:** `screenshot-04-loading.png`  
**Resolución:** 1200x800  
**Contenido:**
- Overlay de loading
- Spinner animado
- Mensaje "Analizando sitio web..."

**Instrucciones:**
- Click en "Analizar"
- Capturar durante el loading (primeros 2 segundos)

---

### 5. **Results - Score Cards**
**Archivo:** `screenshot-05-results.png`  
**Resolución:** 1920x1080  
**Contenido:**
- Score general (0-100)
- Scores individuales (Meta Tags, Headings, Images)
- Traffic lights (verde/amarillo/rojo)
- Detalles expandidos

**Instrucciones:**
- Esperar a que termine el análisis
- Capturar la sección de resultados completa

---

### 6. **Results - Detailed Analysis**
**Archivo:** `screenshot-06-details.png`  
**Resolución:** 1920x1080  
**Contenido:**
- Análisis detallado de meta tags
- Lista de headings encontrados
- Análisis de imágenes con alt text

---

### 7. **Electron App - macOS**
**Archivo:** `screenshot-07-electron-mac.png`  
**Resolución:** 1400x900  
**Contenido:**
- Ventana de Electron con barra de título macOS
- App completa visible
- DevTools cerrados

**Instrucciones:**
```bash
npm run electron:dev
# Capturar ventana completa de la app
```

---

### 8. **Electron App - Windows** (Si aplica)
**Archivo:** `screenshot-08-electron-win.png`  
**Resolución:** 1400x900  
**Contenido:**
- Ventana de Electron con barra de título Windows
- App completa visible

---

### 9. **Mobile View - Responsive**
**Archivo:** `screenshot-09-mobile.png`  
**Resolución:** 375x812 (iPhone)  
**Contenido:**
- Vista móvil del homepage
- Navbar colapsado
- Hero section adaptado

**Instrucciones:**
- Chrome DevTools (F12)
- Toggle device toolbar (Cmd+Shift+M)
- Seleccionar iPhone 13 Pro
- Capturar

---

### 10. **Code Example / Terminal**
**Archivo:** `screenshot-10-terminal.png`  
**Resolución:** 1200x600  
**Contenido:**
- Terminal con `npm run dev` ejecutándose
- Logs del servidor
- Mensajes de inicio exitoso

---

## 🎨 TIPS PARA SCREENSHOTS PROFESIONALES

### **Preparación:**
1. **Limpiar el entorno:**
   - Cerrar tabs innecesarias
   - Ocultar bookmarks bar
   - Modo sin distracciones

2. **Configurar resolución:**
   - Pantalla completa
   - Zoom al 100%
   - Retina display si disponible

3. **Temas:**
   - Usar modo claro (mejor contraste)
   - Fondo limpio
   - Colores vibrantes

### **Herramientas Recomendadas:**

#### **macOS:**
- **Cmd+Shift+3**: Pantalla completa
- **Cmd+Shift+4**: Selección personalizada
- **Cmd+Shift+4 + Espacio**: Capturar ventana
- **Preview**: Para editar

#### **Windows:**
- **Win+Shift+S**: Snipping tool
- **ShareX**: Herramienta avanzada
- **Lightshot**: Fácil de usar

#### **Linux:**
- **Flameshot**: Muy completo
- **Shutter**: Clásico
- **GNOME Screenshot**: Integrado

#### **Cross-Platform:**
- **Firefox**: Herramienta de captura integrada (Shift+F2)
- **Chrome DevTools**: Captura de viewport completo

---

## 📁 ORGANIZACIÓN DE ARCHIVOS

```
docs/
└── screenshots/
    ├── 01-homepage.png
    ├── 02-features.png
    ├── 03-audit-form.png
    ├── 04-loading.png
    ├── 05-results.png
    ├── 06-details.png
    ├── 07-electron-mac.png
    ├── 08-electron-win.png (opcional)
    ├── 09-mobile.png
    └── 10-terminal.png
```

---

## 🖼️ POST-PROCESAMIENTO

### **Edición Recomendada:**
1. **Redimensionar** si es necesario (mantener aspect ratio)
2. **Optimizar** para web (80-90% calidad)
3. **Añadir sombra** suave (opcional, para README)
4. **Recortar** espacios innecesarios

### **Herramientas:**
- **ImageOptim** (Mac) - Optimización sin pérdida
- **TinyPNG** (Web) - Compresión inteligente
- **Photopea** (Web) - Editor online gratuito
- **GIMP** (Cross-platform) - Editor completo

---

## 📝 USAR EN README.md

### **Sintaxis Markdown:**
```markdown
## 📸 Screenshots

### Homepage
![Homepage](docs/screenshots/01-homepage.png)

### Features
![Features](docs/screenshots/02-features.png)

### Audit Results
![Results](docs/screenshots/05-results.png)

### Mobile View
<p align="center">
  <img src="docs/screenshots/09-mobile.png" width="375" alt="Mobile View">
</p>
```

### **Galería en Tabla:**
```markdown
| Homepage | Features | Results |
|----------|----------|---------|
| ![](docs/screenshots/01-homepage.png) | ![](docs/screenshots/02-features.png) | ![](docs/screenshots/05-results.png) |
```

---

## ✅ CHECKLIST

- [ ] Screenshot 1: Homepage capturado
- [ ] Screenshot 2: Features capturado
- [ ] Screenshot 3: Audit Form capturado
- [ ] Screenshot 4: Loading capturado
- [ ] Screenshot 5: Results capturado
- [ ] Screenshot 6: Details capturado
- [ ] Screenshot 7: Electron Mac capturado
- [ ] Screenshot 8: Electron Win capturado (opcional)
- [ ] Screenshot 9: Mobile capturado
- [ ] Screenshot 10: Terminal capturado
- [ ] Todas las imágenes optimizadas
- [ ] Archivos organizados en docs/screenshots/
- [ ] README.md actualizado con screenshots

---

## 🎬 VIDEO DEMO (Opcional)

### **Para crear un GIF animado:**
```bash
# Herramientas:
# Mac: Kap (https://getkap.co)
# Windows: ScreenToGif
# Linux: Peek

# Qué grabar:
# - Ingresando URL
# - Click en Analizar
# - Loading animation
# - Resultados apareciendo
# Duración: 10-15 segundos
```

---

## 📞 NOTAS FINALES

- **Privacidad**: No incluir datos sensibles en screenshots
- **Copyright**: Solo capturar contenido propio o de ejemplo
- **Calidad**: Preferir PNG para UI, JPEG solo para fotos
- **Tamaño**: Mantener archivos <1MB por screenshot

---

**Repositorio:** https://github.com/Sol1973/SEO-Assistant  
**Documentación:** Ver INDEX.md  
**Última Actualización:** 15 de Octubre de 2025 - 12:15 (Madrid)

