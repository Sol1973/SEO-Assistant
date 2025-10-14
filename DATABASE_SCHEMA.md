# 🗄️ DATABASE SCHEMA - Especificación Completa

**Base de Datos:** SQLite  
**Ubicación:** `data/seo-assistant.db`  
**Versión:** 1.0  
**Fecha:** 14 de Octubre de 2025  

---

## 📋 **ÍNDICE**

1. [Diagrama ER](#1-diagrama-er)
2. [Tablas](#2-tablas)
3. [Relaciones](#3-relaciones)
4. [Índices](#4-índices)
5. [Queries Comunes](#5-queries-comunes)
6. [Migraciones](#6-migraciones)

---

## 1. **DIAGRAMA ER**

```
┌─────────────────────────────────┐
│          audits                 │
├─────────────────────────────────┤
│ id (PK)                         │
│ url                             │
│ status                          │
│ created_at                      │
│ completed_at                    │
│ meta_score                      │
│ headings_score                  │
│ images_score                    │
│ overall_score                   │
│ results (JSON)                  │
└────────────┬────────────────────┘
             │
             │ 1:N
             │
┌────────────▼────────────────────┐
│         reports                 │
├─────────────────────────────────┤
│ id (PK)                         │
│ audit_id (FK)                   │
│ format                          │
│ file_path                       │
│ created_at                      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│         keywords                │
├─────────────────────────────────┤
│ id (PK)                         │
│ keyword                         │
│ language                        │
│ country                         │
│ volume                          │
│ difficulty                      │
│ created_at                      │
└────────────┬────────────────────┘
             │
             │ 1:N
             │
┌────────────▼────────────────────┐
│      keyword_tracking           │
├─────────────────────────────────┤
│ id (PK)                         │
│ keyword_id (FK)                 │
│ url                             │
│ position                        │
│ checked_at                      │
└─────────────────────────────────┘
```

---

## 2. **TABLAS**

### 2.1 **audits**
Almacena las auditorías SEO realizadas.

```sql
CREATE TABLE audits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  completed_at DATETIME,
  meta_score INTEGER,
  headings_score INTEGER,
  images_score INTEGER,
  overall_score INTEGER,
  results TEXT
);
```

**Campos:**

| Campo | Tipo | Nulo | Default | Descripción |
|---|---|---|---|---|
| `id` | INTEGER | NO | AUTO | ID único de la auditoría |
| `url` | TEXT | NO | - | URL del sitio auditado |
| `status` | TEXT | NO | 'pending' | Estado: pending, completed, failed |
| `created_at` | DATETIME | NO | NOW | Fecha/hora de creación |
| `completed_at` | DATETIME | SÍ | NULL | Fecha/hora de finalización |
| `meta_score` | INTEGER | SÍ | NULL | Score de meta tags (0-100) |
| `headings_score` | INTEGER | SÍ | NULL | Score de headings (0-100) |
| `images_score` | INTEGER | SÍ | NULL | Score de imágenes (0-100) |
| `overall_score` | INTEGER | SÍ | NULL | Score general (0-100) |
| `results` | TEXT | SÍ | NULL | JSON con resultados detallados |

**Valores de `status`:**
- `pending` - Auditoría en proceso
- `completed` - Auditoría completada
- `failed` - Auditoría falló

**Ejemplo de `results` (JSON):**
```json
{
  "metaTags": { "score": 75 },
  "headings": { "score": 90 },
  "images": { "score": 85 }
}
```

---

### 2.2 **keywords**
Almacena keywords investigadas.

```sql
CREATE TABLE keywords (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  keyword TEXT NOT NULL,
  language TEXT DEFAULT 'es',
  country TEXT DEFAULT 'ES',
  volume INTEGER,
  difficulty INTEGER,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Campos:**

| Campo | Tipo | Nulo | Default | Descripción |
|---|---|---|---|---|
| `id` | INTEGER | NO | AUTO | ID único del keyword |
| `keyword` | TEXT | NO | - | Término de búsqueda |
| `language` | TEXT | NO | 'es' | Idioma (es, en, ca) |
| `country` | TEXT | NO | 'ES' | País (ES, US, MX) |
| `volume` | INTEGER | SÍ | NULL | Volumen de búsquedas mensual |
| `difficulty` | INTEGER | SÍ | NULL | Dificultad SEO (0-100) |
| `created_at` | DATETIME | NO | NOW | Fecha de investigación |

---

### 2.3 **keyword_tracking**
Almacena el tracking de posiciones de keywords.

```sql
CREATE TABLE keyword_tracking (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  keyword_id INTEGER,
  url TEXT NOT NULL,
  position INTEGER,
  checked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (keyword_id) REFERENCES keywords(id)
);
```

**Campos:**

| Campo | Tipo | Nulo | Default | Descripción |
|---|---|---|---|---|
| `id` | INTEGER | NO | AUTO | ID único del tracking |
| `keyword_id` | INTEGER | SÍ | NULL | FK a keywords.id |
| `url` | TEXT | NO | - | URL del sitio |
| `position` | INTEGER | SÍ | NULL | Posición en resultados (1-100) |
| `checked_at` | DATETIME | NO | NOW | Fecha/hora de comprobación |

---

### 2.4 **reports**
Almacena reportes generados.

```sql
CREATE TABLE reports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  audit_id INTEGER,
  format TEXT DEFAULT 'json',
  file_path TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (audit_id) REFERENCES audits(id)
);
```

**Campos:**

| Campo | Tipo | Nulo | Default | Descripción |
|---|---|---|---|---|
| `id` | INTEGER | NO | AUTO | ID único del reporte |
| `audit_id` | INTEGER | SÍ | NULL | FK a audits.id |
| `format` | TEXT | NO | 'json' | Formato: json, pdf, csv |
| `file_path` | TEXT | SÍ | NULL | Ruta al archivo generado |
| `created_at` | DATETIME | NO | NOW | Fecha de generación |

---

## 3. **RELACIONES**

### 3.1 **audits → reports**
**Tipo:** 1:N (Un audit puede tener múltiples reportes)

```sql
-- Un audit puede tener varios reportes en diferentes formatos
SELECT a.*, r.format, r.file_path
FROM audits a
LEFT JOIN reports r ON a.id = r.audit_id
WHERE a.id = 1;
```

---

### 3.2 **keywords → keyword_tracking**
**Tipo:** 1:N (Un keyword puede tener múltiples trackings)

```sql
-- Ver el historial de posiciones de un keyword
SELECT k.keyword, kt.position, kt.checked_at
FROM keywords k
JOIN keyword_tracking kt ON k.id = kt.keyword_id
WHERE k.id = 1
ORDER BY kt.checked_at DESC;
```

---

## 4. **ÍNDICES**

```sql
-- Índice para búsquedas por URL
CREATE INDEX idx_audits_url ON audits(url);

-- Índice para búsquedas por estado
CREATE INDEX idx_audits_status ON audits(status);

-- Índice para búsquedas por fecha
CREATE INDEX idx_audits_created_at ON audits(created_at);

-- Índice para keywords
CREATE INDEX idx_keywords_keyword ON keywords(keyword);

-- Índice para tracking por keyword
CREATE INDEX idx_tracking_keyword_id ON keyword_tracking(keyword_id);
```

---

## 5. **QUERIES COMUNES**

### 5.1 **Crear Nueva Auditoría**
```sql
INSERT INTO audits (url, status)
VALUES ('https://example.com', 'pending');

-- Obtener el ID
SELECT last_insert_rowid();
```

**En JavaScript:**
```javascript
const { run } = require('./backend/models/database');

const result = await run(
  'INSERT INTO audits (url, status) VALUES (?, ?)',
  ['https://example.com', 'pending']
);

const auditId = result.id;
```

---

### 5.2 **Actualizar Auditoría Completada**
```sql
UPDATE audits
SET 
  status = 'completed',
  completed_at = CURRENT_TIMESTAMP,
  meta_score = 75,
  headings_score = 90,
  images_score = 85,
  overall_score = 83,
  results = '{"metaTags":{"score":75},"headings":{"score":90},"images":{"score":85}}'
WHERE id = 1;
```

**En JavaScript:**
```javascript
await run(
  `UPDATE audits 
   SET status = ?, completed_at = CURRENT_TIMESTAMP, 
       meta_score = ?, headings_score = ?, images_score = ?, 
       overall_score = ?, results = ?
   WHERE id = ?`,
  ['completed', 75, 90, 85, 83, JSON.stringify(results), auditId]
);
```

---

### 5.3 **Obtener Resultados de Auditoría**
```sql
SELECT * FROM audits WHERE id = 1;
```

**En JavaScript:**
```javascript
const { get } = require('./backend/models/database');

const audit = await get('SELECT * FROM audits WHERE id = ?', [1]);

// Parsear results si existe
if (audit.results) {
  audit.results = JSON.parse(audit.results);
}
```

---

### 5.4 **Listar Últimas Auditorías**
```sql
SELECT id, url, status, overall_score, created_at
FROM audits
ORDER BY created_at DESC
LIMIT 10;
```

**En JavaScript:**
```javascript
const { all } = require('./backend/models/database');

const audits = await all(
  'SELECT id, url, status, overall_score, created_at FROM audits ORDER BY created_at DESC LIMIT 10'
);
```

---

### 5.5 **Buscar Auditorías por URL**
```sql
SELECT * FROM audits
WHERE url LIKE '%example.com%'
ORDER BY created_at DESC;
```

---

### 5.6 **Estadísticas de Auditorías**
```sql
SELECT 
  COUNT(*) as total,
  AVG(overall_score) as avg_score,
  MAX(overall_score) as max_score,
  MIN(overall_score) as min_score
FROM audits
WHERE status = 'completed';
```

---

### 5.7 **Crear Keyword**
```sql
INSERT INTO keywords (keyword, language, country, volume, difficulty)
VALUES ('seo audit', 'es', 'ES', 1000, 45);
```

---

### 5.8 **Tracking de Keyword**
```sql
INSERT INTO keyword_tracking (keyword_id, url, position)
VALUES (1, 'https://example.com', 12);
```

---

### 5.9 **Historial de Posiciones**
```sql
SELECT 
  kt.checked_at,
  kt.position,
  LAG(kt.position) OVER (ORDER BY kt.checked_at) as previous_position,
  kt.position - LAG(kt.position) OVER (ORDER BY kt.checked_at) as change
FROM keyword_tracking kt
WHERE kt.keyword_id = 1
ORDER BY kt.checked_at DESC;
```

---

### 5.10 **Generar Reporte**
```sql
INSERT INTO reports (audit_id, format, file_path)
VALUES (1, 'pdf', '/reports/audit-1.pdf');
```

---

## 6. **MIGRACIONES**

### 6.1 **Inicialización (v1.0)**

**Archivo:** `backend/models/database.js`

```javascript
const initDatabase = () => {
  db.serialize(() => {
    // Crear tabla audits
    db.run(`
      CREATE TABLE IF NOT EXISTS audits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        completed_at DATETIME,
        meta_score INTEGER,
        headings_score INTEGER,
        images_score INTEGER,
        overall_score INTEGER,
        results TEXT
      )
    `);

    // Crear tabla keywords
    db.run(`
      CREATE TABLE IF NOT EXISTS keywords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT NOT NULL,
        language TEXT DEFAULT 'es',
        country TEXT DEFAULT 'ES',
        volume INTEGER,
        difficulty INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    `);

    // Crear tabla keyword_tracking
    db.run(`
      CREATE TABLE IF NOT EXISTS keyword_tracking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword_id INTEGER,
        url TEXT NOT NULL,
        position INTEGER,
        checked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (keyword_id) REFERENCES keywords(id)
      )
    `);

    // Crear tabla reports
    db.run(`
      CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        audit_id INTEGER,
        format TEXT DEFAULT 'json',
        file_path TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (audit_id) REFERENCES audits(id)
      )
    `);

    console.log('✅ Database schema initialized');
  });
};
```

---

### 6.2 **Futuras Migraciones**

#### **v1.1 - Agregar campo `user_id`**
```sql
ALTER TABLE audits ADD COLUMN user_id INTEGER;
```

#### **v1.2 - Agregar tabla `users`**
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 7. **HELPER FUNCTIONS**

### 7.1 **Funciones del Modelo**

**Archivo:** `backend/models/database.js`

```javascript
const dbHelpers = {
  // Obtener un solo registro
  get: (sql, params = []) => {
    return new Promise((resolve, reject) => {
      db.get(sql, params, (err, row) => {
        if (err) reject(err);
        else resolve(row);
      });
    });
  },

  // Obtener todos los registros
  all: (sql, params = []) => {
    return new Promise((resolve, reject) => {
      db.all(sql, params, (err, rows) => {
        if (err) reject(err);
        else resolve(rows);
      });
    });
  },

  // Ejecutar query (INSERT, UPDATE, DELETE)
  run: (sql, params = []) => {
    return new Promise((resolve, reject) => {
      db.run(sql, params, function(err) {
        if (err) reject(err);
        else resolve({ id: this.lastID, changes: this.changes });
      });
    });
  }
};
```

---

### 7.2 **Uso de Helpers**

```javascript
const { get, all, run } = require('./backend/models/database');

// Crear auditoría
const result = await run(
  'INSERT INTO audits (url, status) VALUES (?, ?)',
  ['https://example.com', 'pending']
);

// Obtener auditoría
const audit = await get('SELECT * FROM audits WHERE id = ?', [result.id]);

// Listar auditorías
const audits = await all('SELECT * FROM audits ORDER BY created_at DESC');
```

---

## 8. **MANTENIMIENTO**

### 8.1 **Backup**
```bash
# Backup de la base de datos
sqlite3 data/seo-assistant.db ".backup data/backup.db"

# O simplemente copiar el archivo
cp data/seo-assistant.db data/backup-$(date +%Y%m%d).db
```

---

### 8.2 **Vacuum**
```sql
-- Optimizar base de datos
VACUUM;

-- Analizar y optimizar índices
ANALYZE;
```

---

### 8.3 **Ver Tamaño**
```bash
# Tamaño del archivo
ls -lh data/seo-assistant.db

# Tamaño de cada tabla
sqlite3 data/seo-assistant.db "
SELECT 
  name,
  SUM(pgsize) as size
FROM dbstat
GROUP BY name
ORDER BY size DESC;
"
```

---

## 9. **TESTING**

### 9.1 **Setup para Tests**
```javascript
// tests/setup.js
const sqlite3 = require('sqlite3').verbose();
const testDb = new sqlite3.Database(':memory:');

// Inicializar schema para tests
// (mismo código que initDatabase())
```

---

### 9.2 **Limpiar DB entre Tests**
```javascript
afterEach(async () => {
  await run('DELETE FROM audits');
  await run('DELETE FROM keywords');
  await run('DELETE FROM keyword_tracking');
  await run('DELETE FROM reports');
});
```

---

## 📊 **ESTADÍSTICAS**

### **Tablas:** 4
- `audits` - Tabla principal
- `keywords` - Keywords investigadas
- `keyword_tracking` - Tracking de posiciones
- `reports` - Reportes generados

### **Relaciones:** 2
- `audits` → `reports` (1:N)
- `keywords` → `keyword_tracking` (1:N)

### **Índices:** 5
- Por URL, status, fecha
- Por keyword
- Por tracking

---

**Última actualización:** 14 de Octubre de 2025  
**Documentación relacionada:** `API_SPECIFICATION.md`, `GETTING_STARTED_DEV.md`

