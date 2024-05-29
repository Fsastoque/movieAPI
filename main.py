from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from config.database import engine, Base
from middlewares .error_handler import ErrorHandler
from routers.movies import movie_router
from routers.auth import auth_router

app = FastAPI()# se crea una instancia de fast api o aplicación

#Datos de la documentación
app.title = "Mi aplicación con FastApi"
app.version = "0.0.1"

#Añade middleware a la aplicacion
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)#Crear base de datos

#D_EXCEPTION = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid movie ID : (")
''' if not movie_to_delete:
        raise ID_EXCEPTION'''  

movies = [
        {
            "id": 1,
            "title": "Avatar",
            "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
            "year": "2009",
            "rating": 7.8,
            "category": "Acción"
        },
        {
            "id": 2,
            "title": "Titanic",
            "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
            "year": "2000",
            "rating": 7.8,
            "category": "Drama"
        }
    ]


@app.get('/',tags=['home'])#Decorador y ruta a consumir
def message():
    #return {"Hello" : "word"}
    return HTMLResponse("<h1>Hello word</h1>") 

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True ,host="0.0.0.0", port=8000, log_level="info")