# 🚀 SUBIR TODO - COMANDOS FINALES
**Sitio web bilingüe completo (ES/CA)**

---

## 📋 RESUMEN DE LO QUE ESTÁ LISTO

### **Páginas en Español (5):**
- ✅ index.html (con hreflang y selector)
- ✅ contacto.html (con hreflang y selector)
- ✅ ayuda.html
- ✅ consejos.html (con tarjetas interactivas)
- ✅ gracias.html (con hreflang y selector)

### **Páginas en Catalán (5):**
- ✅ index-ca.html (294 traducciones)
- ✅ contacte-ca.html (formulario completo)
- ✅ ajuda-ca.html (29 traducciones)
- ✅ consells-ca.html (17 traducciones)
- ✅ gracies-ca.html

### **Archivos SEO:**
- ✅ sitemap.xml (actualizado con 10 páginas + hreflang)
- ✅ robots.txt (configurado)

---

## 🚀 COMANDOS PARA SUBIR (COPIA Y PEGA):

### **1. Ir al directorio:**
```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen
```

---

### **2. Subir TODAS las páginas en CATALÁN:**
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

### **3. Subir páginas ES ACTUALIZADAS (con hreflang y selector):**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html \
  contacto.html \
  gracias.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

### **4. Subir archivos SEO:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  sitemap.xml \
  robots.txt \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

### **5. Verificar que se subieron:**
```bash
# Verificar sitemap
curl -s https://carmenalvarado.es/sitemap.xml | grep "index-ca"

# Verificar página principal CA
curl -s https://carmenalvarado.es/index-ca.html | grep "<title>"

# Verificar selector de idioma
curl -s https://carmenalvarado.es/ | grep "language-selector"
```

---

## ✅ RESULTADO ESPERADO:

### **Sitemap debe mostrar:**
```xml
<loc>https://carmenalvarado.es/index-ca.html</loc>
```

### **Title CA debe mostrar:**
```html
<title>Cuidadora Persones Grans Tarragona | Tècnica Sociosanitària Titulada | Carmen Alvarado</title>
```

### **Selector debe mostrar:**
```html
<div class="language-selector"
```

---

## 🌐 VERIFICAR EN NAVEGADOR:

### **Páginas en Español:**
1. https://carmenalvarado.es/ → Debe tener botones ES | CA
2. https://carmenalvarado.es/contacto.html → Debe tener botones ES | CA
3. https://carmenalvarado.es/ayuda.html
4. https://carmenalvarado.es/consejos.html
5. https://carmenalvarado.es/gracias.html → Debe tener botones ES | CA

### **Páginas en Catalán (NUEVAS):**
1. https://carmenalvarado.es/index-ca.html → Debe tener botones ES | CA
2. https://carmenalvarado.es/contacte-ca.html → Debe tener botones ES | CA
3. https://carmenalvarado.es/ajuda-ca.html
4. https://carmenalvarado.es/consells-ca.html
5. https://carmenalvarado.es/gracies-ca.html → Debe tener botones ES | CA

### **Archivos SEO:**
1. https://carmenalvarado.es/sitemap.xml → Debe mostrar 10 URLs
2. https://carmenalvarado.es/robots.txt → Debe mostrar sitemap

---

## 🧪 PROBAR FUNCIONALIDAD:

### **1. Selector de Idioma:**
- Click en "CA" desde página ES → Debe ir a versión CA
- Click en "ES" desde página CA → Debe ir a versión ES

### **2. Formularios:**
- Llenar formulario en `contacte-ca.html`
- Enviar
- Debe redirigir a `gracies-ca.html`
- Email debe llegar a `calvarado1873@gmail.com`
- Subject debe decir "Versió Catalana"

### **3. Enlaces Internos:**
- Navegar entre páginas CA
- Todos los enlaces deben ir a versiones CA
- No debe haber enlaces rotos

### **4. WhatsApp:**
- Click en botón WhatsApp desde página CA
- Debe abrir con mensaje en catalán

---

## 📊 RESUMEN FINAL

### **Total de archivos a subir:**
- 5 páginas CA (nuevas)
- 3 páginas ES (actualizadas)
- 2 archivos SEO (actualizados)

**Total:** 10 archivos

### **Tamaño total:**
- Páginas CA: ~225 KB
- Páginas ES: ~65 KB
- SEO: ~2 KB

**Total:** ~292 KB

### **Tiempo de subida estimado:**
- Con buena conexión: 30-60 segundos
- Con conexión lenta: 2-3 minutos

---

## 🎉 DESPUÉS DE SUBIR

### **Tendrás:**
- ✅ Sitio web bilingüe completo (ES/CA)
- ✅ 10 páginas optimizadas SEO
- ✅ Formularios funcionando en ambos idiomas
- ✅ Selector de idioma visible
- ✅ Hreflang tags correctos
- ✅ Sitemap actualizado
- ✅ Listo para Google Analytics y Search Console

---

## 📞 PRÓXIMOS PASOS (DESPUÉS DE SUBIR):

1. **Instalar Google Analytics** (30 min)
2. **Registrar en Search Console** (15 min)
3. **Enviar sitemap** (5 min)
4. **Crear Google My Business** (30 min)
5. **Probar todo** (30 min)

**Total:** ~2 horas

---

## 🎯 COMANDO ÚNICO (TODO A LA VEZ):

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen && \
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html contacto.html gracias.html \
  index-ca.html contacte-ca.html ajuda-ca.html gracies-ca.html consells-ca.html \
  sitemap.xml robots.txt \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/ && \
echo "✅ TODO SUBIDO - Verificando..." && \
curl -s https://carmenalvarado.es/sitemap.xml | grep -c "<loc>" && \
echo "URLs en sitemap encontradas"
```

---

**¡EJECUTA LOS COMANDOS Y TENDRÁS EL SITIO BILINGÜE COMPLETO!** 🚀🇪🇸🇨🇦

