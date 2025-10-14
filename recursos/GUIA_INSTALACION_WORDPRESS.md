# 🚀 GUÍA COMPLETA: SUBIR WEB CARMEN A WORDPRESS/HOSTINGER
**Proyecto:** Web Carmen Alvarado - Cuidadora Profesional  
**Hosting:** Hostinger  
**CMS:** WordPress  
**Fecha:** 12 de octubre de 2025

---

## 📋 ÍNDICE
1. [Requisitos Previos](#requisitos)
2. [Instalación WordPress en Hostinger](#instalacion)
3. [Configuración Inicial](#configuracion)
4. [Subir el Contenido HTML](#subir-contenido)
5. [Plugins Necesarios](#plugins)
6. [Configuración SEO](#seo)
7. [Google Analytics y Search Console](#analytics)
8. [Configuración Multiidioma (Futuro)](#multiidioma)
9. [Mantenimiento](#mantenimiento)

---

## 📦 REQUISITOS PREVIOS {#requisitos}

### **1. Hosting Hostinger**
- Plan mínimo: **Business** (recomendado para WordPress)
- Dominio: `carmenalvarado.es`
- SSL incluido (HTTPS)

### **2. Correos Necesarios**
- Correo profesional: `info@carmenalvarado.es`
- Respaldo: `calvarado1873@gmail.com` (ya existe)

### **3. Cuentas a Crear (Gratis)**
- Google Search Console
- Google Analytics
- Google My Business

---

## 🔧 INSTALACIÓN WORDPRESS EN HOSTINGER {#instalacion}

### **PASO 1: Acceder a Hostinger**
1. Ir a: https://www.hostinger.es
2. Login con tu cuenta
3. Panel de Control (hPanel)

### **PASO 2: Auto-instalador WordPress**
1. En hPanel → **Sitios Web**
2. Clic en **Auto Installer**
3. Seleccionar **WordPress**
4. Configurar:
   ```
   Dominio: carmenalvarado.es
   Título del sitio: Carmen Alvarado - Cuidadora Profesional Tarragona
   Usuario admin: carmen_admin
   Contraseña: [Crear una FUERTE]
   Email: calvarado1873@gmail.com
   Idioma: Español
   ```
5. Clic **Instalar**
6. Esperar 2-5 minutos

### **PASO 3: Acceder a WordPress**
```
URL Admin: https://carmenalvarado.es/wp-admin
Usuario: carmen_admin
Contraseña: [La que creaste]
```

---

## ⚙️ CONFIGURACIÓN INICIAL {#configuracion}

### **1. Ajustes Generales**
```
WordPress Admin → Ajustes → Generales

Título: Carmen Alvarado - Cuidadora Profesional en Tarragona
Descripción: Atención profesional a domicilio para personas mayores en Tarragona y Reus
Idioma: Español
Zona horaria: Madrid
```

### **2. Enlaces Permanentes (IMPORTANTE para SEO)**
```
Ajustes → Enlaces Permanentes
Seleccionar: Nombre de la entrada
Ejemplo: /cuidadora-personas-mayores-tarragona
```

### **3. Ajustes de Lectura**
```
Ajustes → Lectura
Página de inicio: Página estática
Seleccionar: Inicio (la crearás después)
```

---

## 📄 SUBIR EL CONTENIDO HTML {#subir-contenido}

Tienes **2 OPCIONES:**

### **OPCIÓN A: Theme Personalizado (Recomendado si sabes HTML)**

1. **Instalar tema Blank/Starter**
   - Tema recomendado: **Astra** (gratis, ligero, personalizable)
   - Apariencia → Temas → Añadir Nuevo → Buscar "Astra"
   
2. **Usar plugin para HTML personalizado**
   - Plugin: **Insert Headers and Footers**
   - Plugin: **Custom CSS/JS**
   
3. **Crear páginas personalizadas**
   - Páginas → Añadir nueva
   - Modo HTML (no visual)
   - Copiar/pegar tu código HTML

### **OPCIÓN B: Constructor Visual (MÁS FÁCIL - RECOMENDADO)**

1. **Instalar Elementor (Gratis)**
   ```
   Plugins → Añadir nuevo → Buscar "Elementor"
   Instalar y Activar
   ```

2. **Convertir HTML a bloques Elementor**
   - Crear página nueva
   - Editar con Elementor
   - Recrear secciones visualmente

**💡 RECOMENDACIÓN:** Usa **Elementor** si no dominas código. Es visual y fácil.

---

## 🔌 PLUGINS NECESARIOS {#plugins}

### **Plugins ESENCIALES (Instalar ya):**

```
Plugins → Añadir Nuevo → Buscar cada uno:
```

#### **1. Yoast SEO** (Gratis) ⭐
- SEO on-page
- Meta descriptions
- Sitemaps automáticos
- Análisis de keywords

#### **2. WPForms** (Gratis)
- Formularios de contacto
- Reemplazo del formulario HTML
- Anti-spam incluido

#### **3. Really Simple SSL** (Gratis)
- Fuerza HTTPS
- Seguridad básica

#### **4. WP Super Cache** (Gratis)
- Velocidad de carga
- Cache de páginas

#### **5. Wordfence Security** (Gratis)
- Firewall
- Protección contra hackers

### **Plugins RECOMENDADOS (Opcionales pero útiles):**

#### **6. TranslatePress** (Gratis versión básica)
- Para agregar catalán después
- Traducción visual
- SEO multiidioma

#### **7. MonsterInsights** (Gratis)
- Google Analytics integrado
- Dashboard en WordPress

#### **8. Schema Pro** (Pago ~50€/año)
- Schema markup automático
- Mejor SEO local
- **Alternativa gratis:** WP Schema Pro Lite

---

## 🔍 CONFIGURACIÓN SEO {#seo}

### **1. Configurar Yoast SEO**

```
SEO → General → Características

✓ Análisis SEO
✓ Análisis de legibilidad
✓ Mapas del sitio XML
✓ Páginas de configuración avanzadas
```

### **2. Meta Datos de Páginas**

**Página Principal:**
```
Título SEO: Cuidadora Personas Mayores Tarragona | Carmen Alvarado
Meta Description: Cuidadora profesional de personas mayores en Tarragona. 
Atención a domicilio personalizada, titulada sociosanitaria. Disponibilidad 
inmediata. ☎️ 611 230 547
Frase clave: cuidadora personas mayores tarragona
```

**Página Te Ayudamos:**
```
Título SEO: Consejos para Familias que Cuidan Personas Mayores | Tarragona
Meta Description: ¿Preocupado por tu familiar mayor? Te ayudamos con 
consejos prácticos. Resuelve miedos, culpa y dudas sobre cuidado de mayores.
Frase clave: consejos cuidar personas mayores
```

### **3. Crear Sitemap.xml Automático**

Yoast lo hace automático en:
```
https://carmenalvarado.es/sitemap_index.xml
```

---

## 📊 GOOGLE ANALYTICS Y SEARCH CONSOLE {#analytics}

### **1. Google Analytics 4**

**Setup:**
1. Ir a: https://analytics.google.com
2. Crear cuenta → Añadir propiedad
3. Nombre: Carmen Alvarado - Cuidadora Tarragona
4. Copiar ID de medición: `G-XXXXXXXXXX`

**Instalar en WordPress:**
- Con MonsterInsights: Pegar ID en plugin
- Sin plugin: `Apariencia → Editor de temas → header.php`
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

### **2. Google Search Console**

**Setup:**
1. Ir a: https://search.google.com/search-console
2. Añadir propiedad: `https://carmenalvarado.es`
3. Verificar propiedad:
   - Método recomendado: **Google Analytics** (si ya está instalado)
   - O subir archivo HTML de verificación
4. Enviar sitemap: `https://carmenalvarado.es/sitemap_index.xml`

### **3. Google My Business** (CRUCIAL para SEO local)

**Setup:**
1. Ir a: https://business.google.com
2. Crear perfil de empresa:
   ```
   Nombre: Carmen Alvarado - Cuidadora Profesional
   Categoría: Servicio de cuidado a domicilio
   Ubicación: Tarragona
   Teléfono: 611 230 547
   Sitio web: https://carmenalvarado.es
   Horario: Lunes-Domingo 8:00-21:00
   ```
3. Verificar (postal o teléfono)
4. Añadir fotos profesionales
5. **PEDIR RESEÑAS** a clientes satisfechos

---

## 🌐 MULTIIDIOMA (CATALÁN) - FUTURO {#multiidioma}

### **Cuando Estés Lista para Catalán:**

**Plugin: TranslatePress (Gratis)**

**Instalación:**
1. `Plugins → Añadir nuevo → TranslatePress`
2. `Ajustes → TranslatePress`
3. Idiomas:
   - Predeterminado: Español
   - Agregar: Catalán
4. **Traducir visualmente:**
   - Ir a cada página
   - Clic en "Traducir página" (barra superior)
   - Cambias textos directamente viendo el diseño

**URLs resultantes:**
```
Español: https://carmenalvarado.es/
Catalán: https://carmenalvarado.es/ca/
```

---

## 📂 ESTRUCTURA DE PÁGINAS EN WORDPRESS

```
PÁGINAS A CREAR:

1. Inicio (index.html)
2. Servicios
   - Atención por Horas
   - Media Jornada
   - Jornada Completa
3. Sobre Mí
4. Te Ayudamos (ayuda.html)
5. Contacto
6. Blog (opcional después)

PÁGINAS LEGALES (Obligatorias):
7. Aviso Legal
8. Política de Privacidad
9. Política de Cookies
```

---

## 📝 CÓMO MIGRAR TU HTML A WORDPRESS

### **MÉTODO 1: Copiar/Pegar en Bloques HTML**

**Para cada página:**

1. `Páginas → Añadir nueva`
2. Nombre: "Inicio" (por ejemplo)
3. Clic en **+ (Añadir bloque)**
4. Buscar: **HTML Personalizado**
5. Pegar el contenido HTML de tu archivo
6. Repetir para cada sección
7. **Publicar**

**Pros:** Rápido, mantienes diseño exacto  
**Contras:** Difícil de editar después

### **MÉTODO 2: Usar Elementor (Recomendado)**

**Para cada página:**

1. `Páginas → Añadir nueva`
2. Clic: **Editar con Elementor**
3. **Recrear secciones** arrastrando widgets:
   - Hero: Widget Título + Texto + Botón
   - Servicios: Widget Tarjetas
   - Formulario: Widget WPForms
4. **Copiar textos** de tu HTML
5. **Configurar colores:**
   - Primary: #2E7D9C
   - Secondary: #E89B5F
6. **Publicar**

**Pros:** Fácil editar después, visual  
**Contras:** Toma más tiempo inicial

---

## 🎨 CONFIGURACIÓN DE COLORES Y DISEÑO

### **En WordPress (con Astra + Elementor):**

```
Apariencia → Personalizar → Colores Globales

Color Primario: #2E7D9C (Azul confianza)
Color Acento: #E89B5F (Naranja cálido)
Texto: #2C3E50
Fondo: #FFFFFF

Tipografía:
Títulos: Poppins
Cuerpo: Open Sans
```

---

## 📧 CONFIGURAR CORREO ELECTRÓNICO

### **Formulario de Contacto debe enviar a tu email:**

**Opción A: SMTP Nativo Hostinger**
```
Plugin: WP Mail SMTP
Configuración:
- Servidor: smtp.hostinger.com
- Puerto: 587
- Usuario: info@carmenalvarado.es
- Contraseña: [La del correo]
```

**Opción B: Gmail SMTP (Más fácil)**
```
Plugin: WP Mail SMTP
Mailer: Gmail
Autorizar cuenta de Gmail
```

---

## 🔒 PÁGINAS LEGALES (OBLIGATORIAS)

### **Generadores Automáticos:**

**1. Política de Privacidad**
- Generador: https://politicadeprivacidadplantilla.com
- Datos a incluir:
  - Responsable: Carmen Alvarado
  - Email: calvarado1873@gmail.com
  - Finalidad: Gestionar consultas
  - Datos recopilados: Nombre, teléfono, email

**2. Aviso Legal**
- Generador: https://www.avilegal.com
- Incluir:
  - Titular: Carmen Alvarado
  - NIF/NIE (cuando seas autónoma)
  - Domicilio (puede ser apartado postal)

**3. Política de Cookies**
- Plugin: **Cookie Notice & Compliance** (gratis)
- Auto-genera el texto
- Banner de cookies automático

---

## 🚀 CHECKLIST ANTES DE LANZAR

### **Técnico:**
- [ ] SSL activado (HTTPS)
- [ ] Enlaces permanentes configurados
- [ ] Plugins esenciales instalados
- [ ] Formulario de contacto funcionando
- [ ] Google Analytics instalado
- [ ] Sitemap enviado a Search Console
- [ ] Velocidad de carga < 3 segundos
- [ ] Responsive (test en móvil)

### **Contenido:**
- [ ] Todas las páginas creadas
- [ ] Información verificada y correcta
- [ ] Imágenes optimizadas (<200KB cada una)
- [ ] Teléfono y email correctos
- [ ] CTAs claros en cada página

### **Legal:**
- [ ] Aviso Legal publicado
- [ ] Política de Privacidad publicada
- [ ] Política de Cookies publicada
- [ ] Banner de cookies activo

### **SEO:**
- [ ] Yoast SEO configurado
- [ ] Meta títulos y descriptions en cada página
- [ ] Keywords principales identificadas
- [ ] Google My Business creado
- [ ] Sitemap enviado

---

## 📁 ARCHIVOS A SUBIR A WORDPRESS

### **Método FTP (Archivos estáticos):**

**Si quieres subir tus archivos HTML directamente:**

1. **Acceder por FTP a Hostinger:**
   ```
   Host: ftp.carmenalvarado.es
   Usuario: [Tu usuario Hostinger]
   Contraseña: [Tu contraseña]
   Puerto: 21
   ```

2. **Programa FTP:** FileZilla (gratis)

3. **Subir archivos a:**
   ```
   /public_html/
   ├── index.html
   ├── ayuda.html
   ├── css/
   │   └── styles.css
   ├── js/
   │   └── main.js
   └── images/
   ```

**Pero SI USAS WORDPRESS, NO subas por FTP.** WordPress gestiona todo internamente.

---

## 🖼️ IMÁGENES NECESARIAS

### **Imágenes Profesionales a Conseguir:**

1. **carmen-professional.jpg**
   - Foto profesional de Carmen
   - Con uniforme o ropa formal
   - Sonriendo, transmitiendo confianza
   - Fondo neutro o en contexto laboral
   - Tamaño: 800x800px mínimo

2. **hero-background.jpg**
   - Imagen para fondo del hero
   - Persona mayor sonriendo con cuidadora
   - Evitar fotos stock genéricas
   - Tamaño: 1920x1080px

3. **Imágenes Blog (3 mínimo):**
   - senales-ayuda-mayores.jpg
   - precio-cuidadora-tarragona.jpg
   - elegir-cuidadora-confianza.jpg

**Optimización antes de subir:**
- Herramienta: TinyPNG.com (gratis)
- Formato: WebP (mejor) o JPG
- Peso máximo: 200KB cada imagen
- Alt text siempre con keywords

---

## 🎯 CONFIGURACIÓN GOOGLE MY BUSINESS

### **Pasos Detallados:**

1. **Crear Perfil:**
   ```
   Nombre: Carmen Alvarado - Cuidadora Profesional
   Categorías:
   - Servicio de cuidado a domicilio (principal)
   - Cuidador de personas mayores
   - Servicio de atención domiciliaria
   
   Ubicación: Tarragona
   Área de servicio: Tarragona, Reus
   ```

2. **Información Completa:**
   ```
   Teléfono: 611 230 547
   Sitio web: https://carmenalvarado.es
   
   Descripción (750 caracteres):
   "Soy Carmen Alvarado, cuidadora profesional de personas mayores 
   en Tarragona. Técnica Sociosanitaria titulada en 2024, ofrezco 
   atención personalizada a domicilio en Tarragona y Reus. Me comunico 
   en castellano y catalán. Servicios: atención por horas, media jornada, 
   jornada completa, post-operatorio, movilidad reducida. Trato directo 
   sin intermediarios. Primera visita gratuita. Disponibilidad inmediata."
   
   Horario:
   Lunes-Domingo: 8:00-21:00
   (Marcar "Atención telefónica")
   ```

3. **Añadir Fotos:**
   - Foto de perfil: Carmen profesional
   - Portada: Carmen con persona mayor
   - Galería: 5-10 fotos (con permisos)

4. **Atributos:**
   - ✓ Citas online disponibles
   - ✓ Identificación como mujer
   - ✓ De propietario latino
   - ✓ Se habla catalán

5. **PEDIR RESEÑAS:**
   - Link directo: https://g.page/r/[TU-ID]/review
   - Envía a clientes satisfechos
   - Responde TODAS las reseñas

---

## 📱 CONFIGURACIÓN WHATSAPP BUSINESS

### **WhatsApp Business (Gratis):**

1. Descargar app: WhatsApp Business
2. Número: 611 230 547
3. **Perfil:**
   ```
   Nombre: Carmen Alvarado - Cuidadora
   Descripción: Cuidadora profesional de personas mayores en Tarragona
   Categoría: Servicio de salud
   Sitio web: https://carmenalvarado.es
   Email: calvarado1873@gmail.com
   Dirección: Tarragona
   ```

4. **Mensajes Automáticos:**
   
   **Mensaje de Bienvenida:**
   ```
   ¡Hola! Soy Carmen 😊
   
   Gracias por contactarme. Te responderé lo antes posible, 
   normalmente en menos de 2 horas.
   
   Si es urgente, llámame directamente al 611 230 547.
   
   ¿En qué puedo ayudarte con tu familiar?
   ```
   
   **Mensaje de Ausencia:**
   ```
   Gracias por tu mensaje. Ahora no puedo responder pero te 
   contestaré en cuanto vea tu mensaje.
   
   Si es urgente, déjame un mensaje de voz y te llamo enseguida.
   ```

5. **Catálogo de Servicios:**
   - Añadir servicios con precios orientativos
   - Fotos de cada servicio

---

## 🎯 ESTRATEGIA PRIMER MES

### **Semana 1: Configuración**
- [ ] WordPress instalado
- [ ] Plugins configurados
- [ ] Páginas principales creadas
- [ ] Google Analytics + Search Console

### **Semana 2: Contenido**
- [ ] Todas las secciones completas
- [ ] Imágenes profesionales
- [ ] Formularios funcionando
- [ ] SEO on-page optimizado

### **Semana 3: Google My Business**
- [ ] Perfil creado y verificado
- [ ] Fotos subidas
- [ ] Primeras 3 reseñas conseguidas
- [ ] Publicaciones semanales

### **Semana 4: Lanzamiento**
- [ ] Última revisión completa
- [ ] Test en diferentes dispositivos
- [ ] Compartir en redes (si tienes)
- [ ] Avisar a contactos cercanos

---

## 💰 PRESUPUESTO ESTIMADO

### **Costes Iniciales:**
```
Dominio (.es): 10-15 €/año (Hostinger)
Hosting Business: 3-6 €/mes (oferta primer año)
SSL: GRATIS (incluido Hostinger)
WordPress: GRATIS
Plugins básicos: GRATIS
TranslatePress: GRATIS (versión básica)
Google Analytics: GRATIS
Google Search Console: GRATIS
Google My Business: GRATIS

TOTAL PRIMER AÑO: ~50-100 €
MENSUAL DESPUÉS: ~6-10 €/mes
```

### **Opcional (Recomendado):**
```
Fotos profesionales: 100-200 € (sesión)
Schema Pro (SEO avanzado): 50 €/año
Elementor Pro: 49 €/año (si necesitas más features)
```

---

## 📞 SOPORTE SI NECESITAS AYUDA

### **Hostinger:**
- Chat 24/7 en español
- Tutoriales: https://support.hostinger.com/es

### **WordPress:**
- Documentación: https://es.wordpress.org/support/
- Foros: https://es.forums.wordpress.org/

### **Vídeos Recomendados (YouTube):**
- "Cómo instalar WordPress en Hostinger"
- "Elementor tutorial español"
- "Yoast SEO configuración completa"

---

## ✅ CHECKLIST FINAL PRE-LANZAMIENTO

### **Funcionalidad:**
- [ ] Todos los enlaces funcionan
- [ ] Formulario envía emails correctamente
- [ ] Botones de teléfono/WhatsApp funcionan
- [ ] No hay errores 404
- [ ] Menú navegable en móvil

### **SEO:**
- [ ] Todas las páginas tienen título SEO único
- [ ] Todas tienen meta description
- [ ] Imágenes con alt text
- [ ] URLs amigables
- [ ] Sitemap generado

### **Velocidad:**
- [ ] Test en PageSpeed Insights > 80/100
- [ ] Test en GTmetrix
- [ ] Cache activado
- [ ] Imágenes optimizadas

### **Legal:**
- [ ] Aviso Legal visible
- [ ] Política Privacidad visible
- [ ] Banner cookies funcionando
- [ ] Enlaces en footer

### **Conversión:**
- [ ] Teléfono visible en todas las páginas
- [ ] WhatsApp flotante funcionando
- [ ] CTAs claros
- [ ] Formulario simple (max 5 campos)

---

## 🎓 PRÓXIMOS PASOS DESPUÉS DEL LANZAMIENTO

### **Mes 1-2:**
1. Monitorizar Google Analytics
2. Revisar Search Console (errores, indexación)
3. Conseguir primeras 5-10 reseñas Google
4. Publicar primer artículo blog (si decides hacerlo)

### **Mes 3-6:**
1. Analizar keywords que funcionan
2. Optimizar páginas con más tráfico
3. Expandir contenido Te Ayudamos
4. Considerar Google Ads

---

**Documento creado:** 12 de octubre de 2025  
**Última actualización:** 12 de octubre de 2025  
**Siguiente paso:** Instalación WordPress en Hostinger

