// ============================================
// CARMEN ALVARADO - CUIDADORA PROFESIONAL
// JavaScript Principal
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // NAVEGACIÓN MÓVIL
    // ============================================
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            mobileToggle.classList.toggle('active');
        });
        
        // Cerrar menú al hacer clic en un enlace
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                mobileToggle.classList.remove('active');
            });
        });
    }
    
    // ============================================
    // SCROLL SUAVE
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ============================================
    // HEADER CON SOMBRA AL HACER SCROLL
    // ============================================
    const header = document.getElementById('header');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            header.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
        } else {
            header.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
        }
        
        lastScroll = currentScroll;
    });
    
    // ============================================
    // FAQ ACCORDION
    // ============================================
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        
        question.addEventListener('click', () => {
            // Cerrar otros items
            faqItems.forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains('active')) {
                    otherItem.classList.remove('active');
                }
            });
            
            // Toggle actual
            item.classList.toggle('active');
        });
    });
    
    // ============================================
    // FORMULARIO DE CONTACTO
    // ============================================
    const contactForm = document.getElementById('contactForm');
    const formSuccess = document.getElementById('formSuccess');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Validación básica antes de enviar
            const nombre = document.getElementById('nombre');
            const telefono = document.getElementById('telefono');
            const mensaje = document.getElementById('mensaje');
            
            // Validar solo si los campos existen
            if (nombre && telefono && mensaje) {
                if (!nombre.value || !telefono.value || !mensaje.value) {
                    e.preventDefault();
                    alert('Por favor, completa todos los campos obligatorios.');
                    return false;
                }
            }
            
            // Opcional: Enviar evento a Google Analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submission', {
                    'event_category': 'contact',
                    'event_label': 'contact_form'
                });
            }
            
            console.log('Formulario enviado a FormSubmit.co');
            
            // NO prevenir el envío - dejar que FormSubmit.co lo maneje
            // El formulario se enviará normalmente
        });
    }
    
    // ============================================
    // ANIMACIONES AL HACER SCROLL (Fade In)
    // ============================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Elementos a animar
    const animatedElements = document.querySelectorAll(
        '.service-card, .benefit-card, .testimonial-card, .blog-card, .timeline-item'
    );
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // ============================================
    // TRACKING DE CLICS EN BOTONES CTA
    // ============================================
    const ctaButtons = document.querySelectorAll('.btn-primary, .btn-secondary, [href^="tel:"]');
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonText = this.textContent.trim();
            const buttonHref = this.getAttribute('href') || 'no-link';
            
            // Google Analytics Event (si está configurado)
            if (typeof gtag !== 'undefined') {
                gtag('event', 'cta_click', {
                    'event_category': 'engagement',
                    'event_label': buttonText,
                    'value': buttonHref
                });
            }
            
            console.log('CTA clicked:', buttonText, buttonHref);
        });
    });
    
    // ============================================
    // TRACKING DE TIEMPO EN PÁGINA
    // ============================================
    let startTime = Date.now();
    
    window.addEventListener('beforeunload', function() {
        const timeSpent = Math.round((Date.now() - startTime) / 1000);
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'time_on_page', {
                'event_category': 'engagement',
                'event_label': window.location.pathname,
                'value': timeSpent
            });
        }
        
        console.log('Tiempo en página:', timeSpent, 'segundos');
    });
    
    // ============================================
    // LAZY LOADING DE IMÁGENES
    // ============================================
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // ============================================
    // DETECTAR SCROLL PROFUNDO
    // ============================================
    let scrollDepthTracked = {
        '25': false,
        '50': false,
        '75': false,
        '100': false
    };
    
    window.addEventListener('scroll', () => {
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / scrollHeight) * 100;
        
        Object.keys(scrollDepthTracked).forEach(depth => {
            if (scrolled >= parseInt(depth) && !scrollDepthTracked[depth]) {
                scrollDepthTracked[depth] = true;
                
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'scroll_depth', {
                        'event_category': 'engagement',
                        'event_label': depth + '%'
                    });
                }
                
                console.log('Scroll depth:', depth + '%');
            }
        });
    });
    
    // ============================================
    // WHATSAPP CLICK TRACKING
    // ============================================
    const whatsappButton = document.querySelector('.whatsapp-float');
    if (whatsappButton) {
        whatsappButton.addEventListener('click', function() {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'whatsapp_click', {
                    'event_category': 'contact',
                    'event_label': 'floating_button'
                });
            }
            console.log('WhatsApp button clicked');
        });
    }
    
    // ============================================
    // PHONE CALL TRACKING
    // ============================================
    const phoneButtons = document.querySelectorAll('a[href^="tel:"]');
    phoneButtons.forEach(button => {
        button.addEventListener('click', function() {
            const phoneNumber = this.getAttribute('href').replace('tel:', '');
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'phone_call', {
                    'event_category': 'contact',
                    'event_label': phoneNumber
                });
            }
            
            console.log('Phone call initiated:', phoneNumber);
        });
    });
    
    // ============================================
    // EMAIL CLICK TRACKING
    // ============================================
    const emailButtons = document.querySelectorAll('a[href^="mailto:"]');
    emailButtons.forEach(button => {
        button.addEventListener('click', function() {
            const email = this.getAttribute('href').replace('mailto:', '');
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'email_click', {
                    'event_category': 'contact',
                    'event_label': email
                });
            }
            
            console.log('Email link clicked:', email);
        });
    });
    
    // ============================================
    // MOSTRAR/OCULTAR BOTÓN BACK TO TOP (opcional)
    // ============================================
    const backToTopButton = document.getElementById('backToTop');
    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTopButton.style.display = 'flex';
            } else {
                backToTopButton.style.display = 'none';
            }
        });
        
        backToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // ============================================
    // PREVENIR SPAM EN FORMULARIO (Desactivado - FormSubmit maneja esto)
    // ============================================
    // FormSubmit.co ya incluye protección anti-spam con honeypot
    
    // ============================================
    // CONSOLE LOG - DESARROLLO
    // ============================================
    console.log('%c👋 Web Carmen Alvarado - Cuidadora Profesional', 'color: #2c7da0; font-size: 16px; font-weight: bold;');
    console.log('%cSi necesitas ayuda, llama al 611 230 547', 'color: #f77f00; font-size: 14px;');
    
});

// ============================================
// FUNCIONES AUXILIARES
// ============================================

// Función para formatear número de teléfono
function formatPhoneNumber(phone) {
    return phone.replace(/\D/g, '').replace(/(\d{3})(\d{3})(\d{3})/, '$1 $2 $3');
}

// Función para validar email
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Función para validar teléfono español
function isValidSpanishPhone(phone) {
    const re = /^[6789]\d{8}$/;
    return re.test(phone.replace(/\s/g, ''));
}

// ============================================
// EXPORTAR FUNCIONES (si se necesitan en otros scripts)
// ============================================
window.CarmenWeb = {
    formatPhoneNumber,
    isValidEmail,
    isValidSpanishPhone
};

