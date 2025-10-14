# 🚀 GUÍA RÁPIDA: INSTALACIÓN MAÑANA (Cuando DNS Esté Listo)
**Dominio:** carmenalvarado.es  
**Servidor:** Hostinger  
**Fecha preparación:** 12 de octubre de 2025  
**Ejecución:** 13 de octubre de 2025 (cuando DNS esté propagado)

---

## ⏰ VERIFICAR DNS PROPAGADO (PRIMER PASO)

### **Antes de hacer NADA, verifica que el DNS esté listo:**

```bash
# En tu terminal:
ping carmenalvarado.es
```

**Debería responder con la IP:** `82.29.87.172`

**Si no responde o da otra IP:** Espera unas horas más.

---

## 📋 CHECKLIST COMPLETO (Orden de Ejecución)

### **PASO 1: Instalar WordPress (5 minutos)**
- [ ] Ir a hPanel Hostinger
- [ ] Auto-instalador WordPress
- [ ] Configurar dominio carmenalvarado.es
- [ ] Crear usuario admin
- [ ] Guardar credenciales

### **PASO 2: Configuración Inicial WordPress (10 minutos)**
- [ ] Login en WordPress
- [ ] Configurar enlaces permanentes
- [ ] Instalar tema Astra
- [ ] Instalar plugins esenciales (5)

### **PASO 3: Subir Contenido (15 minutos)**
- [ ] Crear página "Inicio"
- [ ] Crear página "Te Ayudamos"
- [ ] Subir CSS y JS
- [ ] Configurar menú

### **PASO 4: Configuración SEO (10 minutos)**
- [ ] Configurar Yoast SEO
- [ ] Subir sitemap.xml
- [ ] Verificar Google Search Console

### **PASO 5: Pruebas Finales (10 minutos)**
- [ ] Test todos los enlaces
- [ ] Test formulario contacto
- [ ] Test en móvil
- [ ] Velocidad de carga

**TIEMPO TOTAL ESTIMADO: 50 minutos**

---

## 🔧 PASO 1: INSTALAR WORDPRESS EN HOSTINGER

### **Por Panel Web (MÁS FÁCIL - Recomendado):**

1. **Acceder a Hostinger:**
   ```
   URL: https://hpanel.hostinger.com
   Usuario: [Tu email Hostinger]
   Contraseña: [Tu contraseña]
   ```

2. **Auto-instalador WordPress:**
   - En el panel, busca tu dominio: **carmenalvarado.es**
   - Clic en **"Sitio Web"** o **"Website"**
   - Botón: **"Instalar WordPress"** o **"Auto Installer"**

3. **Configuración:**
   ```
   Dominio: carmenalvarado.es
   Directorio: / (raíz, dejar en blanco)
   
   Título: Carmen Alvarado - Cuidadora Profesional Tarragona
   Descripción: Atención profesional a domicilio para personas mayores
   
   Usuario admin: carmen_admin
   Contraseña: [CREAR UNA FUERTE]
   Email: calvarado1873@gmail.com
   
   Idioma: Español (es_ES)
   ```

4. **Clic en "Instalar"** y esperar 2-5 minutos

5. **Guardar credenciales:**
   ```
   URL Admin: https://carmenalvarado.es/wp-admin
   Usuario: carmen_admin
   Contraseña: [La que creaste]
   ```

---

## 🔌 PASO 2: INSTALAR PLUGINS ESENCIALES

### **Login en WordPress:**
```
URL: https://carmenalvarado.es/wp-admin
```

### **Plugins a Instalar (en orden):**

1. **Yoast SEO**
   ```
   Plugins → Añadir nuevo → Buscar "Yoast SEO"
   Instalar y Activar
   ```

2. **Elementor** (Constructor visual)
   ```
   Plugins → Añadir nuevo → Buscar "Elementor"
   Instalar y Activar
   ```

3. **WPForms Lite**
   ```
   Plugins → Añadir nuevo → Buscar "WPForms"
   Instalar y Activar
   ```

4. **Really Simple SSL**
   ```
   Plugins → Añadir nuevo → Buscar "Really Simple SSL"
   Instalar y Activar (forzará HTTPS)
   ```

