# 🚨 PROBLEMA: Footer de WordPress no se puede ocultar

**Fecha:** 13 de octubre de 2025, 09:50 (Madrid)  
**Sitio:** https://carmenalvarado.es  
**Problema:** No se pueden ocultar las columnas "Acerca de", "Privacidad" y "Social" del footer

---

## 📋 DESCRIPCIÓN DEL PROBLEMA

El sitio web de Carmen Alvarado (carmenalvarado.es) está usando el tema **Twenty Twenty-Five** de WordPress. El footer muestra 4 columnas:

1. ✅ **Carmen Alvarado** (Cuidadora Profesional en Tarragona) - QUEREMOS MANTENER
2. ❌ **Acerca de** (Equipo, Historia, Carreras) - QUEREMOS OCULTAR
3. ❌ **Privacidad** (Política de privacidad, Términos, Contacta) - QUEREMOS OCULTAR
4. ❌ **Social** (Facebook, Instagram, Twitter/X) - QUEREMOS OCULTAR

**Objetivo:** Mostrar solo la primera columna con "Carmen Alvarado" y "Cuidadora Profesional en Tarragona" centrada.

---

## 🔍 ANÁLISIS TÉCNICO

### Estructura HTML del Footer (líneas 283-377 del código fuente):

```html
<footer class="wp-block-template-part">
  <div class="wp-block-group has-global-padding is-layout-constrained">
    <div class="wp-block-columns alignwide is-layout-flex wp-container-core-columns-is-layout-28f84493">
      
      <!-- COLUMNA 1: Carmen Alvarado (MANTENER) -->
      <div class="wp-block-column is-layout-flow" style="flex-basis:30%">
        <div class="wp-block-group is-vertical is-layout-flex">
          <p class="wp-block-site-title">Carmen Alvarado</p>
          <p class="wp-block-site-tagline">Cuidadora Profesional en Tarragona</p>
        </div>
      </div>
      
      <!-- COLUMNA 2: Vacía (20%) -->
      <div class="wp-block-column is-layout-flow" style="flex-basis:20%">
      </div>
      
      <!-- COLUMNA 3: Acerca de, Privacidad, Social (OCULTAR) -->
      <div class="wp-block-column is-layout-flow" style="flex-basis:50%">
        <div class="wp-block-group is-content-justification-space-between">
          <!-- Acerca de -->
          <div class="wp-block-group is-vertical">
            <h2>Acerca de</h2>
            <nav>...</nav>
          </div>
          <!-- Privacidad -->
          <div class="wp-block-group is-vertical">
            <h2>Privacidad</h2>
            <nav>...</nav>
          </div>
          <!-- Social -->
          <div class="wp-block-group is-vertical">
            <h2>Social</h2>
            <nav>...</nav>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</footer>
```

### Plugins Activos:
- **LiteSpeed Cache 7.5.0.1** (Sistema de caché agresivo)
- **WPForms Lite 1.9.8.1**
- **WP Mail SMTP 4.6.0**
- **Hostinger Reach**

### Tema:
- **Twenty Twenty-Five** (Tema de bloques de WordPress 6.8.3)

---

## 🛠️ INTENTOS DE SOLUCIÓN (TODOS FALLARON)

### 1. ❌ CSS en `style.css` del tema
**Intento:** Añadir CSS al archivo `wp-content/themes/twentytwentyfive/style.css`

```css
/* CSS para ocultar footer */
.wp-block-columns .wp-block-column:nth-child(2),
.wp-block-columns .wp-block-column:nth-child(3) {
    display: none !important;
}

.wp-block-columns .wp-block-column:first-child {
    flex-basis: 100% !important;
    max-width: 100% !important;
    text-align: center !important;
}
```

**Resultado:** ❌ No funcionó. El CSS no se aplicó.

---

### 2. ❌ CSS con selector más específico
**Intento:** Usar `footer` como prefijo para mayor especificidad

```css
footer .wp-block-columns .wp-block-column:nth-child(2),
footer .wp-block-columns .wp-block-column:nth-child(3) {
    display: none !important;
}
```

**Resultado:** ❌ No funcionó.

---

### 3. ❌ CSS específico por página (page-id)
**Intento:** Aplicar CSS solo a la página de contacto (ID: 10)

```css
body.page-id-10 .wp-block-columns .wp-block-column:nth-child(2),
body.page-id-10 .wp-block-columns .wp-block-column:nth-child(3) {
    display: none !important;
}
```

