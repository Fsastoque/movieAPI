from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

auth_router = APIRouter()

@auth_router.post('/login',tags=['auth'], status_code=200)
def login(user:User):
   if(user.email=="admin@gmail.com" and user.password=="admin")   :
        token = create_token(user.model_dump()).decode('utf-8')
        return JSONResponse(status_code=200, content=token) 

