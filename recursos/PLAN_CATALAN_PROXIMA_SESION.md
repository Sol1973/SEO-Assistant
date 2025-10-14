# 🇨🇦 PLAN PARA CREAR PÁGINAS EN CATALÁN
**Próxima sesión**

---

## 📋 RESUMEN DE HOY

### ✅ **COMPLETADO:**
1. Documentación completa del proyecto
2. Investigación keywords castellano ("sociosanitario")
3. Implementación keywords en sitio (castellano)
4. Investigación keywords catalán
5. Archivos subidos al servidor

### ⏳ **PENDIENTE:**
1. Crear páginas en catalán (4-5 archivos)
2. Página consejos.html
3. Selector de idioma
4. Favicon

---

## 🎯 PRÓXIMA SESIÓN: CREAR PÁGINAS EN CATALÁN

### **Archivos a crear:**

1. **`index-ca.html`** (Página principal)
2. **`contacte-ca.html`** (Contacto - nota: "contacte" no "contacto")
3. **`ajuda-ca.html`** (Te Ayudamos - nota: "ajuda" no "ayuda")
4. **`gracies-ca.html`** (Gracias - nota: "gràcies")
5. **`consells-ca.html`** (Consejos - nota: "consells")

---

## 📝 TRADUCCIONES CLAVE

### **Meta Tags:**
```
ES: Cuidadora Personas Mayores Tarragona
CA: Cuidadora Persones Grans Tarragona

ES: Técnica Sociosanitaria Titulada
CA: Tècnica Sociosanitària Titulada

ES: Atención domiciliaria personalizada
CA: Atenció domiciliària personalitzada

ES: Disponibilidad inmediata
CA: Disponibilitat immediata
```

### **Navegación:**
```
Inicio → Inici
Servicios → Serveis
Sobre Mí → Sobre Mi
Te Ayudamos → T'Ajudem
Consejos → Consells
Contacto → Contacte
```

### **Secciones:**
```
¿Por qué elegirme? → Per què triar-me?
Experiencia → Experiència
Formación → Formació
Preguntas Frecuentes → Preguntes Freqüents
Testimonios → Testimonis
```

### **Servicios:**
```
Atención por Horas → Atenció per Hores
Media Jornada → Mitja Jornada
Jornada Completa → Jornada Completa
Personas Mayores → Persones Grans
Personas Dependientes → Persones Dependents
```

### **CTAs:**
```
Contacta Ahora → Contacta Ara
Llamar Ahora → Trucar Ara
Más Información → Més Informació
Enviar Mensaje → Enviar Missatge
```

---

## ⚙️ CAMBIOS TÉCNICOS NECESARIOS

### **1. Lang attribute:**
```html
<!-- ES -->
<html lang="es">

<!-- CA -->
<html lang="ca">
```

### **2. Hreflang tags (agregar en TODAS las páginas):**
```html
<!-- En páginas ES -->
<link rel="alternate" hreflang="es" href="https://carmenalvarado.es/index.html" />
<link rel="alternate" hreflang="ca" href="https://carmenalvarado.es/index-ca.html" />

<!-- En páginas CA -->
<link rel="alternate" hreflang="es" href="https://carmenalvarado.es/index.html" />
<link rel="alternate" hreflang="ca" href="https://carmenalvarado.es/index-ca.html" />
```

### **3. Canonical URL:**
```html
<!-- ES -->
<link rel="canonical" href="https://carmenalvarado.es/" />

<!-- CA -->
<link rel="canonical" href="https://carmenalvarado.es/index-ca.html" />
```

### **4. OG Locale:**
```html
<!-- ES -->
<meta property="og:locale" content="es_ES">

<!-- CA -->
<meta property="og:locale" content="ca_ES">
```

---

## 🎨 SELECTOR DE IDIOMA

### **Agregar en el header de TODAS las páginas:**

```html
<div class="language-selector" style="position: absolute; top: 10px; right: 20px;">
    <a href="index.html" style="color: #2c5f7c; font-weight: 500;">ES</a>
    <span style="color: #999;"> | </span>
    <a href="index-ca.html" style="color: #2c5f7c; font-weight: 500;">CA</a>
</div>
```

