# 🔧 COMANDOS SSH MANUAL - carmenalvarado.es
**Fecha:** 12 de octubre de 2025  
**Para ejecutar MANUALMENTE en tu terminal**

---

## 🔐 CONECTAR AL SERVIDOR

### **Comando de Conexión:**
```bash
ssh -i /Users/micky/Documents/Proyectos_IA/CV_Carmen/ssh/manus_reviewer_key -p 65002 u375945539@82.29.87.172
```

Una vez dentro, verás el prompt del servidor. Ahora ejecuta estos comandos:

---

## 📍 PASO 1: VERIFICAR DOMINIOS DISPONIBLES

```bash
# Ver dónde estás
pwd

# Listar dominios
ls -la domains/

# Deberías ver:
# - restauracionhogar.es/
# - carmenalvarado.es/
# - otros...
```

---

## 📂 PASO 2: IR AL DIRECTORIO DE CARMEN

```bash
# Ir al dominio de Carmen
cd domains/carmenalvarado.es/public_html/

# Verificar que estás en el lugar correcto
pwd
# Debería mostrar: /home/u375945539/domains/carmenalvarado.es/public_html

# Ver archivos
ls -la
```

**Deberías ver:**
- `wp-config.php` (archivo de configuración WordPress)
- `wp-content/` (carpeta de contenido)
- `wp-admin/` (carpeta admin)
- `wp-includes/` (carpeta core)
- `index.php`

---

## ✅ PASO 3: VERIFICAR WORDPRESS INSTALADO

```bash
# Ver configuración WordPress
cat wp-config.php | grep "DB_"

# Deberías ver algo como:
# define('DB_NAME', 'u375945539_wpXXX');
# define('DB_USER', 'u375945539_wpXXX');
# define('DB_PASSWORD', 'xxxxx');
# define('DB_HOST', 'localhost');
```

**Guarda esta información**, la necesitarás para acceder a la BBDD.

---

## 🗄️ PASO 4: VERIFICAR BASE DE DATOS

```bash
# Conectar a MySQL (usa las credenciales de arriba)
mysql -u u375945539_wpXXX -p u375945539_wpXXX

# Te pedirá la contraseña (DB_PASSWORD de wp-config.php)
# Una vez dentro:

# Ver tablas WordPress
SHOW TABLES;

# Deberías ver estas 12 tablas:
# wp_posts
# wp_users
# wp_options
# wp_postmeta
# wp_usermeta
# wp_comments
# wp_commentmeta
# wp_terms
# wp_term_relationships
# wp_term_taxonomy
# wp_termmeta
# wp_links

# Verificar URLs correctas
SELECT option_name, option_value FROM wp_options WHERE option_name IN ('siteurl', 'home');

# DEBE mostrar:
# siteurl: https://carmenalvarado.es
# home: https://carmenalvarado.es

# Si muestra otra cosa (IP o URL temporal), actualizar:
UPDATE wp_options SET option_value='https://carmenalvarado.es' WHERE option_name='siteurl';
UPDATE wp_options SET option_value='https://carmenalvarado.es' WHERE option_name='home';

# Salir de MySQL
exit;
```

---

## 📤 PASO 5: SUBIR TUS ARCHIVOS HTML

### **Opción A: Crear carpeta personalizada**

```bash
# Estando en: /domains/carmenalvarado.es/public_html/

# Crear carpeta para tus archivos HTML estáticos
mkdir -p html_estatico

# Verificar
ls -la
```

Ahora desde tu Mac, sube los archivos:

```bash
# DESDE OTRA TERMINAL EN TU MAC (sin conectar por SSH)
cd /Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen

# Subir archivos por SCP
scp -i /Users/micky/Documents/Proyectos_IA/CV_Carmen/ssh/manus_reviewer_key -P 65002 \
  index.html ayuda.html \
  u375945539@82.29.87.172:/home/u375945539/domains/carmenalvarado.es/public_html/html_estatico/

# Subir carpetas CSS y JS
scp -i /Users/micky/Documents/Proyectos_IA/CV_Carmen/ssh/manus_reviewer_key -P 65002 -r \
  css/ js/ images/ \
  u375945539@82.29.87.172:/home/u375945539/domains/carmenalvarado.es/public_html/html_estatico/

# Subir archivos SEO
scp -i /Users/micky/Documents/Proyectos_IA/CV_Carmen/ssh/manus_reviewer_key -P 65002 \
  sitemap.xml robots.txt .htaccess \
  u375945539@82.29.87.172:/home/u375945539/domains/carmenalvarado.es/public_html/
```

### **Opción B: Usar WordPress como base y añadir páginas personalizadas**

```bash
# Estando en SSH en: /domains/carmenalvarado.es/public_html/

# Crear páginas personalizadas dentro de WordPress
mkdir -p wp-content/themes/astra-child/pages
```

Luego sube tus HTML ahí y crea templates en WordPress.

---

