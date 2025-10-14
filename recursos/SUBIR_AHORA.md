# 📤 SUBIR ARCHIVOS AHORA - INSTRUCCIONES RÁPIDAS

## 🚀 COPIA Y PEGA ESTOS COMANDOS:

### **1. Ir al directorio:**
```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen
```

### **2. Subir TODO lo optimizado:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html \
  contacto.html \
  ayuda.html \
  consejos.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

### **3. Verificar que se subieron:**
```bash
curl -s https://carmenalvarado.es/ | grep "<title>"
curl -s https://carmenalvarado.es/consejos.html | grep "<title>"
```

---

## ✅ RESULTADO ESPERADO:

Deberías ver:
```
<title>Cuidadora Personas Mayores Tarragona | Técnica Sociosanitaria Titulada | Carmen Alvarado</title>
<title>Consejos para Cuidar Personas Mayores en Casa | Técnica Sociosanitaria Tarragona</title>
```

---

## 🌐 VERIFICAR EN NAVEGADOR:

1. https://carmenalvarado.es/
2. https://carmenalvarado.es/contacto.html
3. https://carmenalvarado.es/ayuda.html
4. https://carmenalvarado.es/consejos.html (NUEVO)

---

## 📊 ARCHIVOS QUE SE SUBIRÁN:

- ✅ `index.html` - Optimizado con keywords combinadas
- ✅ `contacto.html` - Optimizado con keywords
- ✅ `ayuda.html` - Optimizado con keywords
- ✅ `consejos.html` - NUEVO con 7 consejos profesionales

---

## ⏰ TIEMPO: ~30 segundos

---

**¡LISTO! Después de ejecutar, todo estará actualizado en el servidor.**

