# 📊 GOOGLE ANALYTICS Y SEARCH CONSOLE - INSTRUCCIONES

## 🎯 GOOGLE ANALYTICS 4 (GA4)

### **Paso 1: Crear Cuenta**

1. Ir a: https://analytics.google.com/
2. Click en "Empezar a medir"
3. Nombre de la cuenta: "Carmen Alvarado"
4. Nombre de la propiedad: "carmenalvarado.es"
5. Zona horaria: **España (Madrid)**
6. Moneda: **EUR (€)**

### **Paso 2: Configurar Flujo de Datos**

1. Seleccionar "Web"
2. URL del sitio web: **https://carmenalvarado.es**
3. Nombre del flujo: "Carmen Alvarado - Web"
4. Click en "Crear flujo"

### **Paso 3: Obtener ID de Medición**

Copiarás algo como: **G-XXXXXXXXXX**

### **Paso 4: Agregar Código a TODAS las Páginas**

**Agregar en el `<head>` de cada página (antes del `</head>`):**

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Reemplaza `G-XXXXXXXXXX` con tu ID real.**

### **Páginas donde agregar (10 archivos):**

**Español:**
1. index.html
2. contacto.html
3. ayuda.html
4. consejos.html
5. gracias.html

**Catalán:**
6. index-ca.html
7. contacte-ca.html
8. ajuda-ca.html
9. consells-ca.html
10. gracies-ca.html

---

## 🔍 GOOGLE SEARCH CONSOLE

### **Paso 1: Agregar Propiedad**

1. Ir a: https://search.google.com/search-console
2. Click en "Agregar propiedad"
3. Tipo: **Prefijo de URL**
4. URL: **https://carmenalvarado.es**

### **Paso 2: Verificar Propiedad**

**Método 1: Archivo HTML (RECOMENDADO)**

1. Google te dará un archivo como: `google1234567890abcdef.html`
2. Descárgalo
3. Súbelo a la raíz del sitio:
   ```bash
   rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
     google1234567890abcdef.html \
     u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
   ```
4. Click en "Verificar"

**Método 2: Etiqueta HTML**

Agregar en el `<head>` de `index.html` e `index-ca.html`:
```html
<meta name="google-site-verification" content="tu_codigo_aqui" />
```

### **Paso 3: Enviar Sitemap**

1. En Search Console, ir a "Sitemaps"
2. Agregar URL del sitemap: **https://carmenalvarado.es/sitemap.xml**
3. Click en "Enviar"

### **Paso 4: Configurar Idiomas**

1. Ir a "Configuración" → "Segmentación internacional"
2. Verificar que detecta hreflang correctamente
3. Debe mostrar: ES y CA

---

## 🗺️ SITEMAP.XML ACTUALIZADO

**Ya está actualizado con:**
- ✅ 5 páginas en español
- ✅ 5 páginas en catalán
- ✅ Hreflang tags en cada URL
- ✅ Prioridades correctas
- ✅ Fechas actualizadas

**Archivo:** `sitemap.xml` (listo para subir)

---

## 🤖 ROBOTS.TXT

**Ya está configurado correctamente.**

Permite:
- ✅ Todas las páginas HTML
- ✅ CSS, JS, imágenes
- ✅ Sitemap

Bloquea:
- ❌ WordPress admin
- ❌ Plugins y themes
- ❌ URLs con parámetros

---

## 🔗 ENLACES INTERNOS

### **Enlaces entre idiomas (ya implementado):**

**Selector de idioma en header:**
- Todas las páginas ES tienen botón → CA
- Todas las páginas CA tienen botón → ES

**Hreflang tags:**
- Todas las páginas tienen hreflang ES ↔ CA
- Google sabe qué versión mostrar según idioma del usuario

### **Enlaces internos dentro del mismo idioma:**

**Páginas ES:**
- index.html → contacto.html, ayuda.html, consejos.html
- contacto.html → index.html
- ayuda.html → index.html, contacto.html
- consejos.html → index.html, contacto.html

**Páginas CA:**
- index-ca.html → contacte-ca.html, ajuda-ca.html, consells-ca.html
- contacte-ca.html → index-ca.html
- ajuda-ca.html → index-ca.html, contacte-ca.html
- consells-ca.html → index-ca.html, contacte-ca.html

---

## 🌐 ENLACES EXTERNOS

### **Redes Sociales (futuro):**

Cuando tengas redes sociales, agregar en footer:
```html
<div class="social-links">
    <a href="https://facebook.com/tu_pagina" target="_blank" rel="noopener">Facebook</a>
    <a href="https://instagram.com/tu_cuenta" target="_blank" rel="noopener">Instagram</a>
</div>
```

