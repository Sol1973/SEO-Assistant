# 📱 SOLUCIÓN: PÁGINA NO CARGA EN MÓVILES NUEVOS

## 🔍 DIAGNÓSTICO

El sitio **SÍ está funcionando** (código 200 OK), pero puede haber problemas de caché o visualización en móviles.

---

## ✅ SOLUCIONES

### **Solución 1: Limpiar Caché del Servidor (RECOMENDADO)**

```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172

# Limpiar caché de LiteSpeed
cd domains/carmenalvarado.es/public_html
wp litespeed-purge all

# O manualmente
rm -rf wp-content/cache/*
rm -rf .litespeed_cache/*

exit
```

---

### **Solución 2: Agregar Cache-Control Headers**

Crear archivo `.htaccess` con configuración de caché:

```apache
# Ya existe en el servidor, pero agregar esto:

# Cache-Control para HTML (sin caché)
<FilesMatch "\.(html|htm)$">
    Header set Cache-Control "no-cache, no-store, must-revalidate"
    Header set Pragma "no-cache"
    Header set Expires 0
</FilesMatch>

# Cache para CSS y JS (1 semana)
<FilesMatch "\.(css|js)$">
    Header set Cache-Control "public, max-age=604800"
</FilesMatch>

# Cache para imágenes (1 mes)
<FilesMatch "\.(jpg|jpeg|png|gif|ico|svg|webp)$">
    Header set Cache-Control "public, max-age=2592000"
</FilesMatch>
```

---

### **Solución 3: Versionar CSS y JS**

Cambiar en todas las páginas:

```html
<!-- ANTES -->
<link rel="stylesheet" href="css/styles.css">
<script src="js/main.js"></script>

<!-- DESPUÉS (con versión) -->
<link rel="stylesheet" href="css/styles.css?v=1.0">
<script src="js/main.js?v=1.0"></script>
```

Esto fuerza a los navegadores a recargar los archivos.

---

### **Solución 4: Verificar en Modo Incógnito**

**En el móvil:**
1. Abrir navegador en **modo incógnito/privado**
2. Ir a: https://carmenalvarado.es/
3. Si funciona → El problema es caché
4. Si no funciona → Hay otro problema

---

### **Solución 5: Verificar Viewport en Móvil**

El meta viewport ya está correcto:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## 🔍 DIAGNÓSTICO DETALLADO

### **¿Qué ves exactamente en el móvil?**

**A) Página en blanco:**
- Problema: CSS no carga
- Solución: Limpiar caché del servidor

**B) Página sin estilos (solo texto):**
- Problema: CSS bloqueado o ruta incorrecta
- Solución: Verificar ruta del CSS

**C) Página no carga (error):**
- Problema: Conexión o DNS
- Solución: Verificar DNS

**D) Página carga pero se ve mal:**
- Problema: CSS responsive
- Solución: Revisar media queries

---

## 🚀 ACCIÓN INMEDIATA

### **Ejecuta esto AHORA para limpiar caché:**

```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172 "cd domains/carmenalvarado.es/public_html && wp litespeed-purge all"
```

---

### **Luego prueba en el móvil:**

1. **Cierra completamente el navegador** en el móvil
2. **Abre de nuevo**
3. **Ve a:** https://carmenalvarado.es/
4. **Debe cargar correctamente**

---

## 📊 VERIFICAR RESPONSIVE

### **Desde tu ordenador:**

1. Abre: https://carmenalvarado.es/
2. Presiona `F12` (abrir DevTools)
3. Click en el icono de móvil (arriba a la izquierda)
4. Selecciona "iPhone 12 Pro" o "Samsung Galaxy"
5. Verifica que se vea bien

---

## 🆘 SI PERSISTE EL PROBLEMA

**Dime exactamente qué ves en el móvil:**
- ¿Página en blanco?
- ¿Solo texto sin estilos?
- ¿Error 404?
- ¿Carga infinita?
- ¿Se ve mal el diseño?

Y te doy la solución específica.

---

## 💡 NOTA IMPORTANTE

**Caché de LiteSpeed:**
- Hostinger usa LiteSpeed Cache
- Puede guardar versiones antiguas de las páginas
- Hay que purgarlo después de cada cambio

**Comando para purgar:**
```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172 "cd domains/carmenalvarado.es/public_html && wp litespeed-purge all"
```

---

**¿Quieres que limpie la caché del servidor ahora?** 🧹
