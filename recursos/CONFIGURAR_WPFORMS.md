# 📧 CONFIGURAR WPFORMS - Formulario de Contacto Carmen
**Fecha:** 13 de octubre de 2025  
**Plugin:** WPForms Lite  
**Objetivo:** Recibir consultas en calvarado1873@gmail.com

---

## 🎯 PASO 1: CREAR FORMULARIO (5 minutos)

### **1.1. Acceder a WPForms:**
```
1. Login: https://carmenalvarado.es/wp-admin
2. En el menú izquierdo, clic en: "WPForms" → "Añadir nuevo"
3. Te pedirá nombre del formulario:
   Nombre: "Formulario Contacto Carmen"
4. Plantilla: Seleccionar "Simple Contact Form" o "Blank Form"
```

---

## 📋 PASO 2: CONFIGURAR CAMPOS

### **2.1. Eliminar campos que no necesitas:**
```
Si elegiste "Simple Contact Form", viene con campos básicos.
Elimina los que no necesites haciendo clic en la X roja.
```

### **2.2. Agregar campos necesarios (en orden):**

**CAMPO 1: Nombre**
```
• Tipo: Single Line Text
• Label: Tu Nombre
• Required: ✓ Activado
• Placeholder: Ej: María García
```

**CAMPO 2: Teléfono**
```
• Tipo: Phone
• Label: Teléfono de Contacto
• Required: ✓ Activado
• Format: International (permite +34)
• Placeholder: Ej: 611 230 547
```

**CAMPO 3: Email**
```
• Tipo: Email
• Label: Email
• Required: ✗ Desactivado (es opcional)
• Placeholder: tu@email.com (opcional)
```

**CAMPO 4: Ciudad**
```
• Tipo: Single Line Text
• Label: Ciudad (Tarragona/Reus/Otra)
• Required: ✓ Activado
• Placeholder: Ej: Tarragona
```

**CAMPO 5: Urgencia**
```
• Tipo: Dropdown (Select)
• Label: ¿Cuándo necesitas el servicio?
• Required: ✓ Activado
• Opciones:
  - Urgente (hoy/mañana)
  - Esta semana
  - Próximo mes
  - Solo busco información
```

**CAMPO 6: Mensaje**
```
• Tipo: Paragraph Text (textarea)
• Label: Cuéntame sobre tu familiar y qué necesitas
• Required: ✓ Activado
• Placeholder: Ej: Mi madre tiene 82 años, vive sola en Tarragona y necesita ayuda con la medicación y comidas...
• Rows: 5
```

**CAMPO 7: Privacidad (GDPR)**
```
• Tipo: Checkbox
• Label: He leído y acepto la política de privacidad
• Required: ✓ Activado
• HTML personalizado en descripción:
  He leído y acepto la <a href="https://carmenalvarado.es/politica-privacidad.html" target="_blank">política de privacidad</a>
```

---

## ⚙️ PASO 3: CONFIGURAR AJUSTES

### **3.1. Pestaña "Settings" (Ajustes):**

**General:**
```
Form Name: Formulario Contacto Carmen
Form Description: (dejar vacío)
Submit Button Text: "Enviar Consulta Gratuita"
```

**Notifications (Notificaciones):**
```
1. Clic en pestaña "Notifications"

Send To Email Address:
  calvarado1873@gmail.com

Email Subject:
  Nueva Consulta Web - {field_id="1"} de {field_id="4"}

From Name:
  {field_id="1"}

From Email:
  {admin_email}

Reply-To:
  {field_id="3"}  (el campo email del formulario)

Message (Cuerpo del email):
```

```
Nueva consulta recibida desde carmenalvarado.es

═══════════════════════════════════════
DATOS DEL CLIENTE
═══════════════════════════════════════

Nombre: {field_id="1"}
Teléfono: {field_id="2"}
Email: {field_id="3"}
Ciudad: {field_id="4"}

═══════════════════════════════════════
URGENCIA
═══════════════════════════════════════

¿Cuándo necesita servicio?: {field_id="5"}

═══════════════════════════════════════
MENSAJE
═══════════════════════════════════════

{field_id="6"}

═══════════════════════════════════════

Enviado desde: carmenalvarado.es
Fecha: {date format="d/m/Y H:i"}

Responder directamente:
- Teléfono: {field_id="2"}
- Email: {field_id="3"}
```

**Confirmations (Confirmación al usuario):**
```
1. Pestaña "Confirmations"
2. Type: Message
3. Confirmation Message:

---

<h3 style="color: #2E7D9C; text-align: center;">✓ ¡Mensaje Recibido!</h3>

<p style="text-align: center; font-size: 18px;">Gracias por contactarme. Te responderé lo antes posible, normalmente en menos de 2 horas.</p>

<p style="text-align: center; font-size: 16px;">Si es <strong>urgente</strong>, llámame directamente al:</p>

<p style="text-align: center; font-size: 24px; font-weight: bold;">
<a href="tel:+34611230547" style="color: #E89B5F; text-decoration: none;">📞 611 230 547</a>
</p>

<p style="text-align: center; margin-top: 20px;">
<a href="https://carmenalvarado.es" style="background: #2E7D9C; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; display: inline-block;">← Volver al Inicio</a>
</p>

---
```