## 📝 PASO 6: VERIFICAR PERMISOS

```bash
# Asegurarte que WordPress puede escribir en wp-content
chmod -R 755 wp-content/
chmod -R 644 wp-content/uploads/

# Verificar propietario (debe ser tu usuario)
chown -R u375945539:u375945539 wp-content/
```

---

## 🔍 PASO 7: VERIFICAR QUE TODO FUNCIONA

```bash
# Ver logs de errores (si existen)
tail -f domains/carmenalvarado.es/logs/error.log

# O logs de Apache
tail -f /var/log/apache2/error.log

# Si no tienes acceso a logs, no te preocupes
```

---

## 📊 PASO 8: VERIFICAR DESDE WEB

Ahora desde tu navegador:

1. **WordPress Admin:**
   ```
   https://carmenalvarado.es/wp-admin
   Usuario: (el que creaste al instalar)
   ```

2. **Sitio principal:**
   ```
   https://carmenalvarado.es
   ```

3. **Archivos estáticos (si los subiste a carpeta):**
   ```
   https://carmenalvarado.es/html_estatico/index.html
   https://carmenalvarado.es/html_estatico/ayuda.html
   ```

---

## 🎯 RESUMEN DE QUÉ NECESITAS VERIFICAR:

### **En la Base de Datos:**
- [ ] Tablas WordPress existen (12 tablas)
- [ ] URLs correctas (siteurl y home = https://carmenalvarado.es)
- [ ] Usuarios admin creados

### **En el Servidor:**
- [ ] WordPress instalado en /domains/carmenalvarado.es/public_html/
- [ ] wp-config.php existe y tiene credenciales correctas
- [ ] Permisos correctos (755 para directorios, 644 para archivos)

### **Base de datos NO necesita:**
- ❌ Crear tablas manualmente (ya están)
- ❌ Modificar estructura
- ❌ Instalar plugins de BBDD especiales

**Si WordPress admin funciona, la BBDD está perfecta.**

---

## 💡 ALTERNATIVA: USO PANEL HOSTINGER (MÁS FÁCIL)

Si SSH es complicado, todo lo puedes hacer desde el panel:

### **1. Administrador de Archivos:**
```
hPanel → Archivos → Administrador de Archivos
- Navegar a public_html/
- Subir archivos
- Editar wp-config.php si necesario
```

### **2. phpMyAdmin:**
```
hPanel → Bases de datos → phpMyAdmin
- Ver todas las tablas
- Ejecutar queries SQL
- Hacer backups
```

### **3. Gestor de Archivos:**
```
hPanel → Archivos → FTP
- Descargar FileZilla
- Conectar y subir archivos gráficamente
```

---

## 📋 CHECKLIST ESPECÍFICO PARA BBDD:

Si WordPress está instalado, la BBDD ya tiene:

```sql
-- Tablas necesarias (12 base WordPress):
✓ wp_posts            - Páginas y entradas
✓ wp_postmeta         - Metadata de posts
✓ wp_users            - Usuarios
✓ wp_usermeta         - Metadata usuarios
✓ wp_options          - Configuración WP
✓ wp_comments         - Comentarios
✓ wp_commentmeta      - Metadata comentarios
✓ wp_terms            - Categorías y etiquetas
✓ wp_term_taxonomy    - Taxonomías
✓ wp_term_relationships - Relaciones terms
✓ wp_termmeta         - Metadata términos
✓ wp_links            - Enlaces (legacy)
```

**NO necesitas:**
- Crear tablas adicionales para una web básica
- Modificar estructura de tablas
- Instalar nada relacionado con BBDD

---

## 🎯 CONCLUSIÓN:

### **¿Necesitas hacer algo con BBDD? → NO**

**Si:**
- ✅ WordPress admin carga
- ✅ Puedes crear páginas
- ✅ Plugins se instalan

**Entonces:**
- ✅ La BBDD funciona perfectamente
- ✅ No toques nada de BBDD
- ✅ Solo enfócate en subir contenido

---

## 🆘 SI ALGO FALLA:

### **WordPress no carga:**
```bash
# Verificar wp-config.php
cat wp-config.php | grep DB_

# Probar conexión BBDD manualmente
mysql -u [DB_USER] -p [DB_NAME]
```

### **Error "Error establishing database connection":**
```
1. Verificar credenciales en wp-config.php
2. Verificar que base de datos existe en phpMyAdmin
3. Contactar soporte Hostinger
```

---

## 🚀 PRÓXIMO PASO:

**Una vez verificado que WordPress funciona:**

1. ✅ No toques BBDD
2. ✅ Enfócate en contenido
3. ✅ Instalar plugins desde WordPress admin
4. ✅ Subir tus páginas HTML al tema o como páginas personalizadas

---

**Documento creado:** 12 de octubre de 2025 - 23:30h (Madrid)  
**Usuario SSH:** u375945539@82.29.87.172  
**Puerto:** 65002

