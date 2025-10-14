# 📤 SUBIR ARCHIVOS UNO POR UNO

## 🚀 COPIA Y PEGA CADA COMANDO (UNO A LA VEZ):

### **1. Ir al directorio:**
```bash
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen
```

---

### **2. Subir index.html:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" index.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

**Espera a que termine. Deberías ver:**
```
sent XXX bytes  received XXX bytes
```

---

### **3. Subir contacto.html:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" contacto.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

### **4. Subir ayuda.html:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" ayuda.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

### **5. Subir consejos.html:**
```bash
rsync -avz -e "ssh -i ~/.ssh/hostinger_key -p 65002" consejos.html u375945539@82.29.87.172:domains/carmenalvarado.es/public_html/
```

---

## ✅ VERIFICAR CADA UNO:

### **Después de subir index.html:**
```bash
curl -s https://carmenalvarado.es/ | grep "<title>"
```

**Debe mostrar:**
```
<title>Cuidadora Personas Mayores Tarragona | Técnica Sociosanitaria Titulada | Carmen Alvarado</title>
```

---

### **Después de subir contacto.html:**
```bash
curl -s https://carmenalvarado.es/contacto.html | grep "<title>"
```

**Debe mostrar:**
```
<title>Contacto - Carmen Alvarado | Cuidadora y Técnica Sociosanitaria Tarragona</title>
```

---

### **Después de subir ayuda.html:**
```bash
curl -s https://carmenalvarado.es/ayuda.html | grep "<title>"
```

**Debe mostrar:**
```
<title>Te Ayudamos: Guía para Cuidar Personas Mayores | Técnica Sociosanitaria Tarragona</title>
```

---

### **Después de subir consejos.html:**
```bash
curl -s https://carmenalvarado.es/consejos.html | grep "<title>"
```

**Debe mostrar:**
```
<title>Consejos para Cuidar Personas Mayores en Casa | Técnica Sociosanitaria Tarragona</title>
```

---

## 🌐 VERIFICAR EN NAVEGADOR:

1. https://carmenalvarado.es/
2. https://carmenalvarado.es/contacto.html
3. https://carmenalvarado.es/ayuda.html
4. https://carmenalvarado.es/consejos.html

**Recuerda:** Presiona `Cmd + Shift + R` para limpiar caché

---

## ⚠️ SI ALGUNO NO SE SUBE:

Dime cuál archivo dio error y lo revisamos.

---

**¡Ejecuta los comandos uno por uno y dime cómo va!** 🚀

