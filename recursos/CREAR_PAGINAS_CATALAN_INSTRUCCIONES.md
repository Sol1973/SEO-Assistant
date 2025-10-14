# 🇨🇦 CREAR PÁGINAS EN CATALÁN - INSTRUCCIONES COMPLETAS
**Próxima sesión - Todo preparado**

---

## ✅ LO QUE YA ESTÁ LISTO

1. ✅ **Investigación de keywords en catalán** (keywords_catalan.json)
2. ✅ **Diccionario de traducciones completo** (traducciones_catalan.json)
3. ✅ **Páginas en castellano optimizadas** (base para traducir)
4. ✅ **Estructura SEO definida**

---

## 📋 ARCHIVOS A CREAR (5 páginas)

1. **`index-ca.html`** - Página principal
2. **`contacte-ca.html`** - Contacto (nota: "contacte" no "contacto")
3. **`ajuda-ca.html`** - Te Ayudamos
4. **`gracies-ca.html`** - Gracias
5. **`consells-ca.html`** - Consejos

---

## 🎯 KEYWORDS OPTIMIZADAS EN CATALÁN

### **Para `index-ca.html`:**

**Title:**
```html
<title>Cuidadora Persones Grans Tarragona | Tècnica Sociosanitària Titulada | Carmen Alvarado</title>
```

**Meta Description:**
```html
<meta name="description" content="Cuidadora professional i tècnica sociosanitària titulada a Tarragona. Atenció domiciliària personalitzada per a persones grans i dependents. Disponibilitat immediata. ☎️ 611 230 547">
```

**Meta Keywords:**
```html
<meta name="keywords" content="cuidadora persones grans tarragona, tècnic sociosanitari tarragona, atenció domiciliària tarragona, auxiliar geriatria tarragona, cuidadora a domicili tarragona, cura persones dependents tarragona">
```

**H1:**
```html
<h1>Cuidadora de Persones Grans a Tarragona | Tècnica Sociosanitària Titulada</h1>
```

---

## ⚙️ CAMBIOS TÉCNICOS NECESARIOS

### **1. Lang Attribute:**
```html
<!-- Cambiar de: -->
<html lang="es">

<!-- A: -->
<html lang="ca">
```

### **2. Hreflang Tags (agregar en TODAS las páginas ES y CA):**

**En páginas ES (index.html, contacto.html, etc.):**
```html
<link rel="alternate" hreflang="es" href="https://carmenalvarado.es/index.html" />
<link rel="alternate" hreflang="ca" href="https://carmenalvarado.es/index-ca.html" />
<link rel="alternate" hreflang="x-default" href="https://carmenalvarado.es/" />
```

**En páginas CA (index-ca.html, contacte-ca.html, etc.):**
```html
<link rel="alternate" hreflang="es" href="https://carmenalvarado.es/index.html" />
<link rel="alternate" hreflang="ca" href="https://carmenalvarado.es/index-ca.html" />
<link rel="alternate" hreflang="x-default" href="https://carmenalvarado.es/" />
```

### **3. Canonical URL:**
```html
<!-- index-ca.html -->
<link rel="canonical" href="https://carmenalvarado.es/index-ca.html">

<!-- contacte-ca.html -->
<link rel="canonical" href="https://carmenalvarado.es/contacte-ca.html">
```

### **4. OG Locale:**
```html
<!-- Cambiar de: -->
<meta property="og:locale" content="es_ES">

<!-- A: -->
<meta property="og:locale" content="ca_ES">
```

### **5. OG URL:**
```html
<!-- index-ca.html -->
<meta property="og:url" content="https://carmenalvarado.es/index-ca.html">

<!-- contacte-ca.html -->
<meta property="og:url" content="https://carmenalvarado.es/contacte-ca.html">
```

---

## 🎨 SELECTOR DE IDIOMA

### **Agregar en el header de TODAS las páginas (ES y CA):**

```html
<!-- Agregar después del logo, dentro del nav-container -->
<div class="language-selector" style="position: absolute; top: 20px; right: 20px; z-index: 100;">
    <a href="index.html" style="color: #2c5f7c; font-weight: 600; text-decoration: none; padding: 0.5rem 1rem; background: white; border-radius: 5px; margin-right: 0.5rem;">ES</a>
    <a href="index-ca.html" style="color: #2c5f7c; font-weight: 600; text-decoration: none; padding: 0.5rem 1rem; background: white; border-radius: 5px;">CA</a>
</div>
```

**Ajustar según la página:**
- En `index.html` → href="index-ca.html"
- En `contacto.html` → href="contacte-ca.html"
- En `ayuda.html` → href="ajuda-ca.html"
- En `consejos.html` → href="consells-ca.html"
- En `gracias.html` → href="gracies-ca.html"

