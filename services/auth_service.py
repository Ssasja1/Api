from app.models import modelAuth
from app.genToken import createToken

def authenticate_user(credenciales: modelAuth):
    if credenciales.mail == 'fernando@example.com' and credenciales.passw == '123456789':
        return createToken(credenciales.model_dump())
    return None