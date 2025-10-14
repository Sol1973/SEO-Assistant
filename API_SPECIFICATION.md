# 📡 API SPECIFICATION - Documentación Completa

**Versión:** 0.1.0  
**Base URL:** `http://localhost:3000/api`  
**Formato:** JSON  
**Fecha:** 14 de Octubre de 2025  

---

## 📋 **ÍNDICE**

1. [Health Check](#1-health-check)
2. [Auditoría SEO](#2-auditoría-seo)
3. [Keywords Research](#3-keywords-research)
4. [Reportes](#4-reportes)
5. [Códigos de Error](#5-códigos-de-error)
6. [Ejemplos de Uso](#6-ejemplos-de-uso)

---

## 1. **HEALTH CHECK**

### `GET /api/health`
Verifica que el servidor esté funcionando.

#### **Request:**
```bash
curl http://localhost:3000/api/health
```

#### **Response:** `200 OK`
```json
{
  "status": "OK",
  "message": "SEO Assistant API is running",
  "version": "0.1.0",
  "timestamp": "2025-10-14T10:30:00.000Z"
}
```

---

## 2. **AUDITORÍA SEO**

### `POST /api/audit`
Inicia una nueva auditoría SEO de un sitio web.

#### **Request:**
```bash
curl -X POST http://localhost:3000/api/audit \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com"
  }'
```

#### **Request Body:**
```json
{
  "url": "https://example.com"  // Requerido
}
```

**Validaciones:**
- `url` debe ser una URL válida (http:// o https://)
- `url` debe ser accesible
- Timeout máximo: 30 segundos

#### **Response:** `200 OK`
```json
{
  "success": true,
  "message": "Audit started",
  "data": {
    "auditId": 1,
    "url": "https://example.com",
    "status": "pending"
  }
}
```

#### **Response:** `400 Bad Request`
```json
{
  "error": "Bad Request",
  "message": "URL is required"
}
```

---

### `GET /api/audit/:id`
Obtiene los resultados de una auditoría.

#### **Request:**
```bash
curl http://localhost:3000/api/audit/1
```

#### **Response:** `200 OK` (Pending)
```json
{
  "success": true,
  "data": {
    "auditId": 1,
    "url": "https://example.com",
    "status": "pending",
    "results": null,
    "overallScore": null,
    "createdAt": "2025-10-14T10:30:00.000Z",
    "completedAt": null
  }
}
```

#### **Response:** `200 OK` (Completed)
```json
{
  "success": true,
  "data": {
    "auditId": 1,
    "url": "https://example.com",
    "status": "completed",
    "results": {
      "metaTags": {
        "score": 75
      },
      "headings": {
        "score": 90
      },
      "images": {
        "score": 85
      }
    },
    "overallScore": 83,
    "createdAt": "2025-10-14T10:30:00.000Z",
    "completedAt": "2025-10-14T10:30:05.000Z"
  }
}
```

#### **Response:** `404 Not Found`
```json
{
  "error": "Not Found",
  "message": "Audit not found"
}
```

---

## 3. **KEYWORDS RESEARCH**

### `POST /api/keywords/research`
Investiga keywords relacionadas.

#### **Request:**
```bash
curl -X POST http://localhost:3000/api/keywords/research \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "seo audit",
    "language": "es",
    "country": "ES"
  }'
```

#### **Request Body:**
```json
{
  "keyword": "seo audit",      // Requerido
  "language": "es",             // Opcional (default: "es")
  "country": "ES"               // Opcional (default: "ES")
}
```

#### **Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "keyword": "seo audit",
    "suggestions": [
      {
        "term": "seo audit gratis",
        "volume": 1000,
        "difficulty": 45
      },
      {
        "term": "seo audit online",
        "volume": 800,
        "difficulty": 55
      },
      {
        "term": "seo audit mejor",
        "volume": 600,
        "difficulty": 50
      }
    ]
  }
}
```

**⚠️ Nota:** Actualmente retorna datos de ejemplo. Implementación real pendiente.

---

### `GET /api/keywords/tracking`
Obtiene el tracking de rankings de keywords.

#### **Request:**
```bash
curl http://localhost:3000/api/keywords/tracking
```

#### **Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "keywords": [
      {
        "term": "seo audit",
        "position": 12,
        "change": 3
      },
      {
        "term": "keyword research",
        "position": 8,
        "change": -1
      }
    ]
  }
}
```

**⚠️ Nota:** Actualmente retorna datos de ejemplo. Implementación real pendiente.

---

## 4. **REPORTES**

### `POST /api/reports/generate`
Genera un reporte de auditoría.

#### **Request:**
```bash
curl -X POST http://localhost:3000/api/reports/generate \
  -H "Content-Type: application/json" \
  -d '{
    "auditId": 1,
    "format": "pdf"
  }'
```

#### **Request Body:**
```json
{
  "auditId": 1,           // Requerido
  "format": "pdf"         // Opcional (default: "json")
}
```

**Formatos soportados:**
- `json` - Reporte en formato JSON
- `pdf` - Reporte en formato PDF (pendiente implementación)

#### **Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "reportId": "1234567890",
    "format": "pdf",
    "downloadUrl": "/api/reports/download/1234567890"
  }
}
```

**⚠️ Nota:** PDF pendiente de implementación (Sesión 5 del MASTER_PLAN).

---

### `GET /api/reports/download/:id`
Descarga un reporte generado.

#### **Request:**
```bash
curl http://localhost:3000/api/reports/download/1234567890 \
  -o report.pdf
```

#### **Response:** `200 OK`
```
[Binary PDF data]
```

**Headers:**
```
Content-Type: application/pdf
Content-Disposition: attachment; filename=audit-1.pdf
```

**⚠️ Nota:** Pendiente de implementación.

---

## 5. **CÓDIGOS DE ERROR**

### **400 Bad Request**
```json
{
  "error": "Bad Request",
  "message": "URL is required"
}
```

**Causas comunes:**
- Falta parámetro requerido
- Formato de datos incorrecto
- URL inválida

---

### **404 Not Found**
```json
{
  "error": "Not Found",
  "message": "Audit not found"
}
```

**Causas comunes:**
- ID de auditoría no existe
- Recurso eliminado
- Ruta incorrecta

---

### **500 Internal Server Error**
```json
{
  "error": "Internal Server Error",
  "message": "Error starting audit: ..."
}
```

**Causas comunes:**
- Error en Puppeteer
- Error de base de datos
- Timeout en scraping
- URL no accesible

---

## 6. **EJEMPLOS DE USO**

### **Flujo Completo de Auditoría:**

```javascript
// 1. Iniciar auditoría
const auditResponse = await fetch('http://localhost:3000/api/audit', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ url: 'https://example.com' })
});