**Ubicación:** Dentro del `<header>`, antes o después del `<nav>`

---

## 📊 KEYWORDS EN CATALÁN (RECORDATORIO)

### **Prioridad ALTA:**
1. cuidadora persones grans tarragona (100-200 vol)
2. cuidadora gent gran tarragona (80-150 vol)
3. atenció domiciliària tarragona (60-120 vol)
4. cuidadora a domicili tarragona (50-100 vol)

### **Title Tag recomendado:**
```html
<title>Cuidadora Persones Grans Tarragona | Tècnica Sociosanitària | Carmen Alvarado</title>
```

### **Meta Description recomendada:**
```html
<meta name="description" content="Cuidadora professional i tècnica sociosanitària titulada a Tarragona. Atenció domiciliària personalitzada per a persones grans i dependents. Disponibilitat immediata. ☎️ 611 230 547">
```

---

## 🚀 ESTRATEGIA PARA PRÓXIMA SESIÓN

### **Opción 1: Crear archivos manualmente (RECOMENDADO)**
- Copiar index.html → index-ca.html
- Traducir sección por sección
- Verificar keywords
- Probar localmente
- Subir al servidor

**Tiempo estimado:** 2-3 horas

### **Opción 2: Usar herramienta de traducción + revisión**
- Usar DeepL o Google Translate para traducción inicial
- Revisar y ajustar keywords
- Verificar que suene natural
- Probar y subir

**Tiempo estimado:** 1-2 horas

---

## ✅ CHECKLIST PARA CADA PÁGINA EN CATALÁN

- [ ] Cambiar `lang="es"` a `lang="ca"`
- [ ] Traducir `<title>`
- [ ] Traducir `<meta name="description">`
- [ ] Traducir `<meta name="keywords">`
- [ ] Actualizar `og:locale` a `ca_ES`
- [ ] Actualizar canonical URL
- [ ] Agregar hreflang tags
- [ ] Traducir navegación
- [ ] Traducir H1, H2, H3
- [ ] Traducir contenido del body
- [ ] Traducir botones y CTAs
- [ ] Traducir formularios
- [ ] Traducir footer
- [ ] Agregar selector de idioma
- [ ] Verificar que los links funcionen
- [ ] Probar formulario
- [ ] Subir al servidor
- [ ] Verificar en navegador

---

## 📁 ESTRUCTURA FINAL

```
carmenalvarado.es/
├── index.html              (ES)
├── index-ca.html           (CA) ⏳
├── contacto.html           (ES)
├── contacte-ca.html        (CA) ⏳
├── ayuda.html              (ES)
├── ajuda-ca.html           (CA) ⏳
├── gracias.html            (ES)
├── gracies-ca.html         (CA) ⏳
├── consejos.html           (ES) ⏳
├── consells-ca.html        (CA) ⏳
├── css/
├── js/
└── images/
```

---

## 🎯 OBJETIVO

**Tener el sitio completamente bilingüe (ES/CA) con:**
- ✅ SEO optimizado en ambos idiomas
- ✅ Keywords específicas para cada idioma
- ✅ Selector de idioma visible
- ✅ Hreflang tags correctos
- ✅ Formularios funcionando en ambos idiomas

---

## ⏰ TIEMPO TOTAL ESTIMADO

- Crear 5 páginas en catalán: **2-3 horas**
- Agregar selector de idioma: **30 minutos**
- Agregar hreflang tags: **30 minutos**
- Probar y verificar: **30 minutos**
- Subir al servidor: **15 minutos**

**Total:** ~4 horas

---

## 📞 PARA LA PRÓXIMA SESIÓN

**Empezar directamente con:**
1. Crear `index-ca.html` (página más importante)
2. Probar que funciona
3. Crear el resto de páginas
4. Subir todas juntas
5. Verificar

**Sin demoras, sin investigación adicional. Todo ya está planificado.**

---

**Documento creado:** 13 de octubre de 2025  
**Estado:** ✅ Plan listo para ejecutar  
**Próxima acción:** Crear páginas en catalán

