# 🎯 PLAN DE SOLUCIÓN: Footer WordPress

**Fecha:** 13 de octubre de 2025, 10:15 (Madrid)  
**Sitio:** https://carmenalvarado.es  
**Respuesta de Hostinger:** Problema de desarrollo del tema, no del servidor

---

## ✅ PLAN DE ACCIÓN SEGURO

### FASE 1: BACKUP COMPLETO (CRÍTICO)
```bash
# 1. Backup de la base de datos
wp db export backup_antes_footer_$(date +%Y%m%d_%H%M%S).sql

# 2. Backup de archivos del tema
tar -czf backup_tema_$(date +%Y%m%d_%H%M%S).tar.gz wp-content/themes/twentytwentyfive/

# 3. Verificar backups
ls -lh backup_*
```

---

### FASE 2: INVESTIGACIÓN DEL FOOTER

El footer en Twenty Twenty-Five puede estar en 3 lugares:

#### Opción A: Base de datos (wp_posts)
```sql
SELECT ID, post_name, post_type, post_status 
FROM wp_posts 
WHERE post_type = 'wp_template_part' 
AND post_name LIKE '%footer%';
```

#### Opción B: Archivos del tema
```bash
# Buscar archivos de footer
find wp-content/themes/twentytwentyfive -name '*footer*' -type f

# Buscar en patterns
ls wp-content/themes/twentytwentyfive/patterns/
```

#### Opción C: Theme.json
```bash
# Ver configuración del tema
cat wp-content/themes/twentytwentyfive/theme.json | grep -A 20 footer
```

---

### FASE 3: SOLUCIÓN MEDIANTE CHILD THEME (SEGURA)

**Por qué Child Theme:**
- ✅ No modifica el tema original
- ✅ Cambios permanentes
- ✅ No se pierden con actualizaciones
- ✅ Fácil de revertir

**Pasos:**

#### 1. Crear directorio del child theme
```bash
mkdir -p wp-content/themes/twentytwentyfive-child
```

#### 2. Crear style.css
```css
/*
Theme Name: Twenty Twenty-Five Child
Template: twentytwentyfive
Version: 1.0
*/

/* Ocultar columnas del footer */
footer .wp-block-columns .wp-block-column:nth-child(2),
footer .wp-block-columns .wp-block-column:nth-child(3) {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    width: 0 !important;
    height: 0 !important;
    overflow: hidden !important;
}

/* Expandir primera columna */
footer .wp-block-columns .wp-block-column:first-child {
    flex-basis: 100% !important;
    max-width: 100% !important;
    width: 100% !important;
}

/* Centrar contenido */
footer .wp-block-columns .wp-block-column:first-child .wp-block-group {
    text-align: center !important;
    justify-content: center !important;
    align-items: center !important;
    margin: 0 auto !important;
}
```

#### 3. Crear functions.php
```php
<?php
/**
 * Child Theme Functions
 */

// Cargar estilos del tema padre
function twentytwentyfive_child_enqueue_styles() {
    wp_enqueue_style('parent-style', get_template_directory_uri() . '/style.css');
    wp_enqueue_style('child-style',
        get_stylesheet_directory_uri() . '/style.css',
        array('parent-style'),
        wp_get_theme()->get('Version')
    );
}
add_action('wp_enqueue_scripts', 'twentytwentyfive_child_enqueue_styles');

// CSS adicional inline para mayor prioridad
function twentytwentyfive_child_footer_css() {
    echo '<style id="child-footer-css">
    footer .wp-block-columns .wp-block-column:nth-child(2),
    footer .wp-block-columns .wp-block-column:nth-child(3) {
        display: none !important;
    }
    footer .wp-block-columns .wp-block-column:first-child {
        flex-basis: 100% !important;
        text-align: center !important;
    }
    </style>';
}
add_action('wp_head', 'twentytwentyfive_child_footer_css', 999);
?>
```

#### 4. Activar child theme
```bash
wp theme activate twentytwentyfive-child
```

#### 5. Purgar caché
```bash
wp cache flush
rm -rf wp-content/cache/*
rm -rf wp-content/litespeed/*
```

---

### FASE 4: VERIFICACIÓN

1. **Verificar en navegador:**
   - https://carmenalvarado.es/concejos/
   - https://carmenalvarado.es/formulario-de-contacto/

2. **Verificar código fuente:**
   ```bash
   curl -s https://carmenalvarado.es/ | grep -A 50 "<footer"
   ```

3. **Verificar CSS cargado:**
   - Inspeccionar elemento en el navegador
   - Buscar `#child-footer-css` en el `<head>`

---

### FASE 5: PLAN B - JavaScript (Si CSS no funciona)

```javascript
// Añadir al functions.php
function twentytwentyfive_child_footer_js() {
    ?>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const footerColumns = document.querySelectorAll('footer .wp-block-columns .wp-block-column');
        if (footerColumns.length >= 3) {
            // Ocultar columnas 2 y 3
            footerColumns[1].remove();
            footerColumns[2].remove();
            
            // Expandir primera columna
            footerColumns[0].style.flexBasis = '100%';
            footerColumns[0].style.maxWidth = '100%';
            footerColumns[0].style.textAlign = 'center';
        }
    });
    </script>
    <?php
}
add_action('wp_footer', 'twentytwentyfive_child_footer_js', 999);
```

---

### FASE 6: PLAN C - Editar Base de Datos (ÚLTIMO RECURSO)

**⚠️ SOLO SI TODO LO DEMÁS FALLA**

```sql
-- Buscar el footer en la base de datos
SELECT ID, post_name, post_content 
FROM wp_posts 
WHERE post_type = 'wp_template_part' 
AND post_name LIKE '%footer%';

-- Editar el contenido del footer (CUIDADO)
-- Primero hacer backup de ese registro específico
```

---

## 🔄 ORDEN DE EJECUCIÓN

1. ✅ **BACKUP** (OBLIGATORIO)
2. ✅ **Investigar** dónde está el footer
3. ✅ **Crear Child Theme** (RECOMENDADO)
4. ✅ **Activar y verificar**
5. ⚠️ **Plan B (JS)** si CSS no funciona
6. 🚨 **Plan C (DB)** solo como último recurso

---

## 🛡️ MEDIDAS DE SEGURIDAD

- ✅ Backup completo antes de empezar
- ✅ Trabajar en child theme (no modificar original)
- ✅ Probar en una página primero
- ✅ Mantener acceso SSH activo
- ✅ Tener backup listo para restaurar

---

## 📝 COMANDOS DE EMERGENCIA

### Si algo sale mal:

```bash
# Revertir al tema original
wp theme activate twentytwentyfive

# Restaurar backup de base de datos
wp db import backup_antes_footer_YYYYMMDD_HHMMSS.sql

# Eliminar child theme
rm -rf wp-content/themes/twentytwentyfive-child/

# Purgar caché
wp cache flush
```

---

## ✅ CHECKLIST ANTES DE EMPEZAR

- [ ] Backup de base de datos creado
- [ ] Backup de archivos del tema creado
- [ ] Verificar que los backups se crearon correctamente
- [ ] Tener acceso SSH activo
- [ ] Tener navegador abierto para verificar cambios
- [ ] Leer todo el plan completo

---

¿Procedemos con el PLAN DE ACCIÓN SEGURO?