5. **WP Super Cache**
   ```
   Plugins → Añadir nuevo → Buscar "WP Super Cache"
   Instalar y Activar
   ```

---

## 🎨 PASO 3: INSTALAR Y CONFIGURAR TEMA

### **Tema Recomendado: Astra (Gratis)**

1. **Instalar:**
   ```
   Apariencia → Temas → Añadir nuevo
   Buscar "Astra"
   Instalar y Activar
   ```

2. **Configurar Colores:**
   ```
   Apariencia → Personalizar → Colores Globales
   
   Paleta:
   - Color Primario: #2E7D9C
   - Color Acento: #E89B5F
   - Texto: #2C3E50
   - Fondo: #FFFFFF
   ```

3. **Configurar Tipografía:**
   ```
   Apariencia → Personalizar → Tipografía
   
   - Títulos: Poppins
   - Cuerpo: Open Sans
   ```

---

## 📄 PASO 4: SUBIR TU CONTENIDO HTML

### **MÉTODO 1: Por FTP (Archivos estáticos - Rápido)**

Si quieres usar tus archivos HTML exactos:

1. **Acceder por FTP:**
   ```
   Programa: FileZilla (descarga gratis)
   Host: ftp.carmenalvarado.es (o 82.29.87.172)
   Usuario: u375945539
   Puerto: 21
   ```

2. **Subir archivos a:** `/public_html/`
   ```
   Desde tu Mac: /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen/
   
   Subir:
   - index.html
   - ayuda.html
   - carpeta css/
   - carpeta js/
   - carpeta images/
   - sitemap.xml
   - robots.txt
   ```

3. **Tu web estará en:**
   ```
   https://carmenalvarado.es/index.html
   https://carmenalvarado.es/ayuda.html
   ```

### **MÉTODO 2: Usar WordPress + Elementor (Más profesional)**

1. **Crear Página Inicio:**
   ```
   Páginas → Añadir nueva
   Título: Inicio
   Editar con Elementor
   ```

2. **Copiar secciones de tu HTML:**
   - Hero → Widget Título + Texto + Botón
   - Servicios → Widget Tarjetas/Iconos
   - Etc.

3. **Configurar como página de inicio:**
   ```
   Ajustes → Lectura
   "Página de inicio muestra" → Una página estática
   Página de inicio: Inicio
   ```

---

## 🔍 PASO 5: CONFIGURAR SEO

### **Yoast SEO:**

1. **Configuración Básica:**
   ```
   SEO → General → Configuración
   Completar asistente de configuración
   
   Tipo de sitio: Empresa local
   Nombre: Carmen Alvarado
   ```

2. **Página Inicio:**
   ```
   Editar página "Inicio"
   Scroll abajo → Yoast SEO
   
   Título SEO: Cuidadora Personas Mayores Tarragona | Carmen Alvarado
   Meta description: Cuidadora profesional de personas mayores en Tarragona. 
   Atención a domicilio personalizada, titulada sociosanitaria. 
   Disponibilidad inmediata. ☎️ 611 230 547
   
   Frase clave: cuidadora personas mayores tarragona
   ```

3. **Sitemap:**
   ```
   SEO → General → Características
   ✓ Mapas del sitio XML (activar)
   
   Sitemap estará en:
   https://carmenalvarado.es/sitemap_index.xml
   ```

---

## 📊 PASO 6: GOOGLE SEARCH CONSOLE

### **Verificar Propiedad:**

1. **Ir a:** https://search.google.com/search-console

2. **Añadir propiedad:**
   ```
   Tipo: Prefijo de URL
   URL: https://carmenalvarado.es
   ```

3. **Verificar (Método recomendado):**
   - Elegir: "Etiqueta HTML"
   - Copiar el código de verificación
   - En WordPress:
     ```
     Yoast SEO → General → Herramientas para webmasters
     Pegar código de Google
     ```
   - Volver a Search Console → Verificar

4. **Enviar Sitemap:**
   ```
   Search Console → Sitemaps → Añadir sitemap
   URL: sitemap_index.xml
   Enviar
   ```

---

