# 🎨 FAVICON PARA CARMENALVARADO.ES

## 📋 TAREA PENDIENTE: CREAR FAVICON

### **¿Qué es un favicon?**
El favicon es el pequeño icono que aparece en la pestaña del navegador junto al título de la página.

---

## 🎨 OPCIONES DE DISEÑO

### **Opción 1: Iniciales "CA"**
- Diseño: Letras "CA" en un círculo
- Colores: Azul (#2c5f7c) sobre fondo blanco
- Estilo: Profesional, minimalista
- **RECOMENDADO** ✅

### **Opción 2: Corazón + Cruz**
- Diseño: Corazón con cruz médica
- Colores: Azul y naranja (colores del sitio)
- Estilo: Representa cuidado + salud
- Alternativa válida

### **Opción 3: Manos**
- Diseño: Dos manos cuidando
- Colores: Azul principal
- Estilo: Emocional, cálido
- Más complejo de diseñar

---

## 📐 ESPECIFICACIONES TÉCNICAS

### **Tamaños necesarios:**
```
favicon.ico       → 16x16, 32x32, 48x48 (multi-size)
favicon-16x16.png → 16x16 px
favicon-32x32.png → 32x32 px
apple-touch-icon.png → 180x180 px (iOS)
android-chrome-192x192.png → 192x192 px (Android)
android-chrome-512x512.png → 512x512 px (Android)
```

### **Código HTML a agregar:**
```html
<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

---

## 🛠️ HERRAMIENTAS PARA CREAR FAVICON

### **Opción 1: Generador Online (RECOMENDADO)**
- **Favicon.io:** https://favicon.io/
  - Crear desde texto (CA)
  - Genera todos los tamaños automáticamente
  - Descarga ZIP con todos los archivos

### **Opción 2: Canva**
- Crear diseño 512x512 px
- Exportar como PNG
- Usar Favicon.io para generar tamaños

### **Opción 3: Figma/Photoshop**
- Diseño profesional personalizado
- Exportar en todos los tamaños manualmente

---

## 📝 PASOS PARA IMPLEMENTAR

### **1. Crear el favicon:**
1. Ir a https://favicon.io/favicon-generator/
2. Configurar:
   - **Text:** CA
   - **Background:** #2c5f7c (azul del sitio)
   - **Font Color:** #ffffff (blanco)
   - **Font Family:** Poppins o Roboto
   - **Font Size:** 110
   - **Shape:** Circle

3. Click en "Download"
4. Descomprimir el ZIP

### **2. Subir archivos al servidor:**
```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# Copiar archivos del favicon descargado
# Luego subir:

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  favicon.ico \
  favicon-16x16.png \
  favicon-32x32.png \
  apple-touch-icon.png \
  android-chrome-192x192.png \
  android-chrome-512x512.png \
  site.webmanifest \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

### **3. Actualizar HTML:**
Agregar en el `<head>` de todas las páginas:
- `index.html`
- `index-ca.html`
- `contacto.html`
- `contacte-ca.html`
- `ayuda.html`
- `ajuda-ca.html`
- `gracias.html`
- `gracies-ca.html`

---

## 🎨 DISEÑO RECOMENDADO

### **Favicon Principal:**
```
┌─────────────┐
│             │
│     CA      │  ← Letras "CA" en blanco
│             │     Fondo azul #2c5f7c
│             │     Círculo redondeado
└─────────────┘
```

### **Colores del sitio:**
- **Azul principal:** #2c5f7c
- **Azul secundario:** #4a8fb5
- **Naranja acento:** #e8956f
- **Blanco:** #ffffff

---

## 📱 ARCHIVO site.webmanifest

```json
{
    "name": "Carmen Alvarado - Cuidadora Profesional",
    "short_name": "Carmen Alvarado",
    "icons": [
        {
            "src": "/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#2c5f7c",
    "background_color": "#ffffff",
    "display": "standalone"
}
```

---

## ✅ CHECKLIST

- [ ] Crear favicon con iniciales "CA"
- [ ] Generar todos los tamaños (favicon.io)
- [ ] Descargar ZIP
- [ ] Subir archivos al servidor
- [ ] Actualizar `index.html` con tags
- [ ] Actualizar `contacto.html` con tags
- [ ] Actualizar páginas en catalán (cuando se creen)
- [ ] Verificar en navegador (Ctrl + F5 para limpiar caché)
- [ ] Verificar en móvil (iOS y Android)

---

## 🔗 ENLACES ÚTILES

- **Favicon.io:** https://favicon.io/favicon-generator/
- **RealFaviconGenerator:** https://realfavicongenerator.net/
- **Favicon Checker:** https://realfavicongenerator.net/favicon_checker

---

## ⏰ TIEMPO ESTIMADO

- Crear favicon: **5 minutos**
- Subir archivos: **2 minutos**
- Actualizar HTML: **5 minutos**
- Verificar: **3 minutos**

**Total:** ~15 minutos

---

## 📌 NOTA IMPORTANTE

El favicon actual en el código es:
```html
<link rel="icon" type="image/x-icon" href="images/favicon.ico">
```

Pero el archivo **NO EXISTE** en el servidor. Por eso no se ve ningún favicon actualmente.

---

**Documento creado:** 13 de octubre de 2025  
**Estado:** ⏳ Pendiente de crear  
**Prioridad:** MEDIA (no afecta funcionalidad, solo branding)