**Resultado:** ❌ No funcionó.

---

### 4. ❌ Purgar caché de LiteSpeed
**Intento:** Eliminar todos los archivos de caché

```bash
wp cache flush
wp litespeed-purge all
rm -rf wp-content/cache/*
rm -rf wp-content/litespeed/*
```

**Resultado:** ❌ El caché se limpió, pero el CSS seguía sin aplicarse.

---

### 5. ❌ CSS en WordPress Customizer (Additional CSS)
**Intento:** Añadir CSS desde `Apariencia -> Personalizar -> CSS adicional`

**Problema encontrado:** El usuario reportó que el editor de bloques no guardaba los cambios. Error: "Revisar 1 cambio" pero no se guardaba.

**Resultado:** ❌ No se pudo guardar el CSS.

---

### 6. ❌ Crear `footer.php` personalizado
**Intento:** Crear un archivo `footer.php` en el tema con footer simplificado

```php
<?php
// Footer simplificado
?>
<footer>
    <div style="text-align: center;">
        <h3>Carmen Alvarado</h3>
        <p>Cuidadora Profesional en Tarragona</p>
    </div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
```

**Resultado:** ❌ El tema Twenty Twenty-Five usa templates de bloques, no archivos PHP tradicionales.

---

### 7. ❌ Crear `functions.php` con CSS inline
**Intento:** Añadir CSS directamente al `<head>` mediante `wp_head` hook

```php
<?php
function ocultar_footer_css() {
    echo '<style>
    .wp-block-columns .wp-block-column:nth-child(2),
    .wp-block-columns .wp-block-column:nth-child(3) {
        display: none !important;
    }
    </style>';
}
add_action('wp_head', 'ocultar_footer_css');
```

**Resultado:** ❌ No funcionó. El CSS no se aplicó.

---

### 8. ❌ Editar template del footer directamente
**Intento:** Crear `wp-content/themes/twentytwentyfive/template-parts/footer.html`

**Resultado:** ❌ No se pudo encontrar el archivo del template porque el tema usa el editor de sitio completo (FSE).

---

## 🔍 DIAGNÓSTICO

### Posibles causas del problema:

1. **Tema de bloques (FSE - Full Site Editing):**
   - Twenty Twenty-Five usa el sistema de bloques de WordPress
   - Los templates están en la base de datos, no en archivos PHP
   - No respeta archivos PHP tradicionales como `footer.php`

2. **LiteSpeed Cache:**
   - Caché muy agresivo que puede estar sirviendo versiones antiguas
   - Aunque se purgó varias veces, puede haber caché en múltiples niveles

3. **CSS no se está cargando:**
   - El archivo `style.css` del tema puede no estar siendo leído
   - El tema puede estar usando CSS compilado o minificado

4. **Editor de bloques con problemas:**
   - El usuario reportó que no puede guardar cambios en el editor de bloques
   - Error: "Revisar 1 cambio" pero no guarda

5. **Especificidad CSS:**
   - Puede haber CSS inline con mayor especificidad
   - Los estilos del tema pueden tener `!important` en múltiples lugares

---

## 💡 PROPUESTAS DE SOLUCIÓN

### Opción 1: Editar el Footer desde el Editor de Sitio (RECOMENDADA)
**Dónde:** `Apariencia -> Editor -> Patrones -> Footer`

**Pasos:**
1. Ir a `wp-admin/site-editor.php?postType=wp_template_part&postId=twentytwentyfive//footer`
2. Editar el template del footer directamente
3. Eliminar las columnas "Acerca de", "Privacidad" y "Social"
4. Dejar solo la columna de "Carmen Alvarado"
5. Guardar cambios

**Ventajas:**
- ✅ Solución nativa de WordPress
- ✅ No requiere código
- ✅ Cambios permanentes

**Desventajas:**
- ⚠️ Requiere acceso al editor de bloques (que actualmente tiene problemas)

---

### Opción 2: Usar un Child Theme
**Qué hacer:** Crear un tema hijo de Twenty Twenty-Five

**Pasos:**
1. Crear directorio `wp-content/themes/twentytwentyfive-child/`
2. Crear `style.css` con:
   ```css
   /*
   Theme Name: Twenty Twenty-Five Child
   Template: twentytwentyfive
   */
   
   .wp-block-columns .wp-block-column:nth-child(2),
   .wp-block-columns .wp-block-column:nth-child(3) {
       display: none !important;
   }
   ```