### **Directorios Locales (recomendado):**

Registrar el sitio en:
1. **Google My Business** (esencial para SEO local)
2. **Páginas Amarillas**
3. **Infoisinfo**
4. **11870.com**
5. **Yelp España**

---

## 📈 EVENTOS PERSONALIZADOS EN GOOGLE ANALYTICS

**Ya implementados en `main.js`:**

1. ✅ **Envío de formulario:**
   ```javascript
   gtag('event', 'form_submission', {
       'event_category': 'contact',
       'event_label': 'contact_form'
   });
   ```

2. ✅ **Click en teléfono:**
   ```javascript
   gtag('event', 'phone_call', {
       'event_category': 'contact',
       'event_label': phoneNumber
   });
   ```

3. ✅ **Click en WhatsApp:**
   ```javascript
   gtag('event', 'whatsapp_click', {
       'event_category': 'contact',
       'event_label': 'floating_button'
   });
   ```

4. ✅ **Tiempo en página**
5. ✅ **Profundidad de scroll**

---

## 📊 MÉTRICAS A MONITOREAR

### **Google Search Console:**

1. **Impresiones por keyword:**
   - cuidadora personas mayores tarragona
   - técnico sociosanitario tarragona
   - cuidadora persones grans tarragona (CA)

2. **CTR (Click-Through Rate):**
   - Objetivo: >3% (promedio 2%)

3. **Posición promedio:**
   - Objetivo: Top 10 en 3 meses
   - Objetivo: Top 5 en 6 meses

4. **Errores:**
   - 404s
   - Problemas de indexación
   - Errores de hreflang

### **Google Analytics:**

1. **Usuarios:**
   - Total de visitantes
   - Nuevos vs recurrentes
   - Por idioma (ES vs CA)

2. **Conversiones:**
   - Envíos de formulario
   - Clicks en teléfono
   - Clicks en WhatsApp

3. **Comportamiento:**
   - Páginas más visitadas
   - Tiempo en página
   - Tasa de rebote

4. **Fuentes de tráfico:**
   - Orgánico (Google)
   - Directo
   - Referidos
   - Social (futuro)

---

## 🎯 OBJETIVOS MENSUALES

### **Mes 1 (Octubre 2025):**
- [ ] Instalar Google Analytics
- [ ] Registrar en Search Console
- [ ] Enviar sitemap
- [ ] Verificar indexación de todas las páginas
- [ ] Baseline de métricas

### **Mes 2 (Noviembre 2025):**
- [ ] 50+ visitantes/mes
- [ ] 5+ conversiones (formularios/llamadas)
- [ ] Top 20 para keywords principales
- [ ] 0 errores de indexación

### **Mes 3 (Diciembre 2025):**
- [ ] 100+ visitantes/mes
- [ ] 10+ conversiones
- [ ] Top 10 para "técnico sociosanitario tarragona"
- [ ] Top 15 para "cuidadora personas mayores tarragona"

---

## 🔗 ESTRUCTURA DE ENLACES INTERNOS

### **Arquitectura del sitio:**

```
Inicio (ES/CA)
    ├─→ Servicios (sección interna)
    ├─→ Sobre Mí (sección interna)
    ├─→ Te Ayudamos / T'Ajudem
    │   ├─→ Miedo / Por
    │   ├─→ Culpa / Culpa
    │   ├─→ Agotado / Esgotat
    │   ├─→ Dinero / Diners
    │   └─→ Dudas / Dubtes
    ├─→ Consejos / Consells
    │   ├─→ Higiene / Higiene
    │   ├─→ Medicación / Medicació
    │   ├─→ Alimentación / Alimentació
    │   ├─→ Movilidad / Mobilitat
    │   ├─→ Estimulación / Estimulació
    │   ├─→ Emocional / Emocional
    │   └─→ Ayuda Profesional / Ajuda Professional
    └─→ Contacto / Contacte
        └─→ Gracias / Gràcies
```

### **Profundidad de enlaces:**
- Nivel 1: Inicio (0 clicks)
- Nivel 2: Servicios, Contacto, Te Ayudamos, Consejos (1 click)
- Nivel 3: Sub-temas, Gracias (2 clicks)

**Objetivo SEO:** Todas las páginas a máximo 2 clicks desde inicio ✅

---

## 📱 GOOGLE MY BUSINESS (ESENCIAL)

### **Crear perfil:**

