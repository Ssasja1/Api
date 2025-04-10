from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime


class modelUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id siempre debe ser positivo.")
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios.")
    edad: int = Field(..., gt=0, le=120, description="Edad entre 1 y 120 años.")
    correo: str = Field(..., pattern=r'^[a-z0-9]+[\.]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$', description="Correo válido.")

class modelAuth(BaseModel):
    mail: EmailStr
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="La contraseña es de mínimo 8 caracteres, sólo letras sin espacios")

class modelAtleta(BaseModel):
    id: int
    nombre: str
    edad: int
    deporte: str

class modelWearable(BaseModel):
    timestamp: datetime
    pulso_cardiaco: int
    oxigenacion: int
    dispositivo_id: str