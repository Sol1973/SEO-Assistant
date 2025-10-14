# 🗄️ GUÍA BASE DE DATOS WORDPRESS - carmenalvarado.es
**Fecha:** 12 de octubre de 2025  
**Estado:** WordPress YA instalado

---

## ✅ **BUENAS NOTICIAS:**

Si WordPress ya está instalado, **la base de datos YA ESTÁ CREADA Y FUNCIONANDO**.

El auto-instalador de Hostinger ya hizo automáticamente:
- ✅ Crear base de datos MySQL
- ✅ Crear usuario de base de datos
- ✅ Configurar wp-config.php
- ✅ Instalar tablas WordPress (12 tablas base)

---

## 🔍 **¿NECESITAS HACER ALGO CON LA BBDD?**

### **Respuesta Corta: NO (en principio)**

**Si WordPress funciona, la BBDD está bien configurada.**

---

## 📊 **CUÁNDO SÍ NECESITAS TOCAR LA BBDD:**

### **1. Cambiar URL del sitio** (si estabas usando IP temporal)
### **2. Optimizar rendimiento** (más adelante)
### **3. Migrar de otro servidor** (no aplica, es nueva)
### **4. Hacer backup** (recomendado siempre)

---

## 🔧 **ACCEDER A LA BASE DE DATOS:**

### **Por phpMyAdmin (Panel Hostinger):**

```
1. Login: https://hpanel.hostinger.com
2. Buscar tu dominio: carmenalvarado.es
3. Sección "Bases de datos" o "Databases"
4. Clic en "phpMyAdmin"
5. Ya estarás dentro
```

### **Credenciales (las puedes ver en panel):**
```
Host: localhost (normalmente)
Usuario: u375945539_XXXXX (lo ves en panel)
Base de datos: u375945539_wpXXX (auto-generada)
Contraseña: (la que se generó en instalación)
```

**Estas credenciales están en:** `wp-config.php`

---

## 📋 **VERIFICAR QUE TODO ESTÁ BIEN:**

### **Opción 1: Desde WordPress Admin**

```
1. Login: https://carmenalvarado.es/wp-admin
2. Si entras → La BBDD funciona perfectamente ✅
```

### **Opción 2: Desde phpMyAdmin**

Verificar que existan estas tablas:
```
wp_posts
wp_users
wp_options
wp_postmeta
wp_usermeta
wp_comments
wp_commentmeta
wp_terms
wp_term_relationships
wp_term_taxonomy
wp_termmeta
wp_links
```

**Si existen estas 12 tablas → Todo perfecto ✅**

---

## 🎯 **LO QUE SÍ DEBERÍAS HACER AHORA:**

### **1. Verificar URL correcta en BBDD**

A veces WordPress se instala con URL temporal. Verifica:

```sql
-- Acceder a phpMyAdmin y ejecutar:
SELECT * FROM wp_options WHERE option_name IN ('siteurl', 'home');
```

**Deben mostrar:**
```
siteurl: https://carmenalvarado.es
home: https://carmenalvarado.es
```

**Si muestran otra cosa** (como IP o subdominio temporal):

```sql
UPDATE wp_options SET option_value='https://carmenalvarado.es' 
WHERE option_name='siteurl';

UPDATE wp_options SET option_value='https://carmenalvarado.es' 
WHERE option_name='home';
```

---

## 💾 **BACKUP DE BASE DE DATOS (Recomendado)**

### **Método 1: Desde phpMyAdmin (Manual)**

```
1. phpMyAdmin → Seleccionar tu base de datos
2. Pestaña "Exportar" / "Export"
3. Método: Rápido
4. Formato: SQL
5. Clic "Continuar"
6. Guardar archivo: carmenalvarado_backup_FECHA.sql
```

### **Método 2: Plugin WordPress (Automático)**

Instalar plugin: **UpdraftPlus**
```
1. Plugins → Añadir nuevo
2. Buscar "UpdraftPlus"
3. Instalar y Activar
4. Ajustes → Copias de seguridad
5. Configurar backup automático diario
6. Guardar en Google Drive o Dropbox
```

---

## 🔐 **SEGURIDAD BASE DE DATOS:**

### **Recomendaciones:**

1. **Prefijo de tablas:**
   - Por defecto: `wp_`
   - Más seguro: `wpXXX_` (Hostinger suele cambiar esto automáticamente)
   - Verificar en `wp-config.php`: `$table_prefix`

2. **Usuario de BBDD:**
   - ✅ Hostinger crea usuario único por sitio
   - ✅ No usar usuario "root"
   - ✅ Contraseña fuerte generada automáticamente

