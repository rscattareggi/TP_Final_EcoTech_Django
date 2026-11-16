from django.shortcuts import render


def calcular_emisiones_carbono(
    consumo_kwh,
    factor_emision=0.4
):

    if consumo_kwh < 0:
        raise ValueError(
            "El consumo no puede ser negativo."
        )

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):

    emisiones_totales = 0

    planta_mayor_consumo = max(
        registros,
        key=lambda r: r["consumo"]
    )

    for registro in registros:
        emisiones_totales += calcular_emisiones_carbono(
            registro["consumo"]
        )

    return {
        "emisiones_totales": emisiones_totales,
        "planta_mayor_consumo":
            planta_mayor_consumo["planta"]
    }


def vista_panel_sustentabilidad(request):

    registros = [
        {
            "planta": "Planta Norte",
            "consumo": 1200
        },
        {
            "planta": "Planta Sur",
            "consumo": 1800
        },
        {
            "planta": "Planta Centro",
            "consumo": 950
        }
    ]

    metricas = obtener_metricas_consumo(
        registros
    )

    return render(
        request,
        "sustentabilidad/panel.html",
        metricas
    )
