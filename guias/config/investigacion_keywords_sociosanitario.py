#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Investigación de Keywords: SOCIOSANITARIO
Análisis de palabras clave relacionadas para SEO local en Tarragona
"""

import json
from datetime import datetime

# Palabras clave relacionadas con "sociosanitario" y "cuidado de personas mayores"
keywords_sociosanitario = {
    "primarias": [
        {
            "keyword": "sociosanitario tarragona",
            "volumen_estimado": "50-100",
            "dificultad": "Baja",
            "intencion": "Búsqueda local de servicios",
            "cpc_estimado": "€1.50-€3.00",
            "prioridad": "ALTA"
        },
        {
            "keyword": "técnico sociosanitario tarragona",
            "volumen_estimado": "30-70",
            "dificultad": "Baja",
            "intencion": "Búsqueda de profesionales",
            "cpc_estimado": "€1.20-€2.50",
            "prioridad": "ALTA"
        },
        {
            "keyword": "atención sociosanitaria tarragona",
            "volumen_estimado": "40-80",
            "dificultad": "Media",
            "intencion": "Búsqueda de servicios",
            "cpc_estimado": "€1.80-€3.50",
            "prioridad": "ALTA"
        },
        {
            "keyword": "cuidadora sociosanitaria tarragona",
            "volumen_estimado": "20-50",
            "dificultad": "Baja",
            "intencion": "Búsqueda específica",
            "cpc_estimado": "€1.00-€2.00",
            "prioridad": "MEDIA"
        },
        {
            "keyword": "sociosanitario reus",
            "volumen_estimado": "20-40",
            "dificultad": "Baja",
            "intencion": "Búsqueda local Reus",
            "cpc_estimado": "€1.00-€2.00",
            "prioridad": "MEDIA"
        }
    ],
    
    "long_tail": [
        {
            "keyword": "qué hace un técnico sociosanitario",
            "volumen_estimado": "200-500",
            "dificultad": "Baja",
            "intencion": "Informacional",
            "cpc_estimado": "€0.50-€1.00",
            "prioridad": "ALTA",
            "tipo_contenido": "Blog educativo"
        },
        {
            "keyword": "diferencia entre auxiliar y técnico sociosanitario",
            "volumen_estimado": "100-300",
            "dificultad": "Baja",
            "intencion": "Informacional",
            "cpc_estimado": "€0.30-€0.80",
            "prioridad": "MEDIA",
            "tipo_contenido": "Blog comparativo"
        },
        {
            "keyword": "atención sociosanitaria a domicilio tarragona",
            "volumen_estimado": "30-60",
            "dificultad": "Media",
            "intencion": "Transaccional",
            "cpc_estimado": "€2.00-€4.00",
            "prioridad": "ALTA",
            "tipo_contenido": "Página de servicio"
        },
        {
            "keyword": "cuidados sociosanitarios personas mayores tarragona",
            "volumen_estimado": "20-40",
            "dificultad": "Media",
            "intencion": "Transaccional",
            "cpc_estimado": "€2.50-€5.00",
            "prioridad": "ALTA",
            "tipo_contenido": "Página de servicio"
        },
        {
            "keyword": "técnico sociosanitario titulado tarragona",
            "volumen_estimado": "10-30",
            "dificultad": "Baja",
            "intencion": "Búsqueda de profesional cualificado",
            "cpc_estimado": "€1.50-€3.00",
            "prioridad": "MEDIA",
            "tipo_contenido": "Página sobre mí"
        },
        {
            "keyword": "curso técnico sociosanitario tarragona",
            "volumen_estimado": "100-200",
            "dificultad": "Media",
            "intencion": "Formación (no nuestro target)",
            "cpc_estimado": "€1.00-€2.00",
            "prioridad": "BAJA",
            "tipo_contenido": "No aplicable"
        }
    ],
    
    "relacionadas_servicios": [
        {
            "keyword": "cuidadora personas mayores tarragona",
            "volumen_estimado": "200-400",
            "dificultad": "Alta",
            "intencion": "Transaccional",
            "cpc_estimado": "€3.00-€6.00",
            "prioridad": "ALTA",
            "nota": "Keyword principal del sitio"
        },
        {
            "keyword": "auxiliar geriatría tarragona",
            "volumen_estimado": "100-200",
            "dificultad": "Media",
            "intencion": "Transaccional",
            "cpc_estimado": "€2.50-€5.00",
            "prioridad": "ALTA",
            "nota": "Sinónimo de sociosanitario"
        },
        {
            "keyword": "atención domiciliaria personas mayores tarragona",
            "volumen_estimado": "150-300",
            "dificultad": "Alta",
            "intencion": "Transaccional",
            "cpc_estimado": "€3.50-€7.00",
            "prioridad": "ALTA",
            "nota": "Keyword de alto valor"
        },
        {
            "keyword": "cuidado personas dependientes tarragona",
            "volumen_estimado": "80-150",
            "dificultad": "Media",
            "intencion": "Transaccional",
            "cpc_estimado": "€2.00-€4.00",
            "prioridad": "ALTA",
            "nota": "Relacionado con sociosanitario"
        },
        {
            "keyword": "asistencia personas mayores a domicilio tarragona",
            "volumen_estimado": "60-120",
            "dificultad": "Media",
            "intencion": "Transaccional",
            "cpc_estimado": "€2.50-€5.00",
            "prioridad": "MEDIA",
            "nota": "Variante de búsqueda"
        }
    ],
    
    "preguntas_frecuentes": [
        {
            "pregunta": "¿Qué es un técnico sociosanitario?",
            "volumen_estimado": "500-1000",
            "dificultad": "Baja",
            "tipo": "Definición",
            "prioridad": "ALTA",
            "donde_usar": "Blog, FAQ, Sobre Mí"
        },
        {
            "pregunta": "¿Cuánto cobra un técnico sociosanitario por hora?",
            "volumen_estimado": "200-400",
            "dificultad": "Media",
            "tipo": "Precio",
            "prioridad": "ALTA",
            "donde_usar": "Página de servicios, Blog"
        },
        {
            "pregunta": "¿Qué hace un técnico sociosanitario a domicilio?",
            "volumen_estimado": "100-200",
            "dificultad": "Baja",
            "tipo": "Informacional",
            "prioridad": "ALTA",
            "donde_usar": "Servicios, Blog"
        },
        {
            "pregunta": "¿Necesito un técnico sociosanitario o una auxiliar de enfermería?",
            "volumen_estimado": "50-100",
            "dificultad": "Baja",
            "tipo": "Comparativa",
            "prioridad": "MEDIA",
            "donde_usar": "Blog, FAQ"
        },
        {
            "pregunta": "¿Dónde encontrar técnico sociosanitario en Tarragona?",
            "volumen_estimado": "30-60",
            "dificultad": "Baja",
            "tipo": "Local",
            "prioridad": "ALTA",
            "donde_usar": "Todas las páginas (SEO local)"
        },
        {
            "pregunta": "¿Qué diferencia hay entre sociosanitario y auxiliar de geriatría?",
            "volumen_estimado": "80-150",
            "dificultad": "Baja",
            "tipo": "Comparativa",
            "prioridad": "MEDIA",
            "donde_usar": "Blog"
        }
    ],
    
    "competencia": [
        {
            "tipo": "Plataformas",
            "ejemplos": ["Cuideo", "Cuidum", "Aiudo"],
            "keywords_usan": [
                "cuidadora a domicilio",
                "cuidado personas mayores",
                "atención domiciliaria"
            ],
            "ventaja_carmen": "Trato directo, sin intermediarios, profesional titulada"
        },
        {
            "tipo": "Residencias",
            "ejemplos": ["Residencias locales"],
            "keywords_usan": [
                "residencia personas mayores tarragona",
                "centro geriátrico"
            ],
            "ventaja_carmen": "Atención personalizada en casa, más económico, entorno familiar"
        },
        {
            "tipo": "Agencias locales",
            "ejemplos": ["Agencias de cuidado"],
            "keywords_usan": [
                "agencia cuidadoras tarragona",
                "servicio cuidado mayores"
            ],
            "ventaja_carmen": "Sin comisiones, siempre la misma persona, trato personalizado"
        }
    ],
    
    "oportunidades_contenido": [
        {
            "titulo": "Qué hace un Técnico Sociosanitario: Guía Completa 2025",
            "keywords_target": [
                "qué hace un técnico sociosanitario",
                "funciones técnico sociosanitario",
                "atención sociosanitaria"
            ],
            "tipo": "Blog educativo",
            "prioridad": "ALTA",
            "longitud": "1500-2000 palabras",
            "cta": "¿Necesitas un técnico sociosanitario en Tarragona? Contacta conmigo"
        },
        {
            "titulo": "Técnico Sociosanitario vs Auxiliar de Enfermería: Diferencias",
            "keywords_target": [
                "diferencia técnico sociosanitario auxiliar enfermería",
                "sociosanitario vs auxiliar geriatría"
            ],
            "tipo": "Blog comparativo",
            "prioridad": "MEDIA",
            "longitud": "1200-1500 palabras",
            "cta": "Como técnica sociosanitaria titulada, puedo ayudarte"
        },
        {
            "titulo": "Cuánto Cuesta un Técnico Sociosanitario en Tarragona [2025]",
            "keywords_target": [
                "precio técnico sociosanitario",
                "cuánto cobra sociosanitario tarragona",
                "tarifas cuidadora profesional"
            ],
            "tipo": "Blog precios",
            "prioridad": "ALTA",
            "longitud": "1000-1500 palabras",
            "cta": "Solicita presupuesto personalizado sin compromiso"
        },
        {
            "titulo": "Atención Sociosanitaria a Domicilio: Qué Incluye",
            "keywords_target": [
                "atención sociosanitaria a domicilio",
                "servicios técnico sociosanitario casa",
                "cuidados domiciliarios"
            ],
            "tipo": "Página de servicio",
            "prioridad": "ALTA",
            "longitud": "800-1200 palabras",
            "cta": "Disponibilidad inmediata en Tarragona y Reus"
        },
        {
            "titulo": "Cómo Elegir un Técnico Sociosanitario: 10 Claves",
            "keywords_target": [
                "cómo elegir cuidadora",
                "qué buscar en técnico sociosanitario",
                "contratar cuidadora profesional"
            ],
            "tipo": "Blog guía",
            "prioridad": "MEDIA",
            "longitud": "1500-2000 palabras",
            "cta": "Conoce mi formación y experiencia"
        }
    ],
    
    "estrategia_implementacion": {
        "fase_1_inmediata": [
            "Agregar 'Técnica Sociosanitaria' en todos los títulos H1",
            "Incluir 'sociosanitario' en meta descriptions",
            "Crear sección 'Qué es un Técnico Sociosanitario' en página Sobre Mí",
            "Agregar FAQ sobre diferencias con otros profesionales"
        ],
        "fase_2_corto_plazo": [
            "Crear blog post: 'Qué hace un Técnico Sociosanitario'",
            "Crear blog post: 'Precios Técnico Sociosanitario Tarragona'",
            "Optimizar página de servicios con keyword 'atención sociosanitaria'",
            "Crear página específica: 'Técnico Sociosanitario a Domicilio Tarragona'"
        ],
        "fase_3_medio_plazo": [
            "Serie de blog posts educativos",
            "Comparativas con otros profesionales",
            "Casos de éxito y testimonios",
            "Videos explicativos (YouTube SEO)"
        ]
    }
}

def generar_informe():
    """Genera informe de keywords en formato JSON y texto"""
    
    # Guardar JSON
    with open('keywords_sociosanitario.json', 'w', encoding='utf-8') as f:
        json.dump(keywords_sociosanitario, f, ensure_ascii=False, indent=2)
    
    # Generar informe de texto
    informe = []
    informe.append("=" * 80)
    informe.append("INVESTIGACIÓN DE KEYWORDS: SOCIOSANITARIO")
    informe.append(f"Fecha: {datetime.now().strftime('%d de octubre de 2025')}")
    informe.append("=" * 80)
    informe.append("")
    
    # Keywords primarias
    informe.append("🎯 KEYWORDS PRIMARIAS (Alta prioridad)")
    informe.append("-" * 80)
    for kw in keywords_sociosanitario['primarias']:
        if kw['prioridad'] == 'ALTA':
            informe.append(f"✅ {kw['keyword']}")
            informe.append(f"   Volumen: {kw['volumen_estimado']} | Dificultad: {kw['dificultad']} | CPC: {kw['cpc_estimado']}")
            informe.append(f"   Intención: {kw['intencion']}")
            informe.append("")
    
    # Long tail
    informe.append("\n📝 KEYWORDS LONG TAIL (Contenido)")
    informe.append("-" * 80)
    for kw in keywords_sociosanitario['long_tail']:
        if kw['prioridad'] == 'ALTA':
            informe.append(f"✅ {kw['keyword']}")
            informe.append(f"   Volumen: {kw['volumen_estimado']} | Tipo: {kw.get('tipo_contenido', 'N/A')}")
            informe.append("")
    
    # Preguntas frecuentes
    informe.append("\n❓ PREGUNTAS FRECUENTES (FAQ / Blog)")
    informe.append("-" * 80)
    for q in keywords_sociosanitario['preguntas_frecuentes']:
        if q['prioridad'] == 'ALTA':
            informe.append(f"✅ {q['pregunta']}")
            informe.append(f"   Volumen: {q['volumen_estimado']} | Usar en: {q['donde_usar']}")
            informe.append("")
    
    # Oportunidades de contenido
    informe.append("\n📚 OPORTUNIDADES DE CONTENIDO")
    informe.append("-" * 80)
    for opp in keywords_sociosanitario['oportunidades_contenido']:
        if opp['prioridad'] == 'ALTA':
            informe.append(f"✅ {opp['titulo']}")
            informe.append(f"   Keywords: {', '.join(opp['keywords_target'])}")
            informe.append(f"   Tipo: {opp['tipo']} | Longitud: {opp['longitud']}")
            informe.append(f"   CTA: {opp['cta']}")
            informe.append("")
    
    # Estrategia de implementación
    informe.append("\n🚀 ESTRATEGIA DE IMPLEMENTACIÓN")
    informe.append("-" * 80)
    informe.append("\nFASE 1 - INMEDIATA:")
    for accion in keywords_sociosanitario['estrategia_implementacion']['fase_1_inmediata']:
        informe.append(f"  • {accion}")
    
    informe.append("\nFASE 2 - CORTO PLAZO (1-2 semanas):")
    for accion in keywords_sociosanitario['estrategia_implementacion']['fase_2_corto_plazo']:
        informe.append(f"  • {accion}")
    
    informe.append("\nFASE 3 - MEDIO PLAZO (1-3 meses):")
    for accion in keywords_sociosanitario['estrategia_implementacion']['fase_3_medio_plazo']:
        informe.append(f"  • {accion}")
    
    informe.append("\n" + "=" * 80)
    informe.append("FIN DEL INFORME")
    informe.append("=" * 80)
    
    # Guardar informe
    with open('INFORME_KEYWORDS_SOCIOSANITARIO.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(informe))
    
    print('\n'.join(informe))
    print("\n✅ Archivos generados:")
    print("   - keywords_sociosanitario.json")
    print("   - INFORME_KEYWORDS_SOCIOSANITARIO.txt")

if __name__ == "__main__":
    generar_informe()

