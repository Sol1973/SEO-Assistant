#!/usr/bin/env python3
"""
Analizador de Competencia SEO
Herramienta para analizar competidores en los resultados de búsqueda
Fecha: 12 de octubre de 2025 (Hora Madrid)
"""

import re
from typing import List, Dict
from datetime import datetime

class CompetitorAnalyzer:
    """Analiza competidores y genera insights"""
    
    def __init__(self):
        self.competitors_national = [
            {
                "nombre": "Cuideo",
                "url": "cuideo.es",
                "tipo": "Plataforma nacional",
                "fortalezas": ["Brand reconocido", "Cobertura nacional", "App móvil"],
                "debilidades": ["Impersonal", "Comisiones altas", "Menos local"],
                "keywords_objetivo": ["cuideo tarragona", "plataforma cuidadores"]
            },
            {
                "nombre": "Cuidum",
                "url": "cuidum.com",
                "tipo": "Agregador",
                "fortalezas": ["SEO fuerte", "Contenido extenso", "Blog activo"],
                "debilidades": ["Intermediario", "Precios variables"],
                "keywords_objetivo": ["cuidum", "contratar cuidadora online"]
            },
            {
                "nombre": "Aiudo",
                "url": "aiudo.es",
                "tipo": "Marketplace",
                "fortalezas": ["Comparador", "Reseñas"],
                "debilidades": ["Comisión", "No servicio directo"],
                "keywords_objetivo": ["aiudo", "comparar cuidadoras"]
            }
        ]
        
        self.competitor_local_types = [
            "Residencias con servicio domicilio",
            "Cuidadoras freelance individuales",
            "Agencias locales pequeñas",
            "Centros de día",
            "Servicios municipales"
        ]
    
    def get_differentiation_strategy(self) -> Dict:
        """Estrategia de diferenciación vs competencia"""
        
        return {
            "ventajas_carmen": [
                {
                    "ventaja": "Trato directo sin intermediarios",
                    "beneficio": "Sin comisiones, precio transparente",
                    "keyword_asociada": "cuidadora particular tarragona",
                    "mensaje_marketing": "Trato directo, sin comisiones de plataformas"
                },
                {
                    "ventaja": "Formación dual: Enfermera + Sociosanitaria",
                    "beneficio": "Conocimientos médicos reales, no solo cuidados básicos",
                    "keyword_asociada": "cuidadora enfermera tarragona",
                    "mensaje_marketing": "Formación profesional sanitaria completa"
                },
                {
                    "ventaja": "Bilingüe Español-Catalán (B2)",
                    "beneficio": "Comunicación fluida con mayores catalanoparlantes",
                    "keyword_asociada": "cuidadora catalan tarragona",
                    "mensaje_marketing": "Atención en catalán y castellano"
                },
                {
                    "ventaja": "Experiencia internacional",
                    "beneficio": "Adaptabilidad, diferentes enfoques de cuidado",
                    "keyword_asociada": "cuidadora profesional experiencia",
                    "mensaje_marketing": "20+ años de experiencia sanitaria"
                },
                {
                    "ventaja": "Disponibilidad inmediata",
                    "beneficio": "Sin esperas, respuesta rápida a urgencias",
                    "keyword_asociada": "cuidadora urgente tarragona",
                    "mensaje_marketing": "Disponibilidad inmediata"
                },
                {
                    "ventaja": "Perfil personal, no agencia",
                    "beneficio": "Misma persona siempre, vínculo emocional",
                    "keyword_asociada": "cuidadora fija tarragona",
                    "mensaje_marketing": "Atención personalizada con la misma profesional"
                },
                {
                    "ventaja": "Zona específica Tarragona/Reus",
                    "beneficio": "Conocimiento local, cercanía",
                    "keyword_asociada": "cuidadora local tarragona",
                    "mensaje_marketing": "Profesional de Tarragona para Tarragona"
                }
            ],
            "posicionamiento": "Profesional sanitaria con formación dual que ofrece cuidado personalizado, directo y de confianza en Tarragona, sin intermediarios.",
            "target_ideal": "Familias que buscan atención de calidad, con conocimientos médicos, trato humano y precio justo.",
            "propuesta_valor": "Cuidado profesional con corazón: la experiencia de una enfermera con la calidez del trato familiar."
        }
    
    def get_content_gaps(self) -> List[Dict]:
        """Oportunidades de contenido no cubiertas por competencia"""
        
        return [
            {
                "gap": "Guías específicas para Tarragona",
                "oportunidad": "Recursos locales (centros salud, farmacias, servicios municipales)",
                "contenido_propuesto": "Guía completa de recursos para personas dependientes en Tarragona",
                "keyword": "recursos personas mayores tarragona"
            },
            {
                "gap": "Transparencia en precios",
                "oportunidad": "Competencia no muestra precios claros",
                "contenido_propuesto": "Tabla de tarifas detallada con ejemplos reales",
                "keyword": "precio cuidadora tarragona hora"
            },
            {
                "gap": "Casos de estudio reales",
                "oportunidad": "Historias de éxito anónimas",
                "contenido_propuesto": "Testimonios detallados con antes/después",
                "keyword": "experiencias cuidadora domicilio"
            },
            {
                "gap": "Contenido en catalán",
                "oportunidad": "Poco contenido SEO en catalán en el sector",
                "contenido_propuesto": "Versión completa del sitio en catalán",
                "keyword": "cuidadora persones grans tarragona"
            },
            {
                "gap": "Video personal",
                "oportunidad": "Competencia usa fotos stock, no videos reales",
                "contenido_propuesto": "Video de presentación de Carmen + tours virtuales",
                "keyword": "conocer cuidadora antes contratar"
            },
            {
                "gap": "Checklist descargables",
                "oportunidad": "Recursos prácticos para familias",
                "contenido_propuesto": "PDFs: Checklist elección cuidadora, preparar hogar, etc.",
                "keyword": "como preparar casa cuidadora"
            }
        ]
    
    def get_serp_analysis_template(self) -> str:
        """Template para analizar SERPs manualmente"""
        
        template = """
═══════════════════════════════════════════════════════════════
ANÁLISIS SERP - PLANTILLA
═══════════════════════════════════════════════════════════════

KEYWORD ANALIZADA: _________________________________________
FECHA: ____________________
UBICACIÓN: Tarragona, España
DISPOSITIVO: [ ] Desktop  [ ] Mobile

───────────────────────────────────────────────────────────────
RESULTADOS ORGÁNICOS (Top 10)
───────────────────────────────────────────────────────────────

POSICIÓN 1:
  URL: ___________________________________________________
  Title: ___________________________________________________
  Meta Description: _______________________________________
  Tipo de sitio: [ ] Directorio  [ ] Web propia  [ ] Blog  [ ] Otro: ____
  Autoridad estimada: [ ] Baja  [ ] Media  [ ] Alta
  Extensión contenido: ~_____ palabras
  Usa keyword en URL: [ ] Sí  [ ] No
  Tiene schema markup: [ ] Sí  [ ] No  [ ] No sé
  Velocidad carga: [ ] Rápida  [ ] Media  [ ] Lenta
  Diseño: [ ] Moderno  [ ] Aceptable  [ ] Anticuado
  
  NOTAS: ___________________________________________________

[Repetir para posiciones 2-10]

───────────────────────────────────────────────────────────────
FEATURED SNIPPET / POSITION ZERO
───────────────────────────────────────────────────────────────
[ ] No hay featured snippet
[ ] Párrafo  [ ] Lista  [ ] Tabla  [ ] Video

Contenido: _______________________________________________
URL que lo ocupa: ________________________________________
¿Podemos competir?: [ ] Sí  [ ] No

───────────────────────────────────────────────────────────────
LOCAL PACK (Google Maps - Top 3)
───────────────────────────────────────────────────────────────

1. ________________________  (___★ - ___ reseñas)
2. ________________________  (___★ - ___ reseñas)
3. ________________________  (___★ - ___ reseñas)

¿Aparece Carmen?: [ ] Sí  [ ] No  [ ] No tiene Google My Business

───────────────────────────────────────────────────────────────
ANUNCIOS (Google Ads)
───────────────────────────────────────────────────────────────

Número de anuncios top: ____
Número de anuncios bottom: ____

Anunciante destacado: ____________________________________
Mensaje principal: _______________________________________
Call-to-action: __________________________________________

Estimación inversión: [ ] Baja  [ ] Media  [ ] Alta

───────────────────────────────────────────────────────────────
"LA GENTE TAMBIÉN PREGUNTA"
───────────────────────────────────────────────────────────────

1. ___________________________________________________
2. ___________________________________________________
3. ___________________________________________________
4. ___________________________________________________

Oportunidad contenido: [ ] Sí  [ ] No

───────────────────────────────────────────────────────────────
BÚSQUEDAS RELACIONADAS (Pie de página)
───────────────────────────────────────────────────────────────

1. ___________________________  5. __________________________
2. ___________________________  6. __________________________
3. ___________________________  7. __________________________
4. ___________________________  8. __________________________

───────────────────────────────────────────────────────────────
ANÁLISIS Y CONCLUSIONES
───────────────────────────────────────────────────────────────

Dificultad de competir: [ ] Baja  [ ] Media  [ ] Alta

Tipo de contenido que rankea mejor:
[ ] Directorios/Listados
[ ] Webs locales individuales
[ ] Artículos informativos
[ ] Páginas comerciales directas
[ ] Otro: _________________________________________________

Extensión promedio contenido top 3: ~_____ palabras

Factores diferenciadores en top 3:
_____________________________________________________________
_____________________________________________________________

ESTRATEGIA RECOMENDADA:
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

PRIORIDAD ESTA KEYWORD: [ ] Alta  [ ] Media  [ ] Baja

═══════════════════════════════════════════════════════════════
"""
        return template
    
    def export_analysis(self, filename: str = "competitor_analysis.txt"):
        """Exporta análisis completo"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("ANÁLISIS DE COMPETENCIA - CARMEN ALVARADO\n")
            f.write("Fecha: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("="*80 + "\n\n")
            
            # Competidores nacionales
            f.write("COMPETIDORES NACIONALES\n")
            f.write("-"*80 + "\n")
            for comp in self.competitors_national:
                f.write(f"\n{comp['nombre']} ({comp['url']})\n")
                f.write(f"  Tipo: {comp['tipo']}\n")
                f.write(f"  Fortalezas: {', '.join(comp['fortalezas'])}\n")
                f.write(f"  Debilidades: {', '.join(comp['debilidades'])}\n")
                f.write(f"  Keywords: {', '.join(comp['keywords_objetivo'])}\n")
            
            # Diferenciación
            f.write("\n\n" + "="*80 + "\n")
            f.write("ESTRATEGIA DE DIFERENCIACIÓN\n")
            f.write("="*80 + "\n")
            
            diff = self.get_differentiation_strategy()
            f.write(f"\nPosicionamiento: {diff['posicionamiento']}\n")
            f.write(f"\nPropuesta de Valor: {diff['propuesta_valor']}\n")
            
            f.write("\n\nVENTAJAS COMPETITIVAS:\n")
            f.write("-"*80 + "\n")
            for i, ventaja in enumerate(diff['ventajas_carmen'], 1):
                f.write(f"\n{i}. {ventaja['ventaja']}\n")
                f.write(f"   → Beneficio: {ventaja['beneficio']}\n")
                f.write(f"   → Keyword: {ventaja['keyword_asociada']}\n")
                f.write(f"   → Mensaje: {ventaja['mensaje_marketing']}\n")
            
            # Content Gaps
            f.write("\n\n" + "="*80 + "\n")
            f.write("OPORTUNIDADES DE CONTENIDO\n")
            f.write("="*80 + "\n")
            
            for i, gap in enumerate(self.get_content_gaps(), 1):
                f.write(f"\n{i}. {gap['gap']}\n")
                f.write(f"   Oportunidad: {gap['oportunidad']}\n")
                f.write(f"   Contenido: {gap['contenido_propuesto']}\n")
                f.write(f"   Keyword: {gap['keyword']}\n")
            
            # Template SERP
            f.write("\n\n" + "="*80 + "\n")
            f.write("TEMPLATE PARA ANÁLISIS MANUAL DE SERPs\n")
            f.write("="*80 + "\n")
            f.write(self.get_serp_analysis_template())
        
        print(f"✓ Análisis exportado a {filename}")


def main():
    analyzer = CompetitorAnalyzer()
    
    print("\n" + "="*80)
    print("🔍 ANALIZADOR DE COMPETENCIA SEO")
    print("="*80 + "\n")
    
    # Estrategia de diferenciación
    diff = analyzer.get_differentiation_strategy()
    
    print("🎯 PROPUESTA DE VALOR")
    print("-"*80)
    print(diff['propuesta_valor'])
    
    print("\n\n⭐ VENTAJAS COMPETITIVAS VS GRANDES PLATAFORMAS")
    print("-"*80)
    for i, ventaja in enumerate(diff['ventajas_carmen'][:5], 1):
        print(f"\n{i}. {ventaja['ventaja']}")
        print(f"   💡 {ventaja['mensaje_marketing']}")
        print(f"   🎯 Keyword: {ventaja['keyword_asociada']}")
    
    print("\n\n📝 OPORTUNIDADES DE CONTENIDO")
    print("-"*80)
    gaps = analyzer.get_content_gaps()
    for i, gap in enumerate(gaps[:4], 1):
        print(f"\n{i}. {gap['gap']}")
        print(f"   → {gap['contenido_propuesto']}")
    
    # Exportar
    output_path = "/Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen/config/competitor_analysis.txt"
    analyzer.export_analysis(output_path)
    
    print("\n" + "="*80)
    print("✅ Análisis completado")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()