3. Crear `functions.php` para cargar el CSS
4. Activar el tema hijo

**Ventajas:**
- ✅ Cambios no se perderán con actualizaciones del tema
- ✅ Más control sobre el CSS

**Desventajas:**
- ⚠️ Requiere crear estructura de tema hijo
- ⚠️ Puede no funcionar si el problema es de especificidad CSS

---

### Opción 3: Plugin de CSS personalizado
**Qué hacer:** Instalar un plugin como "Simple Custom CSS" o "WP Add Custom CSS"

**Pasos:**
1. Instalar plugin: `wp plugin install simple-custom-css --activate`
2. Añadir CSS desde el panel del plugin
3. Purgar caché

**Ventajas:**
- ✅ Fácil de implementar
- ✅ No requiere editar archivos del tema

**Desventajas:**
- ⚠️ Añade otro plugin al sitio
- ⚠️ Puede no funcionar si el problema es de especificidad

---

### Opción 4: JavaScript para ocultar elementos (WORKAROUND)
**Qué hacer:** Usar JavaScript para ocultar las columnas después de cargar la página

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const columns = document.querySelectorAll('.wp-block-columns .wp-block-column');
    if (columns.length >= 3) {
        columns[1].style.display = 'none';
        columns[2].style.display = 'none';
        columns[0].style.flexBasis = '100%';
        columns[0].style.textAlign = 'center';
    }
});
```

**Ventajas:**
- ✅ Funciona independientemente del CSS
- ✅ Fácil de implementar

**Desventajas:**
- ❌ Los elementos se verán brevemente antes de ocultarse (flash)
- ❌ No es una solución elegante
- ❌ Problemas de SEO (los elementos siguen en el HTML)

---

### Opción 5: Cambiar de tema (ÚLTIMA OPCIÓN)
**Qué hacer:** Cambiar a un tema más simple que no use FSE

**Temas recomendados:**
- **Astra** (ligero, personalizable)
- **GeneratePress** (rápido, flexible)
- **Kadence** (moderno, con opciones de footer)

**Ventajas:**
- ✅ Mayor control sobre el diseño
- ✅ Más fácil de personalizar

**Desventajas:**
- ❌ Requiere reconfigurar todo el sitio
- ❌ Pérdida de tiempo

---

## 🎯 RECOMENDACIÓN FINAL

### Solución inmediata (URGENTE):
**Contactar con soporte de Hostinger** para que:
1. Verifiquen por qué el editor de bloques no guarda cambios
2. Editen el template del footer desde el servidor
3. Desactiven temporalmente LiteSpeed Cache para probar

### Solución a medio plazo:
1. **Crear un Child Theme** con CSS personalizado
2. **Instalar plugin de CSS** como respaldo
3. **Documentar** todos los cambios para futuras referencias

---

## 📞 INFORMACIÓN PARA SOPORTE

### Acceso SSH:
```
Usuario: u375945539@82.29.87.172
Puerto: 65002
Clave SSH: ~/.ssh/hostinger_key
```

### Comandos útiles:
```bash
# Conectar
ssh -i ~/.ssh/hostinger_key -p 65002 u375945539@82.29.87.172

# Ir al directorio del sitio
cd domains/carmenalvarado.es/public_html

# Ver tema activo
wp theme list

# Purgar caché
wp cache flush

# Ver opciones del tema
wp option get theme_mods_twentytwentyfive
```

### Archivos modificados:
- `wp-content/themes/twentytwentyfive/style.css` (CSS añadido al final)
- `wp-content/themes/twentytwentyfive/functions.php` (creado con hook wp_head)

### URLs afectadas:
- https://carmenalvarado.es/concejos/
- https://carmenalvarado.es/formulario-de-contacto/
- Todas las páginas del sitio

---

## 📝 NOTAS ADICIONALES

- El usuario no puede guardar cambios en el editor de bloques (error: "Revisar 1 cambio")
- El CSS añadido al tema no se está aplicando
- El caché se ha purgado múltiples veces sin éxito
- El tema Twenty Twenty-Five usa Full Site Editing (FSE)
- Todos los intentos de CSS (inline, archivo, específico) han fallado

---

**Preparado por:** Asistente IA  
**Para:** Soporte de Hostinger / Consultor WordPress  
**Prioridad:** Alta  
**Impacto:** Todas las páginas del sitio

