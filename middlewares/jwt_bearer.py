from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token
from fastapi.security import HTTPBearer

#Clase para obtener las credenciales y validar token
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):#Acceder a la peticion
        auth = await super().__call__(request)#Desde mi clase superior "HTTPBearer" llamar la clase __call__
        data = validate_token(auth.credentials)
        if data['email']!='admin@gmail.com':
            return HTTPException(status_code=403, detail="Credenciales son invalidas")