3. **Backups:**
   - ⏰ Diario (automático)
   - 💾 Guardar fuera del servidor
   - ✅ Probar restauración 1 vez al mes

---

## 🚀 **OPTIMIZACIÓN BBDD (Opcional, más adelante)**

### **Cuando tengas contenido (1-2 meses):**

```sql
-- Limpiar revisiones antiguas:
DELETE FROM wp_posts WHERE post_type = 'revision';

-- Limpiar spam:
DELETE FROM wp_comments WHERE comment_approved = 'spam';

-- Optimizar tablas:
OPTIMIZE TABLE wp_posts, wp_postmeta, wp_comments, wp_options;
```

**O usar plugin:** WP-Optimize (automático)

---

## 📊 **MONITOREO DE BBDD:**

### **Qué vigilar:**

1. **Tamaño de BBDD:**
   ```
   phpMyAdmin → Inicio
   Ver tamaño de tu base de datos
   
   Normal inicio: 1-2 MB
   Con contenido: 5-20 MB
   Si pasa 100 MB: Revisar y optimizar
   ```

2. **Conexiones:**
   ```
   Si WordPress da error "Error establishing database connection"
   → Problema de conexión BBDD
   → Verificar credenciales en wp-config.php
   → Contactar soporte Hostinger
   ```

---

## 🛠️ **COMANDOS ÚTILES SSH (Si funciona)**

### **Ver configuración MySQL:**
```bash
mysql --version
```

### **Acceder a MySQL desde terminal:**
```bash
mysql -u usuario -p nombre_base_datos
```

### **Backup desde SSH:**
```bash
mysqldump -u usuario -p nombre_base_datos > backup.sql
```

### **Restaurar backup:**
```bash
mysql -u usuario -p nombre_base_datos < backup.sql
```

---

## 📋 **CHECKLIST BBDD PARA HOY:**

### **Verificaciones Básicas:**

- [ ] WordPress admin carga correctamente
- [ ] Puedes crear/editar páginas
- [ ] URL es https://carmenalvarado.es (sin IP temporal)
- [ ] Verificar en phpMyAdmin que tablas existen

### **Configuración Importante:**

- [ ] Verificar URLs correctas en wp_options (query SQL arriba)
- [ ] Hacer primer backup manual
- [ ] Instalar UpdraftPlus para backups automáticos

### **Seguridad:**

- [ ] Verificar credenciales BBDD en wp-config.php
- [ ] Usuario BBDD no es "root"
- [ ] Contraseña BBDD es fuerte

---

## ⚠️ **PROBLEMAS COMUNES Y SOLUCIONES:**

### **1. "Error establishing database connection"**

**Causa:** Credenciales incorrectas o BBDD caída

**Solución:**
```
1. Verificar wp-config.php:
   - DB_NAME
   - DB_USER
   - DB_PASSWORD
   - DB_HOST

2. Si están bien → Panel Hostinger → Reiniciar MySQL

3. Si persiste → Soporte Hostinger
```

### **2. "Tabla no existe"**

**Causa:** Instalación incompleta

**Solución:**
```
1. phpMyAdmin → Importar
2. Buscar archivo de instalación limpia WordPress
3. O reinstalar WordPress (no pierdes archivos)
```

### **3. BBDD muy lenta**

**Causa:** No optimizada o servidor saturado

**Solución:**
```
1. Instalar plugin WP-Optimize
2. Limpiar revisiones y spam
3. Optimizar tablas
4. Considerar cache de objetos
```

---

## 🎯 **RESUMEN: ¿QUÉ HACER HOY?**

### **Si WordPress funciona:**

1. ✅ **Verificar URLs** (query SQL arriba)
2. ✅ **Hacer backup** (phpMyAdmin export)
3. ✅ **Instalar UpdraftPlus** (backups automáticos)
4. ✅ **Continuar con contenido**

### **NO necesitas:**

- ❌ Crear tablas manualmente
- ❌ Modificar estructura BBDD
- ❌ Configurar permisos (ya están)
- ❌ Instalar MySQL (ya está)

---

## 🔍 **SCRIPT DE VERIFICACIÓN BBDD:**

Te creo un script para verificar todo desde SSH...

---

## 📞 **SOPORTE:**

**Si tienes problemas con BBDD:**
- 💬 Soporte Hostinger 24/7: https://www.hostinger.es/contacto
- 📧 Email: calvarado1873@gmail.com

---

**En resumen:** Si WordPress admin funciona, la BBDD está perfecta. Solo verifica las URLs y haz backup. 🚀

---

**Documento creado:** 12 de octubre de 2025 - 23:15h (Madrid)

