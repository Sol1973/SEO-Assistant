#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Investigación de Keywords en CATALÁN
Análisis de palabras clave en catalán para SEO local en Tarragona
"""

import json
from datetime import datetime

# Keywords en catalán para Tarragona
keywords_catalan = {
    "primarias": [
        {
            "keyword": "cuidadora persones grans tarragona",
            "traduccion": "cuidadora personas mayores tarragona",
            "volumen_estimado": "100-200",
            "dificultad": "Media",
            "intencion": "Búsqueda local de servicios",
            "cpc_estimado": "€2.50-€5.00",
            "prioridad": "ALTA",
            "nota": "Keyword principal en catalán"
        },
        {
            "keyword": "cuidadora gent gran tarragona",
            "traduccion": "cuidadora gente mayor tarragona",
            "volumen_estimado": "80-150",
            "dificultad": "Media",
            "intencion": "Búsqueda local (variante)",
            "cpc_estimado": "€2.00-€4.00",
            "prioridad": "ALTA",
            "nota": "Variante común en catalán"
        },
        {
            "keyword": "tècnic sociosanitari tarragona",
            "traduccion": "técnico sociosanitario tarragona",
            "volumen_estimado": "20-50",
            "dificultad": "Baja",
            "intencion": "Búsqueda de profesionales",
            "cpc_estimado": "€1.50-€3.00",
            "prioridad": "MEDIA",
            "nota": "Profesión específica"
        },
        {
            "keyword": "atenció domiciliària tarragona",
            "traduccion": "atención domiciliaria tarragona",
            "volumen_estimado": "60-120",
            "dificultad": "Media",
            "intencion": "Búsqueda de servicios",
            "cpc_estimado": "€2.50-€5.00",
            "prioridad": "ALTA",
            "nota": "Servicio específico"
        },
        {
            "keyword": "cuidadora a domicili tarragona",
            "traduccion": "cuidadora a domicilio tarragona",
            "volumen_estimado": "50-100",
            "dificultad": "Media",
            "intencion": "Búsqueda específica de servicio",
            "cpc_estimado": "€2.00-€4.00",
            "prioridad": "ALTA",
            "nota": "Búsqueda transaccional"
        },
        {
            "keyword": "auxiliar geriatria tarragona",
            "traduccion": "auxiliar geriatría tarragona",
            "volumen_estimado": "40-80",
            "dificultad": "Media",
            "intencion": "Búsqueda profesional",
            "cpc_estimado": "€2.00-€4.00",
            "prioridad": "MEDIA",
            "nota": "Sinónimo profesional"
        }
    ],
    
    "long_tail": [
        {
            "keyword": "cuidadora persones grans a domicili tarragona",
            "traduccion": "cuidadora personas mayores a domicilio tarragona",
            "volumen_estimado": "30-60",
            "dificultad": "Baja",
            "intencion": "Transaccional específica",
            "cpc_estimado": "€3.00-€6.00",
            "prioridad": "ALTA",
            "tipo_contenido": "Página de servicio"
        },
        {
            "keyword": "cura de persones dependents tarragona",
            "traduccion": "cuidado de personas dependientes tarragona",
            "volumen_estimado": "20-40",
            "dificultad": "Baja",
            "intencion": "Búsqueda de servicios especializados",
            "cpc_estimado": "€2.50-€5.00",
            "prioridad": "MEDIA",
            "tipo_contenido": "Página de servicio"
        },
        {
            "keyword": "què fa un tècnic sociosanitari",
            "traduccion": "qué hace un técnico sociosanitario",
            "volumen_estimado": "50-100",
            "dificultad": "Baja",
            "intencion": "Informacional",
            "cpc_estimado": "€0.50-€1.00",
            "prioridad": "MEDIA",
            "tipo_contenido": "Blog educativo"
        },
        {
            "keyword": "atenció sociosanitària a domicili tarragona",
            "traduccion": "atención sociosanitaria a domicilio tarragona",
            "volumen_estimado": "15-30",
            "dificultad": "Baja",
            "intencion": "Transaccional",
            "cpc_estimado": "€2.00-€4.00",
            "prioridad": "MEDIA",
            "tipo_contenido": "Página de servicio"
        }
    ],
    
    "preguntas_frecuentes": [
        {
            "pregunta": "Què és un tècnic sociosanitari?",
            "traduccion": "¿Qué es un técnico sociosanitario?",
            "volumen_estimado": "100-200",
            "dificultad": "Baja",
            "tipo": "Definición",
            "prioridad": "ALTA",
            "donde_usar": "FAQ, Blog, Sobre Mí"
        },
        {
            "pregunta": "Quant cobra una cuidadora a Tarragona?",
            "traduccion": "¿Cuánto cobra una cuidadora en Tarragona?",
            "volumen_estimado": "80-150",
            "dificultad": "Media",
            "tipo": "Precio",
            "prioridad": "ALTA",
            "donde_usar": "Página de servicios, Blog"
        },
        {
            "pregunta": "Com trobar cuidadora a Tarragona?",
            "traduccion": "¿Cómo encontrar cuidadora en Tarragona?",
            "volumen_estimado": "50-100",
            "dificultad": "Baja",
            "tipo": "Local",
            "prioridad": "ALTA",
            "donde_usar": "Todas las páginas"
        },
        {
            "pregunta": "Diferència entre cuidadora i tècnic sociosanitari?",
            "traduccion": "¿Diferencia entre cuidadora y técnico sociosanitario?",
            "volumen_estimado": "30-60",
            "dificultad": "Baja",
            "tipo": "Comparativa",
            "prioridad": "MEDIA",
            "donde_usar": "Blog, FAQ"
        }
    ],
    
    "variantes_regionales": [
        {
            "termino": "gent gran",
            "traduccion": "gente mayor",
            "uso": "Muy común en Cataluña",
            "prioridad": "ALTA",
            "nota": "Preferido sobre 'persones grans' en contexto informal"
        },
        {
            "termino": "persones grans",
            "traduccion": "personas mayores",
            "uso": "Formal, oficial",
            "prioridad": "ALTA",
            "nota": "Usado en contextos formales y profesionales"
        },
        {
            "termino": "avis / àvies",
            "traduccion": "abuelos / abuelas",
            "uso": "Informal, familiar",
            "prioridad": "MEDIA",
            "nota": "Útil para contenido emocional"
        },
        {
            "termino": "cura",
            "traduccion": "cuidado",
            "uso": "Sustantivo",
            "prioridad": "ALTA",
            "nota": "Usado en 'cura de persones grans'"
        },
        {
            "termino": "cuidar",
            "traduccion": "cuidar",
            "uso": "Verbo",
            "prioridad": "ALTA",
            "nota": "Usado en frases de acción"
        }
    ],
    
    "comparacion_castellano_catalan": {
        "volumen_total_estimado": {
            "castellano": "1000-2000 búsquedas/mes",
            "catalan": "300-600 búsquedas/mes",
            "ratio": "30-40% del volumen castellano",
            "nota": "Catalán tiene menos volumen pero menos competencia"
        },
        "competencia": {
            "castellano": "Alta (muchas plataformas nacionales)",
            "catalan": "Media-Baja (menos competidores locales)",
            "oportunidad": "ALTA - Más fácil posicionarse en catalán"
        },
        "intencion_busqueda": {
            "castellano": "Mixta (locales + nacionales)",
            "catalan": "Principalmente local",
            "nota": "Búsquedas en catalán suelen ser de usuarios locales con mayor intención de contratar"
        }
    },
    
    "estrategia_catalan": {
        "prioridad_keywords": [
            "1. cuidadora persones grans tarragona",
            "2. cuidadora gent gran tarragona",
            "3. atenció domiciliària tarragona",
            "4. cuidadora a domicili tarragona",
            "5. tècnic sociosanitari tarragona"
        ],
        "estructura_title": {
            "recomendacion": "Cuidadora Persones Grans Tarragona | Tècnica Sociosanitària | Carmen Alvarado",
            "longitud": "< 60 caracteres",
            "nota": "Priorizar 'persones grans' sobre 'gent gran' por ser más formal"
        },
        "estructura_h1": {
            "recomendacion": "Cuidadora de Persones Grans a Tarragona | Tècnica Sociosanitària Titulada",
            "nota": "Combinar ambas keywords principales"
        },
        "meta_description": {
            "recomendacion": "Cuidadora professional i tècnica sociosanitària titulada a Tarragona. Atenció domiciliària personalitzada per a persones grans i dependents. Disponibilitat immediata.",
            "longitud": "< 160 caracteres",
            "keywords_incluidas": [
                "cuidadora professional",
                "tècnica sociosanitària",
                "tarragona",
                "atenció domiciliària",
                "persones grans",
                "dependents"
            ]
        }
    },
    
    "traducciones_clave": {
        "titulos_secciones": {
            "Sobre Mí": "Sobre Mi",
            "Servicios": "Serveis",
            "Contacto": "Contacte",
            "Te Ayudamos": "T'Ajudem",
            "Preguntas Frecuentes": "Preguntes Freqüents",
            "Por qué elegirme": "Per què triar-me",
            "Experiencia": "Experiència",
            "Formación": "Formació"
        },
        "servicios": {
            "Atención por Horas": "Atenció per Hores",
            "Media Jornada": "Mitja Jornada",
            "Jornada Completa": "Jornada Completa",
            "Atención Domiciliaria": "Atenció Domiciliària",
            "Cuidado de Personas Mayores": "Cura de Persones Grans",
            "Personas Dependientes": "Persones Dependents"
        },
        "ctas": {
            "Contacta Ahora": "Contacta Ara",
            "Llamar Ahora": "Trucar Ara",
            "Más Información": "Més Informació",
            "Solicitar Presupuesto": "Sol·licitar Pressupost",
            "Disponibilidad Inmediata": "Disponibilitat Immediata"
        }
    },
    
    "consideraciones_seo": [
        {
            "aspecto": "Hreflang",
            "implementacion": '<link rel="alternate" hreflang="es" href="https://carmenalvarado.es/" />',
            "implementacion_ca": '<link rel="alternate" hreflang="ca" href="https://carmenalvarado.es/index-ca.html" />',
            "prioridad": "ALTA",
            "nota": "Esencial para SEO multiidioma"
        },
        {
            "aspecto": "Canonical URL",
            "implementacion": "Cada versión debe tener su propio canonical",
            "ejemplo_es": '<link rel="canonical" href="https://carmenalvarado.es/" />',
            "ejemplo_ca": '<link rel="canonical" href="https://carmenalvarado.es/index-ca.html" />',
            "prioridad": "ALTA"
        },
        {
            "aspecto": "Lang attribute",
            "implementacion": '<html lang="ca">',
            "prioridad": "ALTA",
            "nota": "Cambiar de 'es' a 'ca' en versión catalana"
        },
        {
            "aspecto": "Selector de idioma",
            "implementacion": "Agregar selector visible en navegación",
            "ubicacion": "Header, esquina superior derecha",
            "formato": "ES | CA",
            "prioridad": "ALTA"
        }
    ],
    
    "archivos_a_crear": [
        {
            "archivo": "index-ca.html",
            "descripcion": "Página principal en catalán",
            "keywords_target": [
                "cuidadora persones grans tarragona",
                "tècnic sociosanitari tarragona",
                "atenció domiciliària tarragona"
            ]
        },
        {
            "archivo": "contacto-ca.html",
            "descripcion": "Página de contacto en catalán",
            "keywords_target": [
                "contacte cuidadora tarragona",
                "tècnic sociosanitari contacte"
            ]
        },
        {
            "archivo": "ayuda-ca.html",
            "descripcion": "Página Te Ayudamos en catalán",
            "keywords_target": [
                "ajuda cura persones grans",
                "consells cuidadors"
            ]
        },
        {
            "archivo": "gracias-ca.html",
            "descripcion": "Página de agradecimiento en catalán",
            "keywords_target": []
        }
    ]
}

def generar_informe():
    """Genera informe de keywords en catalán"""
    
    # Guardar JSON
    with open('keywords_catalan.json', 'w', encoding='utf-8') as f:
        json.dump(keywords_catalan, f, ensure_ascii=False, indent=2)
    
    # Generar informe de texto
    informe = []
    informe.append("=" * 80)
    informe.append("INVESTIGACIÓN DE KEYWORDS EN CATALÁN")
    informe.append(f"Fecha: {datetime.now().strftime('%d de octubre de 2025')}")
    informe.append("=" * 80)
    informe.append("")
    
    # Keywords primarias
    informe.append("🎯 KEYWORDS PRIMARIAS EN CATALÁN (Alta prioridad)")
    informe.append("-" * 80)
    for kw in keywords_catalan['primarias']:
        if kw['prioridad'] == 'ALTA':
            informe.append(f"✅ {kw['keyword']}")
            informe.append(f"   Traducción: {kw['traduccion']}")
            informe.append(f"   Volumen: {kw['volumen_estimado']} | Dificultad: {kw['dificultad']} | CPC: {kw['cpc_estimado']}")
            informe.append(f"   Nota: {kw['nota']}")
            informe.append("")
    
    # Comparación castellano-catalán
    informe.append("\n📊 COMPARACIÓN CASTELLANO vs CATALÁN")
    informe.append("-" * 80)
    comp = keywords_catalan['comparacion_castellano_catalan']
    informe.append(f"Volumen Castellano: {comp['volumen_total_estimado']['castellano']}")
    informe.append(f"Volumen Catalán: {comp['volumen_total_estimado']['catalan']}")
    informe.append(f"Ratio: {comp['volumen_total_estimado']['ratio']}")
    informe.append(f"\nCompetencia Castellano: {comp['competencia']['castellano']}")
    informe.append(f"Competencia Catalán: {comp['competencia']['catalan']}")
    informe.append(f"Oportunidad: {comp['competencia']['oportunidad']}")
    informe.append("")
    
    # Estrategia
    informe.append("\n🚀 ESTRATEGIA PARA CATALÁN")
    informe.append("-" * 80)
    est = keywords_catalan['estrategia_catalan']
    informe.append("Prioridad de Keywords:")
    for kw in est['prioridad_keywords']:
        informe.append(f"  {kw}")
    informe.append(f"\nTitle Tag Recomendado:")
    informe.append(f"  {est['estructura_title']['recomendacion']}")
    informe.append(f"\nH1 Recomendado:")
    informe.append(f"  {est['estructura_h1']['recomendacion']}")
    informe.append(f"\nMeta Description:")
    informe.append(f"  {est['meta_description']['recomendacion']}")
    informe.append("")
    
    # Archivos a crear
    informe.append("\n📁 ARCHIVOS A CREAR")
    informe.append("-" * 80)
    for archivo in keywords_catalan['archivos_a_crear']:
        informe.append(f"✅ {archivo['archivo']}")
        informe.append(f"   {archivo['descripcion']}")
        if archivo['keywords_target']:
            informe.append(f"   Keywords: {', '.join(archivo['keywords_target'])}")
        informe.append("")
    
    # Consideraciones SEO
    informe.append("\n⚙️ CONSIDERACIONES SEO MULTIIDIOMA")
    informe.append("-" * 80)
    for consideracion in keywords_catalan['consideraciones_seo']:
        informe.append(f"✅ {consideracion['aspecto']}")
        informe.append(f"   Prioridad: {consideracion['prioridad']}")
        if 'nota' in consideracion:
            informe.append(f"   Nota: {consideracion['nota']}")
        informe.append("")
    
    informe.append("\n" + "=" * 80)
    informe.append("FIN DEL INFORME")
    informe.append("=" * 80)
    
    # Guardar informe
    with open('INFORME_KEYWORDS_CATALAN.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(informe))
    
    print('\n'.join(informe))
    print("\n✅ Archivos generados:")
    print("   - keywords_catalan.json")
    print("   - INFORME_KEYWORDS_CATALAN.txt")

if __name__ == "__main__":
    generar_informe()