---

## 🎨 PASO 4: DISEÑO Y ESTILO

### **4.1. Pestaña "Settings" → "General":**

```
Form CSS Class:
  carmen-contact-form

Anti-spam:
  ✓ Enable Anti-spam honeypot

reCAPTCHA: (opcional, para más adelante si hay spam)
  ☐ Desactivado por ahora
```

---

## 💾 PASO 5: GUARDAR Y OBTENER SHORTCODE

```
1. Clic en botón "Save" (arriba a la derecha)
2. Aparecerá un mensaje: "Form saved"
3. Copia el SHORTCODE que aparece, ejemplo:
   [wpforms id="123"]
```

---

## 🔗 PASO 6: INTEGRAR EN TU SITIO HTML

### **Opción A: Crear Página WordPress (Recomendado)**

```
1. Páginas → Añadir nueva
2. Título: "Formulario de Contacto"
3. En el editor, pega el shortcode:
   [wpforms id="123"]
4. Publicar
5. URL quedará: https://carmenalvarado.es/formulario-de-contacto/
```

Luego actualizar el HTML del sitio para que el formulario apunte a esa URL.

### **Opción B: Integrar en index.html directamente**

Cambiar el formulario HTML actual por un iframe:

```html
<iframe 
    src="https://carmenalvarado.es/formulario-de-contacto/" 
    width="100%" 
    height="800" 
    frameborder="0"
    style="border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
</iframe>
```

### **Opción C: Plugin para shortcodes en HTML**

Instalar plugin "Shortcodes in HTML" para usar shortcodes directamente en archivos HTML.

---

## ✅ PASO 7: PROBAR EL FORMULARIO

```
1. Abrir: https://carmenalvarado.es/formulario-de-contacto/
2. Llenar todos los campos
3. Enviar
4. Verificar:
   ✓ Aparece mensaje de confirmación
   ✓ Email llega a calvarado1873@gmail.com
   ✓ Puedes responder desde el email
```

---

## 🎯 CONFIGURACIÓN AVANZADA (Opcional)

### **Agregar notificación SMS (Twilio):**
```
WPForms tiene addon para enviar SMS cuando llega consulta
Requiere cuenta Twilio (tiene costes)
```

### **Integración con Google Sheets:**
```
Plugin: WPForms Zapier Addon
O usar Zapier directamente para guardar consultas en Google Sheets
```

### **Email de respuesta automática:**
```
Settings → Notifications → Add New Notification
Type: Additional
Send To: {field_id="3"} (el email del usuario)
Subject: "Gracias por tu consulta - Carmen Alvarado"
Message: Email bonito de agradecimiento
```

---

## 📧 ALTERNATIVA: Email Directo sin Página

Si quieres que el formulario del HTML actual funcione SIN crear página WordPress:

### **Usar FormSubmit.co (Gratis, sin registro):**

```html
<form action="https://formsubmit.co/calvarado1873@gmail.com" method="POST">
    <!-- Configuración -->
    <input type="hidden" name="_subject" value="Nueva Consulta Web Carmen">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_template" value="table">
    <input type="text" name="_honey" style="display:none">
    
    <!-- Tus campos actuales -->
    <input type="text" name="nombre" required>
    <input type="tel" name="telefono" required>
    <input type="email" name="email">
    <input type="text" name="ciudad" required>
    <select name="urgencia" required>...</select>
    <textarea name="mensaje" required></textarea>
    
    <button type="submit">Enviar</button>
</form>
```

**Ventajas:**
- ✅ Gratis ilimitado
- ✅ Sin configuración
- ✅ Anti-spam incluido

**Desventajas:**
- ❌ Primera vez pide confirmar email (solo una vez)
- ❌ Dependes de servicio externo

---

## 📞 RESUMEN

### **Lo más importante:**

1. ✅ Email destino: `calvarado1873@gmail.com`
2. ✅ Asunto claro para identificar consultas
3. ✅ Todos los datos del cliente en el email
4. ✅ Confirmación al usuario que enviaste
5. ✅ Anti-spam activado

---

## 🆘 SI TIENES PROBLEMAS

### **Emails no llegan:**
```
1. Verificar carpeta SPAM de Gmail
2. Añadir remitente a contactos
3. Verificar en WPForms → Entries (se guardan aunque no llegue email)
4. Instalar plugin "WP Mail SMTP" para mejorar deliverability
```

### **Formulario no se ve bonito:**
```
1. WPForms → Settings → General
2. Form Style: Modern
3. O agregar CSS personalizado en Appearance → Customize → Additional CSS
```

---

**Documento creado:** 13/10/2025 - 01:00h Madrid  
**Tiempo estimado configuración:** 15 minutos  
**Email destino:** calvarado1873@gmail.com