## 📧 PASO 7: CONFIGURAR FORMULARIO CONTACTO

### **Con WPForms:**

1. **Crear formulario:**
   ```
   WPForms → Añadir nuevo
   Nombre: Formulario Contacto Carmen
   Plantilla: Formulario Simple de Contacto
   ```

2. **Campos necesarios:**
   - Nombre *
   - Teléfono *
   - Email
   - Ciudad (Tarragona/Reus) *
   - ¿Cuándo necesitas servicio? * (dropdown)
   - Mensaje *
   - Checkbox privacidad

3. **Configurar notificaciones:**
   ```
   Ajustes → Notificaciones
   Enviar a: calvarado1873@gmail.com
   Asunto: Nueva Consulta - Web Carmen
   ```

4. **Insertar en página:**
   ```
   Editar página "Inicio"
   Donde está el formulario → Widget WPForms
   Seleccionar: Formulario Contacto Carmen
   ```

---

## 🌐 PASO 8: GOOGLE MY BUSINESS (CRUCIAL)

### **Crear Perfil:**

1. **Ir a:** https://business.google.com

2. **Crear perfil:**
   ```
   Nombre: Carmen Alvarado - Cuidadora Profesional
   
   Categoría principal: Servicio de cuidado a domicilio
   Categorías secundarias:
   - Cuidador de personas mayores
   - Servicio de atención domiciliaria
   
   Ubicación: Tarragona
   ¿Entregas/visitas a clientes?: SÍ
   Áreas de servicio: Tarragona, Reus
   
   Teléfono: 611 230 547
   Sitio web: https://carmenalvarado.es
   
   Descripción:
   "Soy Carmen Alvarado, cuidadora profesional de personas mayores en 
   Tarragona. Técnica Sociosanitaria titulada, ofrezco atención 
   personalizada a domicilio en Tarragona y Reus. Me comunico en 
   castellano y catalán básico. Servicios: atención por horas, media 
   jornada, jornada completa. Trato directo sin intermediarios. 
   Primera visita gratuita. Disponibilidad inmediata."
   
   Horario:
   Lunes-Domingo: 8:00-21:00
   ```

3. **Verificación:**
   - Postal (tarda ~5 días) o
   - Teléfono (inmediato)

4. **Añadir fotos:**
   - Foto de perfil: Carmen
   - Portada: Profesional
   - Mínimo 5 fotos

---

## ✅ CHECKLIST ANTES DE LANZAR