---

## 📝 TRADUCCIONES PRINCIPALES

### **Navegación:**
```
Inicio → Inici
Servicios → Serveis
Sobre Mí → Sobre Mi
Te Ayudamos → T'Ajudem
Consejos → Consells
Contacto → Contacte
```

### **Formulario:**
```
Tu nombre completo → El teu nom complet
Teléfono de contacto → Telèfon de contacte
Correo electrónico → Correu electrònic
Ciudad → Ciutat
Selecciona tu ciudad → Selecciona la teva ciutat
¿Qué tipo de ayuda necesitas? → Quin tipus d'ajuda necessites?
Cuidados a domicilio → Cures a domicili
Acompañamiento médico → Acompanyament mèdic
Ayuda con medicación → Ajuda amb medicació
Cuidados post-hospitalización → Cures post-hospitalització
Compañía y conversación → Companyia i conversa
¿Cuándo necesitas el servicio? → Quan necessites el servei?
Inmediato (esta semana) → Immediat (aquesta setmana)
Próximas 2 semanas → Properes 2 setmanes
Próximo mes → Proper mes
Solo busco información → Només busco informació
Cuéntame más sobre tu familiar → Explica'm més sobre el teu familiar
Enviar Mensaje → Enviar Missatge
Enviar Consulta Gratuita → Enviar Consulta Gratuïta
```

### **WhatsApp (cambiar el mensaje):**
```
<!-- ES -->
https://wa.me/34611230547?text=Hola%20Carmen,%20necesito%20información%20sobre%20cuidado%20de%20personas%20mayores%20en%20Tarragona

<!-- CA -->
https://wa.me/34611230547?text=Hola%20Carmen,%20necessito%20informació%20sobre%20cura%20de%20persones%20grans%20a%20Tarragona
```

---

## 🔄 PROCESO RECOMENDADO

### **Para cada página:**

1. **Copiar el archivo ES:**
   ```bash
   cp index.html index-ca.html
   cp contacto.html contacte-ca.html
   cp ayuda.html ajuda-ca.html
   cp gracias.html gracies-ca.html
   cp consejos.html consells-ca.html
   ```

2. **Hacer los cambios técnicos:**
   - Cambiar `lang="es"` a `lang="ca"`
   - Actualizar canonical URL
   - Actualizar og:locale a `ca_ES`
   - Actualizar og:url
   - Agregar hreflang tags

3. **Traducir contenido:**
   - Title, meta description, meta keywords
   - H1, H2, H3
   - Navegación
   - Contenido del body
   - Botones y CTAs
   - Formulario
   - Footer

4. **Actualizar enlaces:**
   - Cambiar enlaces internos a versiones CA
   - Actualizar WhatsApp con mensaje en catalán

5. **Probar localmente:**
   - Abrir en navegador
   - Verificar que todo funciona
   - Probar formulario

6. **Subir al servidor:**
   ```bash
   rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
     index-ca.html \
     u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
   ```

---

## 📊 CHECKLIST POR PÁGINA

### **index-ca.html:**
- [ ] lang="ca"
- [ ] Title traducido con keywords CA
- [ ] Meta description traducida
- [ ] Meta keywords en catalán
- [ ] og:locale = ca_ES
- [ ] Canonical = index-ca.html
- [ ] Hreflang tags
- [ ] H1 traducido
- [ ] Navegación traducida
- [ ] Hero section traducido
- [ ] Servicios traducidos
- [ ] Por qué elegirme traducido
- [ ] Sobre mí traducido
- [ ] Experiencia traducida
- [ ] Testimonios traducidos
- [ ] Te Ayudamos traducido
- [ ] FAQ traducido
- [ ] Formulario traducido
- [ ] Footer traducido
- [ ] WhatsApp mensaje en catalán
- [ ] Selector de idioma
- [ ] Enlaces internos a versiones CA

### **contacte-ca.html:**
- [ ] Todos los puntos anteriores adaptados
- [ ] Formulario con labels en catalán
- [ ] Placeholders en catalán

### **ajuda-ca.html:**
- [ ] Tarjetas principales traducidas
- [ ] Modales con contenido en catalán
- [ ] Sub-tarjetas traducidas

### **gracies-ca.html:**
- [ ] Mensaje de agradecimiento en catalán
- [ ] Enlaces a versiones CA

### **consells-ca.html:**
- [ ] Tarjetas traducidas
- [ ] Modales con contenido en catalán

---

## ⏰ TIEMPO ESTIMADO

