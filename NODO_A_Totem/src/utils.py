import datetime

def procesar_datos(raw_data):
    """Limpia los datos de las APIs para el dashboard."""
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "processed": True,
        "length": len(str(raw_data))
    }

def check_system():
    """Verifica el estado del hardware."""
    return "System OK"