### **Técnico:**
- [ ] DNS propagado (verificar con ping)
- [ ] WordPress instalado
- [ ] Plugins activados
- [ ] SSL activado (https://)
- [ ] Enlaces permanentes configurados

### **Contenido:**
- [ ] Página Inicio publicada
- [ ] Página Te Ayudamos publicada
- [ ] Formulario funcionando (enviar test)
- [ ] Teléfono correcto en todas partes
- [ ] Email correcto

### **SEO:**
- [ ] Yoast SEO configurado
- [ ] Meta títulos y descriptions
- [ ] Sitemap enviado a Search Console
- [ ] Google My Business creado

### **Pruebas:**
- [ ] Abrir web en Chrome
- [ ] Abrir en Safari
- [ ] Abrir en móvil (iPhone/Android)
- [ ] Todos los botones funcionan
- [ ] Modal "Te Ayudamos" abre y cierra
- [ ] WhatsApp flotante funciona

---

## 📦 ARCHIVOS PREPARADOS PARA SUBIR

Todos están en:
```
/Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen/
```

**Archivos principales:**
- ✅ index.html (938 líneas)
- ✅ ayuda.html (2,461 líneas)
- ✅ css/styles.css (29KB)
- ✅ js/main.js (14KB)
- ✅ sitemap.xml (limpio, solo 2 URLs)
- ✅ robots.txt
- ✅ .htaccess

**Cuando subas por FTP:**
Arrastra estas carpetas completas a `/public_html/`:
- css/
- js/
- images/
- index.html
- ayuda.html
- sitemap.xml
- robots.txt

---

## 🎯 OPCIONES PARA MAÑANA

### **OPCIÓN A: Rápida (HTML Directo - 15 minutos)**
1. Instalar WordPress
2. Subir archivos HTML por FTP
3. Configurar DNS apuntando a archivos
4. ¡Listo!

**Pros:** Rápido, diseño exacto  
**Contras:** Difícil actualizar después

### **OPCIÓN B: Profesional (WordPress + Elementor - 1 hora)**
1. Instalar WordPress
2. Instalar Elementor
3. Recrear páginas visualmente
4. Copiar textos
5. Configurar SEO

**Pros:** Fácil actualizar, muy profesional  
**Contras:** Toma más tiempo inicial

### **OPCIÓN C: Híbrida (Recomendado - 30 minutos)**
1. Instalar WordPress
2. Plugin "Insert HTML Snippet"
3. Crear páginas en WordPress
4. Pegar HTML en bloques
5. Mantener diseño + fácil administrar

---

## 📞 ORDEN DE PRIORIDAD MAÑANA

### **MÍNIMO VIABLE (Lanzar rápido):**
1. WordPress instalado
2. Página Inicio visible
3. Formulario funcionando
4. SSL activado

**Con esto YA puedes lanzar y recibir contactos.**

### **Ideal (Si tienes tiempo):**
5. Página Te Ayudamos
6. Google My Business
7. Search Console
8. Yoast SEO configurado

### **Perfecto (Completar en días siguientes):**
9. Google Analytics
10. Fotos profesionales
11. Testimonios reales
12. Optimizaciones adicionales

---

## 💡 COMANDOS ÚTILES PARA MAÑANA

### **Verificar DNS:**
```bash
# En tu terminal Mac:
ping carmenalvarado.es
nslookup carmenalvarado.es
```

### **Conectar por SSH (si necesitas):**
```bash
ssh -i /Users/micky/Documents/Proyectos_IA/CV_Carmen/ssh/manus_reviewer_key -p 65002 u375945539@82.29.87.172
```

### **Ver dominios en el servidor:**
```bash
ls -la ~/domains/
cd ~/domains/carmenalvarado.es/public_html/
```

---

## 📱 DESPUÉS DEL LANZAMIENTO

### **Día 1 (Mañana):**
- [ ] Compartir web con amigos cercanos
- [ ] Pedir feedback
- [ ] Hacer ajustes si necesario

### **Semana 1:**
- [ ] Conseguir primeras fotos profesionales
- [ ] Añadir a Google My Business
- [ ] Testear todo exhaustivamente

### **Semana 2:**
- [ ] Primera reseña Google (pedir a conocidos)
- [ ] Optimizar según feedback
- [ ] Verificar posiciones en Google

---

## 🆘 SI ALGO SALE MAL

### **WordPress no se instala:**
- Chat Hostinger 24/7: https://www.hostinger.es/contacto
- Soporte rápido en español

### **DNS no propaga:**
- Esperar 48h más
- Verificar en panel Hostinger que DNS estén bien

### **Formulario no envía emails:**
- Plugin WP Mail SMTP
- Configurar con Gmail (más fácil)

---

## 📋 NOTA IMPORTANTE

**Todo el contenido ya está listo y perfecto:**
- ✅ Información verificada y correcta
- ✅ SEO optimizado
- ✅ 25 sub-temas en "Te Ayudamos"
- ✅ Diseño profesional y responsive
- ✅ Pain points bien trabajados
- ✅ CTAs estratégicos
- ✅ Sin mencionar competidores
- ✅ Tarifas del mercado investigadas
- ✅ Keywords analizadas

**Solo falta subirlo. Mañana será rápido.** 🚀

---

## ⏰ HORA ESTIMADA MAÑANA

**Mejor hora para hacerlo:** 
- **Mañana:** Verifica DNS esté propagado
- **Instalar:** Cualquier hora del día (no afecta)
- **Total:** 30-60 minutos de trabajo

---

**¿Alguna duda para mañana? Dímelo ahora y lo agrego a la guía.** 😊

---

**Documento creado:** 12 de octubre de 2025 - 22:45h (Madrid)  
**Ejecución:** 13 de octubre de 2025 - Cuando DNS esté listo  
**Contacto soporte:** calvarado1873@gmail.com

