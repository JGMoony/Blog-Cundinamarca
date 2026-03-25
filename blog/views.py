from django.shortcuts import render
import json

def index(request):
    kpis = [
        {
            "municipio": "Soacha",
            "empresas": 25,
            "ventas_totales": "Alto",
            "ticket_promedio": "Medio",
            "viabilidad": 92.5
        },
        {
            "municipio": "Chía",
            "empresas": 15,
            "ventas_totales": "Medio",
            "ticket_promedio": "Alto",
            "viabilidad": 85.3
        },
        {
            "municipio": "Zipaquirá",
            "empresas": 10,
            "ventas_totales": "Medio",
            "ticket_promedio": "Medio",
            "viabilidad": 78.2
        }
    ]

    resumen = [
        {"titulo": "21+", "texto": "Municipios analizados"},
        {"titulo": "370+", "texto": "Registros de prueba"},
        {"titulo": "12", "texto": "Tablas principales"},
        {"titulo": "11", "texto": "Vistas analíticas"},
    ]

    chart_labels = ["Soacha", "Chía", "Zipaquirá"]
    chart_empresas = [25, 15, 10]
    chart_viabilidad = [92.5, 85.3, 78.2]

    contexto = {
        "titulo_blog": "Electrónicos Cundinamarca",
        "subtitulo": "Análisis descriptivo para la localización óptima de tiendas electrónicas en 2026",
        "kpis": kpis,
        "resumen": resumen,
        "chart_labels": json.dumps(chart_labels),
        "chart_empresas": json.dumps(chart_empresas),
        "chart_viabilidad": json.dumps(chart_viabilidad),
    }

    return render(request, "blog/index.html", contexto)