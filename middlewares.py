from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from app.genToken import validateToken


class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)

        if not isinstance(data, dict):
            raise HTTPException(status_code=401, detail="Token Inválido")

        if data.get('email') != 'fernando@example.com':
            raise HTTPException(status_code=403, detail="Credenciales no válidas")