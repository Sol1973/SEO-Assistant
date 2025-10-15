# 🚀 DEPLOY EN VERCEL - GUÍA COMPLETA

**Fecha:** 15 de Octubre de 2025 - 13:15 (Madrid)  
**Estado:** ✅ Configurado y listo para deploy

---

## 📋 **PASOS PARA DEPLOY:**

### **1. Instalar Vercel CLI**
```bash
npm install -g vercel
```

### **2. Login en Vercel**
```bash
vercel login
```

### **3. Deploy desde el directorio del proyecto**
```bash
cd /Users/micky/Documents/Proyectos_IA/SEO_ASSISTANT/SEO_ASSISTANT_COMPLETE
vercel
```

### **4. Configurar variables de entorno en Vercel Dashboard:**
- `NODE_ENV` = `production`
- `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD` = `true`
- `PUPPETEER_EXECUTABLE_PATH` = `/usr/bin/google-chrome-stable`

---

## 🔧 **ARCHIVOS CONFIGURADOS:**

### **✅ vercel.json**
- Configuración de builds
- Rutas para API y frontend
- Variables de entorno
- Timeout de 30 segundos

### **✅ backend/server.js**
- Adaptado para Vercel
- Solo inicia servidor si no está en Vercel
- Manejo de variables de entorno

### **✅ backend/controllers/auditController.js**
- Puppeteer configurado para producción
- Args para Vercel (--no-sandbox, etc.)
- User agent configurado

### **✅ api/index.js**
- Punto de entrada para Vercel
- Importa la app Express

---

## 🌐 **URL ESPERADA:**
`https://seo-assistant-demo.vercel.app`

---

## ⚠️ **CONSIDERACIONES:**

1. **Puppeteer en Vercel:**
   - Usa Chrome preinstalado
   - Args de seguridad configurados
   - Timeout de 30 segundos máximo

2. **Base de datos:**
   - SQLite en memoria (no persistente)
   - Cada función serverless es independiente

3. **Rate limiting:**
   - 50 requests por 15 minutos
   - Configurado para demo

---

## 🧪 **TESTING POST-DEPLOY:**

1. **Homepage:** `GET /`
2. **API Health:** `GET /api/health`
3. **Audit:** `POST /api/audit`
4. **Results:** `GET /api/audit/{id}`

---

## 📝 **COMANDOS ÚTILES:**

```bash
# Deploy
vercel

# Deploy a producción
vercel --prod

# Ver logs
vercel logs

# Remover deploy
vercel remove
```