- **index-ca.html:** 1.5 horas (página más compleja)
- **contacte-ca.html:** 30 minutos
- **ajuda-ca.html:** 1 hora (muchos modales)
- **gracies-ca.html:** 15 minutos
- **consells-ca.html:** 45 minutos
- **Agregar hreflang en páginas ES:** 30 minutos
- **Agregar selector de idioma:** 30 minutos
- **Probar y subir:** 30 minutos

**TOTAL:** ~5-6 horas

---

## 🛠️ HERRAMIENTAS ÚTILES

### **Diccionario de traducciones:**
- `traducciones_catalan.json` (ya creado)

### **Verificar traducciones:**
- **DeepL:** https://www.deepl.com/translator (mejor que Google Translate)
- **Softcatalà:** https://www.softcatala.org/traductor/

### **Verificar ortografía catalana:**
- Acentos: à, è, é, í, ò, ó, ú
- Apóstrofos: l', d', t', m', n', s'
- Cedilla: ç

---

## 📞 FORMSUBMIT.CO EN CATALÁN

### **Configuración del formulario (IGUAL que ES):**

```html
<form action="https://formsubmit.co/calvarado1873@gmail.com" method="POST">
    <input type="hidden" name="_subject" value="Nou missatge des de carmenalvarado.es - Versió Catalana">
    <input type="hidden" name="_captcha" value="true">
    <input type="hidden" name="_template" value="box">
    <input type="text" name="_honey" style="display:none">
    <input type="hidden" name="_next" value="https://carmenalvarado.es/gracies-ca.html">
</form>
```

**Cambios:**
- `_subject` en catalán para identificar
- `_next` apunta a `gracies-ca.html`

---

## 🎯 PRIORIDAD DE CREACIÓN

1. **index-ca.html** (ALTA - página principal)
2. **contacte-ca.html** (ALTA - conversión)
3. **gracies-ca.html** (ALTA - necesaria para formularios)
4. **ajuda-ca.html** (MEDIA)
5. **consells-ca.html** (MEDIA)

---

## 📤 COMANDOS PARA SUBIR (cuando estén listos)

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# Subir uno por uno
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" index-ca.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" contacte-ca.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" gracies-ca.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" ajuda-ca.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" consells-ca.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

## 🌐 URLS FINALES

- https://carmenalvarado.es/index-ca.html
- https://carmenalvarado.es/contacte-ca.html
- https://carmenalvarado.es/ajuda-ca.html
- https://carmenalvarado.es/gracies-ca.html
- https://carmenalvarado.es/consells-ca.html

---

## ✅ ESTADO ACTUAL DEL PROYECTO

### **Páginas en Castellano (COMPLETAS):**
- ✅ index.html - Optimizado SEO
- ✅ contacto.html - Optimizado SEO
- ✅ ayuda.html - Optimizado SEO
- ✅ consejos.html - Con tarjetas interactivas
- ✅ gracias.html - Funcional

### **Formularios:**
- ✅ FormSubmit.co activado
- ✅ Emails funcionando
- ✅ Campos optimizados

### **SEO:**
- ✅ Keywords castellano optimizadas
- ✅ Keywords "sociosanitario" implementadas
- ✅ Keywords catalán investigadas

### **Pendiente:**
- ⏳ Crear 5 páginas en catalán
- ⏳ Agregar selector de idioma
- ⏳ Agregar hreflang tags
- ⏳ Favicon

---

## 📁 ARCHIVOS DE REFERENCIA

- **Traducciones:** `traducciones_catalan.json`
- **Keywords CA:** `config/keywords_catalan.json`
- **Informe CA:** `config/INFORME_KEYWORDS_CATALAN.txt`

---

## 💡 RECOMENDACIÓN PARA PRÓXIMA SESIÓN

**Empezar directamente con la creación:**

1. Yo creo `index-ca.html` completo (1.5 horas)
2. Tú lo revisas y apruebas
3. Yo creo el resto de páginas (2 horas)
4. Agregamos selector de idioma (30 min)
5. Agregamos hreflang tags (30 min)
6. Subimos todo (15 min)
7. Verificamos (15 min)

**Total:** ~5 horas de trabajo enfocado

---

## 🎯 OBJETIVO FINAL

**Sitio web bilingüe completo (ES/CA) con:**
- ✅ SEO optimizado en ambos idiomas
- ✅ Keywords específicas para cada idioma
- ✅ Selector de idioma visible
- ✅ Hreflang tags correctos
- ✅ Formularios funcionando en ambos idiomas
- ✅ Mismo diseño y funcionalidad
- ✅ WhatsApp con mensajes en cada idioma

---

**Documento creado:** 13 de octubre de 2025  
**Estado:** ✅ Todo preparado para ejecutar  
**Próxima acción:** Crear páginas en catalán (próxima sesión)

