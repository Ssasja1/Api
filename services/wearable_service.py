from app.models import modelWearable

datos_wearable = []

def recibir_datos_wearable(datos: modelWearable):
    datos_wearable.append(datos)
    return datos