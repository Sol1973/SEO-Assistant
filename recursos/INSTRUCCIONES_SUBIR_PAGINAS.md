# 📤 INSTRUCCIONES PARA SUBIR LAS PÁGINAS HTML

## 🚀 PASO 1: Subir las páginas al servidor

Abre tu terminal y ejecuta estos comandos:

### **Opción A: Subir con rsync (RECOMENDADO)**

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" \
  contacto.html \
  gracias.html \
  consejos.html \
  u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

### **Opción B: Subir con scp (alternativa)**

```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

scp -i ~/.ssh/hostinger_key -P 65002 contacto.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

scp -i ~/.ssh/hostinger_key -P 65002 gracias.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/

scp -i ~/.ssh/hostinger_key -P 65002 consejos.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

## ✅ PASO 2: Verificar que se subieron correctamente

```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172 "ls -lh domains/carmenalvarado.es/public_html/*.html"
```

Deberías ver:
- contacto.html
- gracias.html
- consejos.html
- index.html
- ayuda.html

---

## 🌐 PASO 3: Probar las páginas en el navegador

Abre estas URLs en tu navegador:

1. **Contacto:** https://carmenalvarado.es/contacto.html
2. **Gracias:** https://carmenalvarado.es/gracias.html
3. **Consejos:** https://carmenalvarado.es/consejos.html

---

## 📧 PASO 4: Probar el formulario de contacto

1. Ve a: https://carmenalvarado.es/contacto.html
2. Rellena el formulario con datos de prueba
3. Envía el formulario
4. Deberías ser redirigido a: https://carmenalvarado.es/gracias.html
5. **Revisa el correo:** calvarado1873@gmail.com

---

## 🗑️ PASO 5: Borrar la página de WordPress (SOLO SI TODO FUNCIONA)

**⚠️ IMPORTANTE: Solo haz esto DESPUÉS de verificar que el formulario HTML funciona correctamente**

### Desde WordPress Admin:

1. Ve a: https://carmenalvarado.es/wp-admin
2. Ve a `Páginas -> Todas las páginas`
3. Busca "Formulario de Contacto" o "Contacta a Carmen Alvarado"
4. Muévela a la papelera (NO la borres permanentemente todavía)
5. Verifica que todo sigue funcionando
6. Si todo está bien, borra permanentemente

### Desde SSH (alternativa):

```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172

cd domains/carmenalvarado.es/public_html

# Ver páginas de WordPress
wp post list --post_type=page --format=table

# Mover a papelera (reemplaza ID con el número correcto)
wp post delete 10 --force=false

# Si todo funciona bien, borrar permanentemente
# wp post delete 10 --force
```

---

## 🔗 PASO 6: Actualizar enlaces en index.html

Después de verificar que todo funciona, actualiza los enlaces en `index.html`:

```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172

cd domains/carmenalvarado.es/public_html

# Hacer backup
cp index.html index.html.backup

# Editar para cambiar los enlaces de /formulario-de-contacto/ a /contacto.html
# Esto lo haremos después de confirmar que todo funciona
```

---

## 📝 CHECKLIST

- [ ] Páginas subidas al servidor
- [ ] Verificado que se ven correctamente en el navegador
- [ ] Formulario de contacto probado
- [ ] Email recibido en calvarado1873@gmail.com
- [ ] Página de "gracias" funciona
- [ ] Página de consejos se ve bien
- [ ] Enlaces en el menú funcionan
- [ ] Página de WordPress movida a papelera
- [ ] Todo verificado y funcionando

---

## 🚨 SI ALGO SALE MAL

### Restaurar backup:

```bash
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172

cd domains/carmenalvarado.es/public_html

# Restaurar página de WordPress desde papelera
wp post untrash 10

# Borrar páginas HTML si es necesario
rm contacto.html gracias.html consejos.html
```

---

## 💡 NOTAS IMPORTANTES

1. **No borres nada de WordPress hasta verificar que el formulario HTML funciona**
2. **Guarda el ID de la página de WordPress por si necesitas restaurarla**
3. **Haz pruebas del formulario con tu propio email primero**
4. **Verifica que FormSubmit.co no requiera verificación adicional**

---

¡Buena suerte! 🚀