const audit = await auditResponse.json();
const auditId = audit.data.auditId;
console.log('Audit ID:', auditId);

// 2. Esperar procesamiento (3-5 segundos)
await new Promise(resolve => setTimeout(resolve, 5000));

// 3. Obtener resultados
const resultsResponse = await fetch(`http://localhost:3000/api/audit/${auditId}`);
const results = await resultsResponse.json();

if (results.data.status === 'completed') {
  console.log('Overall Score:', results.data.overallScore);
  console.log('Meta Tags Score:', results.data.results.metaTags.score);
  console.log('Headings Score:', results.data.results.headings.score);
  console.log('Images Score:', results.data.results.images.score);
}

// 4. Generar reporte PDF
const reportResponse = await fetch('http://localhost:3000/api/reports/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ auditId, format: 'pdf' })
});

const report = await reportResponse.json();
console.log('Download URL:', report.data.downloadUrl);
```

---

### **cURL Examples:**

#### **Auditoría Completa:**
```bash
# 1. Iniciar
AUDIT_ID=$(curl -s -X POST http://localhost:3000/api/audit \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}' | jq -r '.data.auditId')

echo "Audit ID: $AUDIT_ID"

# 2. Esperar 5 segundos
sleep 5

# 3. Ver resultados
curl http://localhost:3000/api/audit/$AUDIT_ID | jq '.'
```

---

### **JavaScript Fetch:**

```javascript
// Función helper
async function runAudit(url) {
  try {
    // Iniciar auditoría
    const response = await fetch('http://localhost:3000/api/audit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    
    const data = await response.json();
    
    if (!data.success) {
      throw new Error(data.message);
    }
    
    return data.data.auditId;
  } catch (error) {
    console.error('Error:', error.message);
    throw error;
  }
}

// Uso
const auditId = await runAudit('https://example.com');
console.log('Audit started:', auditId);
```

---

### **Axios Example:**

```javascript
const axios = require('axios');

async function createAudit(url) {
  try {
    const response = await axios.post('http://localhost:3000/api/audit', {
      url
    });
    
    return response.data.data;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.message);
    } else {
      console.error('Error:', error.message);
    }
    throw error;
  }
}

// Uso
const audit = await createAudit('https://example.com');
console.log('Audit ID:', audit.auditId);
```

---

## 📊 **ESTRUCTURA DE DATOS**

### **Audit Object:**
```typescript
interface Audit {
  id: number;
  url: string;
  status: 'pending' | 'completed' | 'failed';
  created_at: string;          // ISO 8601
  completed_at: string | null; // ISO 8601
  meta_score: number | null;   // 0-100
  headings_score: number | null; // 0-100
  images_score: number | null;   // 0-100
  overall_score: number | null;  // 0-100
  results: string | null;        // JSON stringified
}
```

### **Results Object:**
```typescript
interface Results {
  metaTags: {
    score: number;  // 0-100
  };
  headings: {
    score: number;  // 0-100
  };
  images: {
    score: number;  // 0-100
  };
}
```

---

## 🔐 **AUTENTICACIÓN**

**Actualmente:** No hay autenticación (app local).

**Futuro (v2):**
- API Key para acceso externo
- OAuth para integraciones
- Rate limiting

---

## 📝 **NOTAS IMPORTANTES**

1. **Timeout:** Las auditorías tienen un timeout de 30 segundos
2. **Rate Limiting:** No implementado aún
3. **CORS:** Habilitado para desarrollo
4. **Cache:** No implementado
5. **Webhooks:** No implementado

---

## 🚀 **PRÓXIMAS MEJORAS**

### **v0.2.0:**
- [ ] Keyword research funcional
- [ ] Tracking de rankings real
- [ ] Cache de resultados

### **v0.3.0:**
- [ ] Generación de PDF
- [ ] Múltiples formatos (JSON, PDF, CSV)
- [ ] Webhooks para notificaciones

### **v0.4.0:**
- [ ] API Key authentication
- [ ] Rate limiting
- [ ] GraphQL endpoint

---

**Última actualización:** 14 de Octubre de 2025  
**Documentación relacionada:** `DATABASE_SCHEMA.md`, `GETTING_STARTED_DEV.md`

