# Assets - Recursos de la Aplicación

**Fecha:** 15 de Octubre de 2025 - 10:50 (Madrid)

## 📁 Estructura de Assets

```
assets/
├── icon.png          # Icono principal (512x512)
├── icon.ico          # Icono Windows
├── icon.icns         # Icono macOS
├── logo.svg          # Logo vectorial
└── favicon.ico       # Favicon web
```

## 🎨 Iconos Necesarios

### Para la Aplicación Web:
- `favicon.ico` - 16x16, 32x32, 48x48
- `logo.svg` - Logo escalable

### Para Electron (Desktop):
- `icon.png` - 512x512 (Linux AppImage)
- `icon.ico` - Multi-size (Windows portable)
- `icon.icns` - Multi-resolution (macOS DMG)

## 📋 TODO - Crear Iconos

Los iconos deben crearse con las siguientes especificaciones:

### Concepto de Diseño:
- **Tema**: SEO / Optimización / Analytics
- **Colores sugeridos**: 
  - Primario: #0d6efd (azul Bootstrap)
  - Secundario: #198754 (verde éxito)
  - Acento: #ffc107 (amarillo warning)
- **Elementos**: 
  - Lupa (búsqueda/auditoría)
  - Gráfico ascendente (mejora/ranking)
  - Checkmark (optimización)

### Herramientas Recomendadas:
- **Online**: 
  - Favicon.io
  - RealFaviconGenerator.net
  - ConvertICO.com
- **Desktop**:
  - Figma
  - Adobe Illustrator
  - Inkscape (gratis)

### Generación Rápida:
```bash
# Con ImageMagick (si está instalado)
convert icon.png -resize 512x512 icon-512.png
convert icon.png -define icon:auto-resize=256,128,64,48,32,16 icon.ico
```

## ⚠️ Nota Temporal

Por ahora, el proyecto funcionará sin iconos. Los iconos se agregarán en la **Sesión 3: UI/UX**.

Si intentas construir la app Electron sin iconos, se usará el icono por defecto de Electron.

