# 🚀 GETTING STARTED - GUÍA PARA DESARROLLADORES

**Para:** Desarrolladores que van a implementar el proyecto  
**Objetivo:** Empezar a desarrollar en 10 minutos  
**Fecha:** 14 de Octubre de 2025  

---

## 📋 **ÍNDICE RÁPIDO**

1. [Requisitos Previos](#requisitos-previos)
2. [Instalación Paso a Paso](#instalación-paso-a-paso)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Flujo de Desarrollo](#flujo-de-desarrollo)
5. [Primeros Pasos](#primeros-pasos)
6. [Comandos Útiles](#comandos-útiles)
7. [Troubleshooting](#troubleshooting)

---

## 🔧 **REQUISITOS PREVIOS**

### **Software Necesario:**
```bash
# Verificar versiones
node --version    # >= 18.0.0 ✅
npm --version     # >= 9.0.0 ✅
git --version     # >= 2.30.0 ✅
```

### **Herramientas Recomendadas:**
- **Editor:** VSCode
- **Extensions VSCode:**
  - ESLint
  - Prettier
  - SQLite Viewer
  - REST Client

---

## 📦 **INSTALACIÓN PASO A PASO**

### **1. Clonar el Repositorio**
```bash
# HTTPS
git clone https://github.com/Sol1973/SEO-Assistant.git

# SSH (si tienes configurado)
git clone git@github.com:Sol1973/SEO-Assistant.git

# Entrar al proyecto
cd SEO-Assistant
```

### **2. Instalar Dependencias**
```bash
# Instalar todas las dependencias
npm install

# Esto instalará:
# - express (servidor)
# - sqlite3 (base de datos)
# - puppeteer (scraping)
# - cheerio (parsing HTML)
# - axios (HTTP client)
# - Jest (testing)
# - ESLint + Prettier (linting)
```

### **3. Configurar Variables de Entorno**
```bash
# Copiar archivo de ejemplo
cp config/env.example .env

# Editar .env (opcional, tiene valores por defecto)
nano .env
```

**Contenido de `.env`:**
```bash
NODE_ENV=development
PORT=3000
DATABASE_PATH=./data/seo-assistant.db
PUPPETEER_HEADLESS=true
PUPPETEER_TIMEOUT=30000
```

### **4. Inicializar Base de Datos**
```bash
# La base de datos se crea automáticamente al iniciar el servidor
# Ubicación: data/seo-assistant.db

# Verificar (después del primer arranque)
ls -la data/
```

### **5. Iniciar Servidor de Desarrollo**
```bash
# Modo desarrollo (con hot reload)
npm run dev

# Debería mostrar:
# ╔════════════════════════════════════════════╗
# ║   SEO ASSISTANT - Server Running 🚀       ║
# ╠════════════════════════════════════════════╣
# ║   Port: 3000                               ║
# ║   URL: http://localhost:3000               ║
# ║   Environment: development                 ║
# ╚════════════════════════════════════════════╝
# ✅ Connected to SQLite database
# ✅ Database schema initialized
```

### **6. Verificar que Funciona**
```bash
# En otra terminal

# Health check
curl http://localhost:3000/api/health

# Debería retornar:
# {
#   "status": "OK",
#   "message": "SEO Assistant API is running",
#   "version": "0.1.0",
#   "timestamp": "2025-10-14T..."
# }
```

### **7. Abrir la Aplicación**
```bash
# Navegador
open http://localhost:3000

# O manualmente:
# http://localhost:3000
```

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
SEO-Assistant/
├── 📂 backend/              # Backend Node.js/Express
│   ├── server.js           # ⭐ Punto de entrada del servidor
│   ├── controllers/        # Lógica de negocio
│   │   └── auditController.js  # ⭐ Controlador principal
│   ├── models/             # Modelos de datos
│   │   └── database.js     # ⭐ Configuración SQLite
│   ├── routes/             # Rutas de API
│   │   ├── audit.js        # Endpoints auditoría
│   │   ├── keywords.js     # Endpoints keywords
│   │   └── reports.js      # Endpoints reportes
│   └── utils/              # Utilidades
│
├── 📂 frontend/             # Frontend HTML/CSS/JS
│   ├── index.html          # ⭐ Página principal
│   ├── css/
│   │   └── styles.css      # Estilos
│   ├── js/
│   │   └── app.js          # ⭐ Lógica frontend
│   └── components/         # Componentes reutilizables
│
├── 📂 tests/                # Tests
│   ├── unit/               # Tests unitarios
│   │   └── audit.test.js   # ⭐ Tests de auditoría
│   └── integration/        # Tests de integración
│
├── 📂 config/               # Configuraciones
│   └── env.example         # Variables de entorno
│
├── 📂 data/                 # Base de datos (se crea automáticamente)
│   └── seo-assistant.db    # SQLite database
│
├── 📂 docs/                 # Documentación adicional
├── 📂 documentacion/        # Docs principales
│
├── 📄 package.json          # ⭐ Dependencias
├── 📄 .eslintrc.json        # Config ESLint
├── 📄 .prettierrc           # Config Prettier
├── 📄 jest.config.js        # Config Jest
└── 📄 .gitignore            # Git ignore
```

**Archivos Clave (⭐):**
1. `backend/server.js` - Servidor Express
2. `backend/controllers/auditController.js` - Lógica SEO
3. `backend/models/database.js` - Base de datos
4. `frontend/index.html` - UI
5. `frontend/js/app.js` - Frontend
6. `tests/unit/audit.test.js` - Tests

---

## 🔄 **FLUJO DE DESARROLLO**

### **1. Crear una Nueva Feature:**
```bash
# Crear rama
git checkout -b feature/nueva-funcionalidad

# Desarrollar
# ... editar archivos ...

# Verificar linting
npm run lint

# Ejecutar tests
npm test

# Commit
git add .
git commit -m "feat: descripción de la funcionalidad"

# Push
git push origin feature/nueva-funcionalidad

# Crear Pull Request en GitHub
```

### **2. Flujo de Trabajo Típico:**
```
1. Leer requisito en MASTER_PLAN.md
2. Crear rama feature/
3. Implementar cambios
4. Escribir tests
5. Ejecutar npm test
6. Verificar npm run lint
7. Commit y push
8. PR en GitHub
```

---

## 🎯 **PRIMEROS PASOS**

### **¿Por dónde empezar?**

#### **Opción A: Entender el Código Existente**
```bash
# 1. Leer el servidor
code backend/server.js

# 2. Entender la lógica SEO
code backend/controllers/auditController.js

# 3. Ver la base de datos
code backend/models/database.js

# 4. Revisar el frontend
code frontend/index.html
code frontend/js/app.js
```

#### **Opción B: Probar Funcionalidad Existente**
```bash
# 1. Iniciar servidor
npm run dev

# 2. Abrir http://localhost:3000

# 3. Probar auditoría:
#    - Ingresar URL: https://example.com
#    - Click "Analizar"
#    - Ver resultados (3-5 segundos)

# 4. Ver base de datos:
sqlite3 data/seo-assistant.db
> .tables
> SELECT * FROM audits;
> .quit
```

#### **Opción C: Implementar Nueva Feature (Siguiendo MASTER_PLAN.md)**
```bash
# Ver el plan de sesiones
cat MASTER_PLAN.md

# Sesión 1: Verificación ✅ (ya hecho en instalación)
# Sesión 2: Electron (siguiente)
# Sesión 3: UI/UX
# Sesión 4: Demo online
# Sesión 5: PDF Reports
# Sesión 6: Testing

# Empezar con Sesión 2 - Electron:
npm install --save-dev electron electron-builder
```

---

## 🛠️ **COMANDOS ÚTILES**

### **Desarrollo:**
```bash
# Iniciar servidor (con hot reload)
npm run dev

# Iniciar servidor (producción)
npm start

# Formatear código
npm run format

# Linting
npm run lint
npm run lint:fix
```

### **Testing:**
```bash
# Ejecutar todos los tests
npm test

# Watch mode (se ejecutan al guardar)
npm run test:watch

# Coverage
npm run test:coverage
```

### **Base de Datos:**
```bash
# Abrir SQLite
sqlite3 data/seo-assistant.db

# Comandos SQLite útiles:
.tables                    # Ver tablas
.schema audits            # Ver schema de tabla
SELECT * FROM audits;     # Ver datos
.quit                     # Salir
```

### **Git:**
```bash
# Estado
git status

# Crear rama
git checkout -b feature/nombre

# Commit
git add .
git commit -m "tipo: mensaje"

# Push
git push origin rama

# Actualizar main
git checkout main
git pull origin main
```

---

## 🔍 **DEBUGGING**

### **Ver Logs del Servidor:**
```bash
# Los logs se muestran en la terminal donde corriste npm run dev

# Logs importantes:
✅ Connected to SQLite database
✅ Database schema initialized
✅ Audit 1 completed
❌ Error processing audit 1: ...
```

### **Debugging con VSCode:**
```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Server",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/backend/server.js",
      "runtimeArgs": ["--inspect"],
      "console": "integratedTerminal"
    }
  ]
}
```

### **Debugging Frontend:**
```bash
# Chrome DevTools
# 1. Abrir http://localhost:3000
# 2. F12 (DevTools)
# 3. Console / Network / Sources
```

---

## ❓ **TROUBLESHOOTING**

### **Error: Cannot find module**
```bash
# Solución: Reinstalar dependencias
rm -rf node_modules package-lock.json
npm install
```

### **Error: Port 3000 already in use**
```bash
# Solución 1: Matar el proceso
lsof -ti:3000 | xargs kill -9

# Solución 2: Cambiar puerto en .env
echo "PORT=3001" >> .env
npm run dev
```

### **Error: Database locked**
```bash
# Solución: Eliminar DB y reiniciar
rm -rf data/
npm run dev
# La DB se recreará automáticamente
```

### **Tests fallan**
```bash
# Verificar que el servidor NO esté corriendo
# Los tests crean su propia DB temporal

# Solución:
# 1. Detener servidor (Ctrl+C)
# 2. Ejecutar tests
npm test
```

### **Puppeteer no funciona**
```bash
# En macOS con M1/M2
# Solución:
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
export PUPPETEER_EXECUTABLE_PATH=`which chromium`
npm install
```

---

## 📚 **DOCUMENTACIÓN RELACIONADA**

### **Orden de Lectura Recomendado:**
1. **GETTING_STARTED_DEV.md** ← Este documento
2. **API_SPECIFICATION.md** - Endpoints detallados
3. **DATABASE_SCHEMA.md** - Esquema de BD
4. **MASTER_PLAN.md** - Plan de implementación
5. **DEVELOPMENT.md** - Guía completa

### **Para Consultas Específicas:**
- **API Endpoints:** `API_SPECIFICATION.md`
- **Base de Datos:** `DATABASE_SCHEMA.md`
- **Algoritmos SEO:** `backend/controllers/auditController.js`
- **Frontend:** `frontend/js/app.js`
- **Tests:** `tests/unit/audit.test.js`

---

## 🎯 **CHECKLIST PRIMER DÍA**

### **Setup Inicial:**
- [ ] Node.js 18+ instalado
- [ ] Git configurado
- [ ] VSCode con extensiones
- [ ] Repositorio clonado
- [ ] `npm install` exitoso
- [ ] `.env` configurado
- [ ] `npm run dev` funciona
- [ ] http://localhost:3000 carga
- [ ] Tests pasan (`npm test`)

### **Familiarización:**
- [ ] Leer `backend/server.js`
- [ ] Leer `backend/controllers/auditController.js`
- [ ] Leer `backend/models/database.js`
- [ ] Probar una auditoría en el browser
- [ ] Ver la BD con SQLite
- [ ] Ejecutar tests y entenderlos

### **Siguiente Paso:**
- [ ] Leer `MASTER_PLAN.md`
- [ ] Leer `API_SPECIFICATION.md`
- [ ] Leer `DATABASE_SCHEMA.md`
- [ ] Decidir qué implementar (Sesión 2, 3, 4, 5 o 6)

---

## 🚀 **SIGUIENTE PASO**

**Una vez que tengas todo funcionando:**

1. ✅ Lee **MASTER_PLAN.md** para ver el plan completo
2. ✅ Revisa **API_SPECIFICATION.md** para endpoints
3. ✅ Estudia **DATABASE_SCHEMA.md** para la BD
4. ✅ Elige una sesión del MASTER_PLAN para implementar

**Recomendación:** Empezar con **Sesión 2 - Electron** para hacer la app portable.

---

**¡Listo para desarrollar!** 🎉

**¿Dudas?** Revisa `DEVELOPMENT.md` para más detalles.

