#!/usr/bin/env python3
"""
Script para investigación de palabras clave SEO
Herramienta para analizar keywords relacionadas con cuidado de personas mayores
Fecha: 2025-10-12 (Hora Madrid)
"""

import requests
import json
from datetime import datetime
from typing import List, Dict
import time

class KeywordResearcher:
    """Herramienta para investigación de palabras clave"""
    
    def __init__(self):
        self.base_keywords = []
        self.related_keywords = []
        self.long_tail_keywords = []
        
    def generate_keyword_variations(self, base_term: str, location: str = "tarragona") -> List[str]:
        """Genera variaciones de palabras clave"""
        
        # Modificadores de intención de búsqueda
        intent_modifiers = [
            "contratar", "buscar", "necesito", "urgente", "precio", "coste",
            "mejor", "profesional", "titulada", "experiencia", "cerca de mi",
            "económica", "barata", "de confianza", "referencias", "24 horas"
        ]
        
        # Modificadores de servicio
        service_modifiers = [
            "a domicilio", "en casa", "particular", "interna", "externa",
            "por horas", "fin de semana", "nocturna", "de noche", "de día"
        ]
        
        # Modificadores de especialización
        specialty_modifiers = [
            "alzheimer", "demencia", "post-operatorio", "dependientes",
            "ancianos", "personas mayores", "tercera edad", "movilidad reducida"
        ]
        
        variations = []
        
        # Combinaciones básicas
        variations.append(f"{base_term} {location}")
        variations.append(f"{base_term} en {location}")
        
        # Con intención
        for modifier in intent_modifiers:
            variations.append(f"{modifier} {base_term} {location}")
            
        # Con servicio
        for modifier in service_modifiers:
            variations.append(f"{base_term} {modifier} {location}")
            
        # Con especialización
        for modifier in specialty_modifiers:
            variations.append(f"{base_term} {modifier} {location}")
            
        # Long-tail (3+ palabras)
        variations.append(f"cuanto cuesta {base_term} {location}")
        variations.append(f"donde contratar {base_term} {location}")
        variations.append(f"como elegir {base_term} {location}")
        
        return variations
    
    def get_primary_keywords(self) -> List[Dict]:
        """Palabras clave principales basadas en datos del sector"""
        
        return [
            {
                "keyword": "cuidadora personas mayores tarragona",
                "volume": "Alto (1000-2500/mes estimado)",
                "difficulty": "Media",
                "intent": "Comercial/Transaccional",
                "priority": "ALTA",
                "cpc_estimate": "€1.50-€3.50"
            },
            {
                "keyword": "cuidado personas mayores a domicilio tarragona",
                "volume": "Alto (800-1500/mes estimado)",
                "difficulty": "Media-Baja",
                "intent": "Transaccional",
                "priority": "ALTA",
                "cpc_estimate": "€1.80-€4.00"
            },
            {
                "keyword": "atención domiciliaria ancianos tarragona",
                "volume": "Medio (500-1000/mes estimado)",
                "difficulty": "Baja",
                "intent": "Informacional/Comercial",
                "priority": "ALTA",
                "cpc_estimate": "€1.20-€2.80"
            },
            {
                "keyword": "auxiliar geriatría tarragona",
                "volume": "Medio (300-800/mes estimado)",
                "difficulty": "Baja",
                "intent": "Comercial",
                "priority": "MEDIA",
                "cpc_estimate": "€1.00-€2.50"
            },
            {
                "keyword": "cuidadora interna tarragona",
                "volume": "Medio-Alto (600-1200/mes estimado)",
                "difficulty": "Media",
                "intent": "Transaccional",
                "priority": "MEDIA",
                "cpc_estimate": "€2.00-€4.50"
            },
            {
                "keyword": "asistencia domiciliaria mayores reus",
                "volume": "Medio (400-900/mes estimado)",
                "difficulty": "Baja",
                "intent": "Comercial",
                "priority": "MEDIA",
                "cpc_estimate": "€1.50-€3.00"
            }
        ]
    
    def get_secondary_keywords(self) -> List[Dict]:
        """Palabras clave secundarias (long-tail)"""
        
        return [
            {
                "keyword": "contratar cuidadora personas mayores tarragona",
                "volume": "Medio (200-500/mes)",
                "difficulty": "Baja",
                "priority": "MEDIA"
            },
            {
                "keyword": "precio cuidadora ancianos tarragona",
                "volume": "Medio (250-600/mes)",
                "difficulty": "Baja",
                "priority": "ALTA"
            },
            {
                "keyword": "cuidado personas dependientes tarragona",
                "volume": "Bajo-Medio (150-400/mes)",
                "difficulty": "Baja",
                "priority": "MEDIA"
            },
            {
                "keyword": "cuidadora alzheimer tarragona",
                "volume": "Bajo-Medio (100-300/mes)",
                "difficulty": "Baja",
                "priority": "MEDIA"
            },
            {
                "keyword": "cuidadora fin de semana tarragona",
                "volume": "Bajo (80-200/mes)",
                "difficulty": "Muy Baja",
                "priority": "BAJA"
            },
            {
                "keyword": "cuidadora nocturna tarragona",
                "volume": "Bajo-Medio (120-350/mes)",
                "difficulty": "Baja",
                "priority": "MEDIA"
            },
            {
                "keyword": "servicio cuidado mayores domicilio tarragona",
                "volume": "Bajo (100-250/mes)",
                "difficulty": "Muy Baja",
                "priority": "BAJA"
            }
        ]
    
    def get_informational_keywords(self) -> List[Dict]:
        """Keywords informacionales para blog/contenido SEO"""
        
        return [
            {
                "keyword": "como elegir cuidadora personas mayores",
                "volume": "Alto (1500-3000/mes nacional)",
                "intent": "Informacional - Top of funnel",
                "priority": "ALTA - BLOG"
            },
            {
                "keyword": "cuanto cuesta cuidadora personas mayores",
                "volume": "Alto (2000-4000/mes nacional)",
                "intent": "Informacional/Comercial",
                "priority": "ALTA - BLOG"
            },
            {
                "keyword": "señales necesita ayuda persona mayor",
                "volume": "Medio (500-1200/mes)",
                "intent": "Informacional",
                "priority": "MEDIA - BLOG"
            },
            {
                "keyword": "actividades estimulacion cognitiva mayores",
                "volume": "Medio-Alto (800-1800/mes)",
                "intent": "Informacional",
                "priority": "MEDIA - BLOG"
            },
            {
                "keyword": "cuidados personas alzheimer en casa",
                "volume": "Alto (1000-2500/mes)",
                "intent": "Informacional",
                "priority": "ALTA - BLOG"
            },
            {
                "keyword": "diferencia cuidadora auxiliar enfermeria",
                "volume": "Medio (400-900/mes)",
                "intent": "Informacional",
                "priority": "MEDIA - BLOG"
            }
        ]
    
    def get_local_seo_terms(self) -> List[Dict]:
        """Términos para SEO local"""
        
        return [
            {
                "term": "cuidadora tarragona",
                "location": "Tarragona capital",
                "priority": "ALTA"
            },
            {
                "term": "cuidadora reus",
                "location": "Reus",
                "priority": "ALTA"
            },
            {
                "term": "cuidadora cambrils",
                "location": "Cambrils",
                "priority": "MEDIA"
            },
            {
                "term": "cuidadora salou",
                "location": "Salou",
                "priority": "MEDIA"
            },
            {
                "term": "cuidadora vila-seca",
                "location": "Vila-seca",
                "priority": "MEDIA"
            },
            {
                "term": "cuidadora tortosa",
                "location": "Tortosa",
                "priority": "BAJA"
            }
        ]
    
    def get_competitor_keywords(self) -> List[str]:
        """Keywords de competidores típicos"""
        
        return [
            "cuideo tarragona",
            "cuideo",
            "cuidum tarragona",
            "abuelo cuidado",
            "aiudo",
            "residencia vs cuidadora domicilio"
        ]
    
    def generate_content_calendar(self) -> List[Dict]:
        """Calendario de contenido SEO para blog"""
        
        return [
            {
                "mes": "Mes 1",
                "articulo": "10 Señales de que tu Familiar Mayor Necesita Ayuda Profesional",
                "keyword_principal": "señales necesita ayuda persona mayor",
                "keywords_secundarias": ["cuando contratar cuidadora", "persona mayor necesita asistencia"],
                "tipo": "Guía completa",
                "palabras": "1200-1500"
            },
            {
                "mes": "Mes 1",
                "articulo": "Cuánto Cuesta una Cuidadora de Personas Mayores en Tarragona [2025]",
                "keyword_principal": "precio cuidadora ancianos tarragona",
                "keywords_secundarias": ["coste cuidadora", "tarifas cuidado mayores"],
                "tipo": "Guía de precios",
                "palabras": "1000-1200"
            },
            {
                "mes": "Mes 2",
                "articulo": "Cómo Elegir una Cuidadora de Confianza: Guía Completa para Familias",
                "keyword_principal": "como elegir cuidadora personas mayores",
                "keywords_secundarias": ["contratar cuidadora confianza", "referencias cuidadora"],
                "tipo": "Guía práctica",
                "palabras": "1500-1800"
            },
            {
                "mes": "Mes 2",
                "articulo": "Cuidados para Personas con Alzheimer en Casa: Guía Práctica",
                "keyword_principal": "cuidados personas alzheimer en casa",
                "keywords_secundarias": ["cuidadora alzheimer", "atención demencia domicilio"],
                "tipo": "Guía especializada",
                "palabras": "1200-1500"
            },
            {
                "mes": "Mes 3",
                "articulo": "Actividades de Estimulación Cognitiva para Personas Mayores",
                "keyword_principal": "actividades estimulacion cognitiva mayores",
                "keywords_secundarias": ["ejercicios mentales mayores", "prevenir demencia"],
                "tipo": "Guía práctica",
                "palabras": "1000-1300"
            },
            {
                "mes": "Mes 3",
                "articulo": "Cuidadora vs Residencia: ¿Qué es Mejor para tu Familiar?",
                "keyword_principal": "residencia vs cuidadora domicilio",
                "keywords_secundarias": ["ventajas cuidado domicilio", "comparativa atención mayores"],
                "tipo": "Comparativa",
                "palabras": "1200-1500"
            }
        ]
    
    def export_to_json(self, filename: str = "keyword_strategy.json"):
        """Exporta toda la estrategia a JSON"""
        
        strategy = {
            "fecha_analisis": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ubicacion_objetivo": "Tarragona, Reus y área metropolitana",
            "keywords_principales": self.get_primary_keywords(),
            "keywords_secundarias": self.get_secondary_keywords(),
            "keywords_informacionales": self.get_informational_keywords(),
            "seo_local": self.get_local_seo_terms(),
            "keywords_competencia": self.get_competitor_keywords(),
            "calendario_contenido": self.generate_content_calendar()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(strategy, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Estrategia exportada a {filename}")
        return strategy
    
    def print_summary(self):
        """Imprime resumen de la investigación"""
        
        print("\n" + "="*80)
        print("📊 INVESTIGACIÓN DE PALABRAS CLAVE - CARMEN ALVARADO")
        print("="*80 + "\n")
        
        print("🎯 KEYWORDS PRINCIPALES (Alta prioridad)")
        print("-" * 80)
        for kw in self.get_primary_keywords():
            print(f"  • {kw['keyword']}")
            print(f"    Volumen: {kw['volume']} | Dificultad: {kw['difficulty']} | CPC: {kw['cpc_estimate']}")
            print()
        
        print("\n📍 KEYWORDS LONG-TAIL (Mayor conversión)")
        print("-" * 80)
        for kw in self.get_secondary_keywords()[:5]:
            print(f"  • {kw['keyword']} - {kw['priority']}")
        
        print("\n📝 KEYWORDS PARA BLOG (SEO Contenido)")
        print("-" * 80)
        for kw in self.get_informational_keywords()[:4]:
            print(f"  • {kw['keyword']} - {kw['priority']}")
        
        print("\n📌 SEO LOCAL")
        print("-" * 80)
        for loc in self.get_local_seo_terms()[:4]:
            print(f"  • {loc['term']} ({loc['location']}) - {loc['priority']}")
        
        print("\n" + "="*80)
        print("💡 RECOMENDACIONES:")
        print("="*80)
        print("1. Usar keywords principales en títulos H1 y meta descriptions")
        print("2. Crear landing pages específicas para cada keyword principal")
        print("3. Publicar 2 artículos/mes usando keywords informacionales")
        print("4. Optimizar Google My Business con keywords locales")
        print("5. Monitorizar rankings semanalmente")
        print("="*80 + "\n")


def main():
    """Ejecuta el análisis de keywords"""
    
    researcher = KeywordResearcher()
    
    # Mostrar resumen
    researcher.print_summary()
    
    # Exportar a JSON
    strategy = researcher.export_to_json("/Users/micky/Documents/Proyectos_IA/CV_Carmen/trabajo_temporal/web_carmen/config/keyword_strategy.json")
    
    print("\n✅ Análisis completado!")
    print("\n📋 PRÓXIMOS PASOS:")
    print("  1. Verificar volúmenes en Google Keyword Planner")
    print("  2. Analizar competencia en Google Search")
    print("  3. Revisar tendencias en Google Trends")
    print("  4. Ajustar estrategia según datos reales")


if __name__ == "__main__":
    main()

