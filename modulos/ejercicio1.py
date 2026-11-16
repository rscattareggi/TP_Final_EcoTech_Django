def limpiar_registro_sensor(registro_raw):
    """
    Normaliza un registro de sensor.
    """

    sensor_id = registro_raw.get("sensor_id", "").strip()

    temperatura = registro_raw.get("temperatura", "0")
    temperatura = float(
        temperatura.replace("C", "").replace("c", "").strip()
    )

    ubicacion = registro_raw.get(
        "ubicacion",
        "Ubicación no informada"
    )

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """
    Genera alerta y promedio de temperaturas.
    """

    sensores_alerta = [
        sensor["sensor_id"]
        for sensor in lista_sensores_limpios
        if sensor["temperatura"] > umbral_temperatura
    ]

    promedio_temperatura = (
        sum(sensor["temperatura"] for sensor in lista_sensores_limpios)
        / len(lista_sensores_limpios)
    )

    return sensores_alerta, promedio_temperatura


if __name__ == "__main__":

    registros_crudos = [
        {
            "sensor_id": " SENSOR-001 ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte"
        },
        {
            "sensor_id": " SENSOR-002 ",
            "temperatura": "31.0C"
        },
        {
            "sensor_id": " SENSOR-003 ",
            "temperatura": "28.5C",
            "ubicacion": "Planta Sur"
        }
    ]

    registros_limpios = [
        limpiar_registro_sensor(r)
        for r in registros_crudos
    ]

    alertas, promedio = generar_resumen_sensores(
        registros_limpios,
        30
    )

    print("=== REPORTE SENSORES ===")
    print("Alertas:", alertas)
    print(f"Promedio: {promedio:.2f} °C")
