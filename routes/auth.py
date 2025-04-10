from fastapi import APIRouter, HTTPException
from app.models import modelAuth
from app.genToken import createToken
from typing import List

router = APIRouter()

@router.post('/auth', tags=['Autentificacion'])
def auth(credenciales: modelAuth):
    if credenciales.mail == 'fernando@example.com' and credenciales.passw == '123456789':
        token: str = createToken(credenciales.model_dump())
        return {"Aviso:": "Token Generado"}
    else:
        return {"Aviso:": "El usuario no cuenta con permiso"}