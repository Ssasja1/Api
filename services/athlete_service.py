from app.models import modelAtleta

atletas = []

def agregar_atleta(atleta: modelAtleta):
    atletas.append(atleta)
    return atleta

def obtener_atletas():
    return atletas