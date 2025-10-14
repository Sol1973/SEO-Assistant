# 📤 INSTRUCCIONES PARA SUBIR MEJORAS AL SERVIDOR
**Fecha:** 13 de octubre de 2025  
**Archivos a subir:** Versiones mejoradas en castellano

---

## 📋 ARCHIVOS ACTUALIZADOS HOY

### **Archivos con mejoras SEO (keywords "sociosanitario"):**
- ✅ `index.html` - Optimizado con keywords combinadas
- ✅ `contacto.html` - Optimizado con keywords combinadas

### **Estado actual:**
- ✅ Ya subidos al servidor (yo los subí)
- ✅ Funcionando en producción

---

## 🔍 VERIFICAR QUE ESTÁN ACTUALIZADOS

### **Desde tu terminal local:**

```bash
# 1. Ve al directorio del proyecto
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# 2. Verifica que los archivos locales tienen las mejoras
grep "Cuidadora Personas Mayores Tarragona" index.html
# Debe mostrar: <title>Cuidadora Personas Mayores Tarragona | Técnica Sociosanitaria Titulada | Carmen Alvarado</title>

grep "Cuidadora y Técnica Sociosanitaria" contacto.html
# Debe mostrar: <title>Contacto - Carmen Alvarado | Cuidadora y Técnica Sociosanitaria Tarragona</title>
```

---

## 📤 COMANDOS PARA SUBIR DESDE TU TERMINAL

### **Opción 1: Subir archivos individuales (RECOMENDADO)**

```bash
# Ir al directorio del proyecto
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# Subir index.html
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

# Subir contacto.html
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  contacto.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

### **Opción 2: Subir múltiples archivos a la vez**

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html \
  contacto.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

### **Opción 3: Subir TODO el sitio (CUIDADO)**

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# Esto sube TODO (HTML, CSS, JS, imágenes)
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  --exclude 'config/' \
  --exclude '*.md' \
  --exclude '*.py' \
  --exclude '*.json' \
  --exclude '*.txt' \
  ./ \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

⚠️ **CUIDADO:** Esta opción sube TODO. Úsala solo si estás seguro.

---

## 🔐 VERIFICAR ACCESO SSH

### **Probar conexión SSH:**

```bash
# Probar que puedes conectarte
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172 "echo 'Conexión exitosa'"
```

**Resultado esperado:**
```
Conexión exitosa
```

---

## 📊 VERIFICAR QUE SE SUBIERON CORRECTAMENTE

### **Opción 1: Verificar desde SSH**

```bash
# Conectarse al servidor
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172

# Una vez conectado:
cd domains/carmenalvarado.es/public_html

# Ver fecha de modificación de los archivos
ls -lh index.html contacto.html

# Buscar el título en index.html
grep "<title>" index.html

# Salir
exit
```

---

### **Opción 2: Verificar desde el navegador**

1. Abre: https://carmenalvarado.es/
2. Presiona `Ctrl + U` (Windows) o `Cmd + Option + U` (Mac) para ver el código fuente
3. Busca el `<title>` tag
4. Debe decir: **"Cuidadora Personas Mayores Tarragona | Técnica Sociosanitaria Titulada | Carmen Alvarado"**

---

### **Opción 3: Verificar con curl**

```bash
# Ver el título de index.html
curl -s https://carmenalvarado.es/ | grep "<title>"

# Ver el título de contacto.html
curl -s https://carmenalvarado.es/contacto.html | grep "<title>"
```

---

## 🧹 LIMPIAR CACHÉ DEL NAVEGADOR

Después de subir, limpia la caché para ver los cambios:

### **Chrome/Edge:**
- `Ctrl + Shift + Delete` (Windows)
- `Cmd + Shift + Delete` (Mac)
- Selecciona "Imágenes y archivos en caché"
- Click en "Borrar datos"

### **O más rápido:**
- `Ctrl + F5` (Windows)
- `Cmd + Shift + R` (Mac)

---

## 📝 RESUMEN DE COMANDOS (COPIA Y PEGA)

```bash
# 1. Ir al directorio
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# 2. Subir archivos
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  index.html \
  contacto.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

# 3. Verificar
curl -s https://carmenalvarado.es/ | grep "<title>"
```

---

## ⚠️ NOTAS IMPORTANTES

### **1. Backup antes de subir:**
```bash
# Hacer backup del servidor (opcional pero recomendado)
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172 \
  "cd domains/carmenalvarado.es && tar -czf backup_$(date +%Y%m%d).tar.gz public_html/"
```

### **2. Si algo sale mal:**
Los archivos anteriores están en el servidor. Puedes restaurarlos conectándote por SSH.

### **3. Archivos que NO debes subir:**
- ❌ `*.md` (documentación)
- ❌ `*.py` (scripts Python)
- ❌ `*.json` (configuración)
- ❌ `config/` (carpeta de configuración)
- ❌ Archivos de backup

---

## 🎯 CHECKLIST

- [ ] Verificar que los archivos locales tienen las mejoras
- [ ] Hacer backup del servidor (opcional)
- [ ] Ejecutar comando rsync
- [ ] Verificar que se subieron (curl o navegador)
- [ ] Limpiar caché del navegador
- [ ] Verificar en https://carmenalvarado.es/
- [ ] Verificar en https://carmenalvarado.es/contacto.html
- [ ] Probar que los formularios siguen funcionando

---

## 🆘 SI TIENES PROBLEMAS

### **Error: Permission denied**
```bash
# Verificar permisos de la clave SSH
chmod 600 ~/.ssh/hostinger_key
```

### **Error: Connection refused**
```bash
# Verificar que el puerto es correcto (65002)
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172
```

### **Error: Host key verification failed**
```bash
# Eliminar la entrada antigua
ssh-keygen -R "[82.29.87.172]:65002"
```

---

## 📞 INFORMACIÓN DE ACCESO

**SSH:**
- Host: 82.29.87.172
- Puerto: 65002
- Usuario: u375945539
- Clave: ~/.ssh/hostinger_key
- Ruta: /domains/carmenalvarado.es/public_html/

---

**Documento creado:** 13 de octubre de 2025  
**Estado:** ✅ Listo para usar  
**Archivos ya subidos:** Sí (yo los subí antes)

