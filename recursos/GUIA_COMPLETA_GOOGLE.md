# 📊 GUÍA COMPLETA: GOOGLE ANALYTICS + SEARCH CONSOLE
**Configuración paso a paso para carmenalvarado.es**

---

## 📋 ÍNDICE

1. [Google Analytics](#google-analytics)
2. [Google Search Console](#google-search-console)
3. [Enviar Sitemap](#enviar-sitemap)
4. [Verificar Indexación](#verificar-indexación)
5. [Google My Business](#google-my-business)

---

## 📊 GOOGLE ANALYTICS

### **PASO 1: Crear Cuenta (5 minutos)**

1. **Ir a:** https://analytics.google.com/
2. **Click en:** "Empezar a medir"
3. **Nombre de cuenta:** Carmen Alvarado
4. **Click en:** Siguiente

### **PASO 2: Crear Propiedad (5 minutos)**

1. **Nombre de propiedad:** carmenalvarado.es
2. **Zona horaria:** España (Madrid) ⏰
3. **Moneda:** EUR - Euro (€)
4. **Click en:** Siguiente

### **PASO 3: Detalles de la Empresa**

1. **Categoría:** Salud y bienestar
2. **Tamaño:** 1-10 empleados
3. **Objetivos:** Generar clientes potenciales
4. **Click en:** Crear

### **PASO 4: Configurar Flujo de Datos**

1. **Plataforma:** Web
2. **URL del sitio web:** https://carmenalvarado.es
3. **Nombre del flujo:** Carmen Alvarado - Web
4. **Click en:** Crear flujo

### **PASO 5: Copiar ID de Medición**

Te aparecerá algo como: **G-XXXXXXXXXX**

📋 **Copia este ID** (lo necesitarás en el siguiente paso)

---

## 🔧 INSTALAR GOOGLE ANALYTICS EN EL SITIO

### **Código a agregar:**

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**⚠️ Reemplaza `G-XXXXXXXXXX` con tu ID real**

### **Dónde agregar:**

En el `<head>` de **TODAS las páginas**, justo antes del `</head>`:

**Páginas ES (5):**
1. index.html
2. contacto.html
3. ayuda.html
4. consejos.html
5. gracias.html

**Páginas CA (5):**
6. index-ca.html
7. contacte-ca.html
8. ajuda-ca.html
9. consells-ca.html
10. gracies-ca.html

### **Cómo agregarlo:**

**Opción 1: Manualmente** (editar cada archivo)

**Opción 2: Con script** (más rápido):

```bash
# Crear el snippet con tu ID real
cat > ga-snippet.txt << 'EOF'
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-TU_ID_AQUI"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-TU_ID_AQUI');
</script>
EOF

# Luego yo te ayudo a insertarlo en todos los archivos
```

---

## 🔍 GOOGLE SEARCH CONSOLE

### **PASO 1: Agregar Propiedad (5 minutos)**

1. **Ir a:** https://search.google.com/search-console
2. **Click en:** "Agregar propiedad"
3. **Seleccionar:** Prefijo de URL
4. **URL:** https://carmenalvarado.es
5. **Click en:** Continuar

### **PASO 2: Verificar Propiedad**

**Método 1: Archivo HTML (RECOMENDADO)**

1. Google te dará un archivo: `google1234567890abcdef.html`
2. **Descarga el archivo**
3. **Sube al servidor:**

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# Copiar el archivo descargado aquí, luego:
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  google*.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

4. **Volver a Search Console** y click en "Verificar"

**Método 2: Etiqueta HTML (Alternativa)**

Si prefieres, puedes agregar una meta tag en `index.html` e `index-ca.html`:

```html
<meta name="google-site-verification" content="tu_codigo_aqui" />
```

---

## 🗺️ ENVIAR SITEMAP

### **PASO 1: Verificar Sitemap**

Tu sitemap ya está listo en:
- https://carmenalvarado.es/sitemap.xml

Verifica que funciona:
```bash
curl -s https://carmenalvarado.es/sitemap.xml | grep -c "<loc>"
```

Debe mostrar: **10** (5 ES + 5 CA)

### **PASO 2: Enviar a Google Search Console**

1. En Search Console, ir a **"Sitemaps"** (menú izquierdo)
2. En "Agregar un sitemap nuevo"
3. Escribir: **sitemap.xml**
4. Click en **"Enviar"**

### **PASO 3: Verificar Estado**

Después de unas horas, verás:
- ✅ Estado: Correcto
- ✅ URLs descubiertas: 10
- ✅ URLs indexadas: (irá aumentando)

---

## 🌐 VERIFICAR HREFLANG EN SEARCH CONSOLE

### **Después de 1-2 días:**

1. Ir a **"Segmentación internacional"**
2. Pestaña **"Idioma"**
3. Debe mostrar:
   - ✅ Español (es) - 5 páginas
   - ✅ Catalán (ca) - 5 páginas
4. Si hay errores de hreflang, te los mostrará aquí

---

## 📈 CONFIGURAR OBJETIVOS EN ANALYTICS

### **Objetivo 1: Envío de Formulario**

Ya está implementado en `main.js`:
```javascript
gtag('event', 'form_submission', {
    'event_category': 'contact',
    'event_label': 'contact_form'
});
```

### **Objetivo 2: Click en Teléfono**

Ya está implementado:
```javascript
gtag('event', 'phone_call', {
    'event_category': 'contact',
    'event_label': phoneNumber
});
```

### **Objetivo 3: Click en WhatsApp**

Ya está implementado:
```javascript
gtag('event', 'whatsapp_click', {
    'event_category': 'contact',
    'event_label': 'floating_button'
});
```

---

## 🎯 MÉTRICAS A MONITOREAR

### **En Google Analytics:**

**Panel Principal:**
- Usuarios en tiempo real
- Usuarios totales (últimos 7/30 días)
- Sesiones
- Tasa de rebote

**Adquisición:**
- Orgánico (Google)
- Directo
- Referidos
- Social

**Comportamiento:**
- Páginas más visitadas
- Tiempo en página
- Flujo de usuarios

**Conversiones:**
- Formularios enviados
- Llamadas telefónicas
- Clicks en WhatsApp

### **En Google Search Console:**

**Rendimiento:**
- Impresiones totales
- Clicks totales
- CTR promedio
- Posición promedio

**Por Query:**
- "cuidadora personas mayores tarragona"
- "técnico sociosanitario tarragona"
- "cuidadora persones grans tarragona"

**Cobertura:**
- Páginas indexadas (objetivo: 10/10)
- Errores de indexación (objetivo: 0)
- Páginas válidas con advertencias

**Experiencia:**
- Core Web Vitals
- Usabilidad móvil
- HTTPS

---

## 📋 CHECKLIST DE CONFIGURACIÓN

### **Google Analytics:**
- [ ] Crear cuenta
- [ ] Crear propiedad
- [ ] Obtener ID de medición (G-XXXXXXXXXX)
- [ ] Agregar código en 10 páginas
- [ ] Subir páginas actualizadas
- [ ] Verificar que funciona (tiempo real)

### **Google Search Console:**
- [ ] Agregar propiedad
- [ ] Verificar con archivo HTML
- [ ] Enviar sitemap.xml
- [ ] Verificar indexación
- [ ] Revisar errores de hreflang
- [ ] Configurar segmentación internacional

### **Sitemap:**
- [x] Sitemap.xml creado (10 URLs)
- [x] Hreflang tags en sitemap
- [x] Subido al servidor
- [ ] Enviado a Search Console

---

## 🚀 ORDEN DE IMPLEMENTACIÓN

### **1. AHORA (yo lo hago):**
- ✅ Sitemap.xml actualizado y subido
- ✅ Robots.txt configurado y subido
- ⏳ Preparar snippet de Analytics

### **2. TÚ HACES (cuando tengas el ID de GA):**
- [ ] Crear cuenta Google Analytics
- [ ] Copiar ID de medición
- [ ] Darme el ID para agregarlo a las páginas
- [ ] Yo actualizo las 10 páginas
- [ ] Subimos al servidor

### **3. TÚ HACES (después de Analytics):**
- [ ] Registrar en Search Console
- [ ] Descargar archivo de verificación
- [ ] Subirlo al servidor
- [ ] Verificar propiedad
- [ ] Enviar sitemap

---

## 📊 TIEMPO ESTIMADO

- **Google Analytics:** 15 minutos (crear cuenta + obtener ID)
- **Agregar código GA:** 10 minutos (yo lo hago)
- **Subir archivos:** 2 minutos
- **Search Console:** 10 minutos (verificar + enviar sitemap)

**Total:** ~40 minutos

---

## 💡 PRÓXIMOS PASOS INMEDIATOS

### **Opción A: Hacerlo ahora**
1. Tú creas cuenta Google Analytics
2. Me das el ID (G-XXXXXXXXXX)
3. Yo agrego el código en las 10 páginas
4. Subimos
5. Configuras Search Console

### **Opción B: Hacerlo después**
Te dejo todo documentado y lo haces cuando quieras

---

**¿Qué prefieres: A o B?** 

Si eliges A, crea la cuenta de Analytics ahora y dame el ID. Si eliges B, todo está documentado para cuando quieras. 😊