1. Ir a: https://business.google.com/
2. Crear perfil de empresa
3. Datos:
   - **Nombre:** Carmen Alvarado - Cuidadora Profesional
   - **Categoría:** Servicio de atención domiciliaria
   - **Dirección:** Tarragona (si no quieres mostrar dirección exacta, marca "Ocultar dirección")
   - **Área de servicio:** Tarragona, Reus
   - **Teléfono:** 611 230 547
   - **Sitio web:** https://carmenalvarado.es
   - **Horario:** Lunes-Domingo 8:00-21:00

4. Verificación: Google enviará postal o llamada

### **Optimizar perfil:**

- Agregar fotos profesionales
- Descripción: "Técnica sociosanitaria titulada en Tarragona. Atención domiciliaria profesional para personas mayores y dependientes. Disponibilidad inmediata."
- Servicios: Listar todos los servicios
- Preguntas y respuestas
- Pedir reseñas a clientes satisfechos

---

## 🎯 CHECKLIST SEO COMPLETO

### **On-Page SEO:**
- [x] Keywords optimizadas (ES y CA)
- [x] Title tags únicos
- [x] Meta descriptions únicas
- [x] H1, H2, H3 optimizados
- [x] URLs amigables
- [x] Imágenes con alt text (pendiente)
- [x] Velocidad de carga < 3 seg
- [x] Mobile-friendly
- [x] Schema.org markup
- [x] Canonical URLs

### **Technical SEO:**
- [x] Sitemap.xml actualizado
- [x] Robots.txt configurado
- [x] Hreflang tags (multiidioma)
- [x] HTTPS (SSL)
- [x] .htaccess optimizado
- [ ] Google Analytics instalado (pendiente)
- [ ] Search Console configurado (pendiente)

### **Local SEO:**
- [x] Geo tags en HTML
- [x] "Tarragona" y "Reus" en contenido
- [x] Dirección en Schema.org
- [ ] Google My Business (pendiente)
- [ ] Directorios locales (pendiente)

### **Content SEO:**
- [x] Contenido único y relevante
- [x] Keywords naturales
- [x] FAQs optimizadas
- [x] Contenido emocional (pain points)
- [x] CTAs claros

### **Multiidioma SEO:**
- [x] Hreflang tags
- [x] Lang attribute
- [x] Canonical URLs separados
- [x] Selector de idioma visible
- [x] URLs diferentes por idioma

---

## 📤 ARCHIVOS A SUBIR

### **Archivos SEO:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  sitemap.xml \
  robots.txt \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

### **Páginas actualizadas:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html \
  contacto.html \
  gracias.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

### **Páginas en catalán:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index-ca.html \
  contacte-ca.html \
  ajuda-ca.html \
  gracies-ca.html \
  consells-ca.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

## 🎯 PRÓXIMOS PASOS (DESPUÉS DE SUBIR)

### **Inmediato (hoy):**
1. Subir todos los archivos
2. Verificar que funcionan
3. Probar selector de idioma
4. Probar formularios en ambos idiomas

### **Esta semana:**
1. Crear cuenta Google Analytics
2. Instalar código GA en todas las páginas
3. Registrar en Google Search Console
4. Enviar sitemap
5. Verificar indexación

### **Próximas 2 semanas:**
1. Crear Google My Business
2. Registrar en directorios locales
3. Optimizar imágenes (alt text)
4. Crear favicon

### **Próximo mes:**
1. Primer blog post
2. Primeras reseñas de clientes
3. Análisis de métricas
4. Ajustes según datos

---

## 📊 DASHBOARD DE MÉTRICAS (FUTURO)

### **KPIs Principales:**

1. **Tráfico Orgánico:**
   - Usuarios/mes
   - Sesiones/mes
   - Páginas/sesión

2. **Conversiones:**
   - Formularios enviados
   - Llamadas telefónicas
   - Clicks en WhatsApp

3. **SEO:**
   - Posición promedio
   - Impresiones
   - CTR
   - Keywords en Top 10

4. **Engagement:**
   - Tiempo en página
   - Tasa de rebote
   - Páginas más visitadas

---

## 🎯 OBJETIVOS 3 MESES

### **Tráfico:**
- 200+ visitantes/mes
- 50% orgánico (Google)
- 30% directo
- 20% otros

### **Conversiones:**
- 15+ contactos/mes
- Tasa de conversión: 5-10%

### **SEO:**
- Top 5: "técnico sociosanitario tarragona"
- Top 10: "cuidadora personas mayores tarragona"
- Top 5: "cuidadora persones grans tarragona" (CA)

---

**Documento creado:** 13 de octubre de 2025  
**Estado:** ✅ Listo para implementar

