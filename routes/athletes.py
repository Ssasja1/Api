from fastapi import APIRouter, Depends, HTTPException
from app.models import modelAtleta
from app.middlewares import BearerJWT
from typing import List

router = APIRouter()

atletas = []

@router.get('/atletas', dependencies=[Depends(BearerJWT())], response_model=List[modelAtleta], tags=['Atletas'])
def obtener_atletas():
    return atletas

@router.post('/atletas', dependencies=[Depends(BearerJWT())], response_model=modelAtleta, tags=['Atletas'])
def crear_atleta(atleta: modelAtleta):
    atletas.append(atleta)
    return atleta