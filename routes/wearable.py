from fastapi import APIRouter, Depends, HTTPException
from app.models import modelWearable
from app.middlewares import BearerJWT
from typing import List
import random
from datetime import datetime
import threading
import time

router = APIRouter()

datos_wearable = []
simulacion_activa = False

@router.post('/wearable', tags=['Wearable'])
def recibir_datos_wearable(datos: modelWearable):
    """Endpoint para recibir datos reales del wearable"""
    datos_wearable.append(datos)
    return {"mensaje": "Datos recibidos correctamente"}

@router.post('/wearable/simular', tags=['Wearable'])
def iniciar_simulacion():
    """Endpoint para iniciar la simulación automática"""
    global simulacion_activa
    
    if not simulacion_activa:
        simulacion_activa = True
        thread = threading.Thread(target=generar_datos_simulados, daemon=True)
        thread.start()
        return {"mensaje": "Simulación iniciada"}
    return {"mensaje": "La simulación ya estaba activa"}

@router.post('/wearable/detener', tags=['Wearable'])
def detener_simulacion():
    """Endpoint para detener la simulación"""
    global simulacion_activa
    simulacion_activa = False
    return {"mensaje": "Simulación detenida"}

@router.get('/wearable/datos', tags=['Wearable'])
def obtener_datos_wearable():
    """Endpoint para consultar todos los datos recibidos"""
    return datos_wearable

def generar_datos_simulados():
    """Genera datos de wearable simulados cada 5 segundos"""
    while simulacion_activa:
        # Datos normales (90% de los casos)
        if random.random() < 0.9:
            pulso = random.randint(60, 100)
            oxigenacion = random.randint(95, 99)
        # Datos anormales (10% de los casos)
        else:
            pulso = random.choice([random.randint(40, 59), random.randint(101, 140)])
            oxigenacion = random.randint(85, 94)
        
        dato_simulado = modelWearable(
            timestamp=datetime.now(),
            pulso_cardiaco=pulso,
            oxigenacion=oxigenacion,
            dispositivo_id=f"SIM-{random.randint(1000, 9999)}"
        )
        
        datos_wearable.append(dato_simulado)
        time.sleep(5)  # Intervalo entre datos