from fastapi import APIRouter
from fastapi import Depends, Path, Query
from models.movie import Movie as MovieModel
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares .jwt_bearer import JWTBearer
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService
from schemas.movie import Movie

#Crea una aplicación a nivel de router
movie_router = APIRouter() 

#Variables globales
DB = Session()

#Metodo get
@movie_router.get('/movies',tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])#Decorador y ruta a consumir Depndes indica que se deje ejecutar la clase JWTBearer
def get_movies() -> List[Movie]:  
    #result = DB.query(MovieModel).all()
    result = MovieService(DB).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    #return JSONResponse(status_code=200, content=movies)

#Utilizando parametros
@movie_router.get('/movies/{id}',tags=['movies'], response_model=Movie, status_code=200) #Devolver un modelo de respuestas
def get_movie(id: int =Path(ge=1, le=2000)) -> Movie:    
    #result = DB.query(MovieModel).filter(MovieModel.id == id).first()#Obtener primer resultado
    #movie = [item for item in movies if (item['id'] == id)]
    result = MovieService(DB).get_movie(id)
    if(not result):
        return JSONResponse(status_code=404,content={"mesagge" : "No encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

#Utilizando querys
@movie_router.get('/movies/',tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=20)) -> List[Movie]:    
    #result = DB.query(MovieModel).filter(MovieModel.category == category).all()  
    #movie = list(filter(lambda item : item["category"] == category, movies))  
    result = MovieService(DB).get_movies_by_category(category)

    if(not result):
        return JSONResponse(status_code=404,content={"mesagge" : "No encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

#Metodo POST
@movie_router.post('/movies/',tags=['movies'], response_model=dict, status_code=201)
#def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
def create_movie(movie:Movie) -> dict:   
    '''movies.append({
                "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category
        })'''
    #db = Session()
    #new_movie = MovieModel(**movie.model_dump())

    #db.add(new_movie)#asigar datos a la session d ela base de datos
    #db.commit()#Guardar datos
    #movies.append(movie.model_dump())
    #movie.model_dump() convertir un modelo en diccionario

    MovieService(DB).create_movie(movie)
    return JSONResponse(status_code=201, content={"mesagge":"Se ha registrado la película"}) 

#Metodo PUT
@movie_router.put('/movies/{id}',tags=['movies'], response_model=dict, status_code=200)
#def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
def update_movie(id: int, movie:Movie) -> dict:
   try:
        #Update en la bd
        #result = DB.query(MovieModel).filter(MovieModel.id == id).first()
        result = MovieService(DB).get_movie(id)
        if(not result):
            return JSONResponse(status_code=404,content={"mesagge" : "Película no encontrada"})
        
        MovieService(DB).update_movie(id, movie)
      
        #Update en diccionario
        '''_movie = [item for item in movies if (item['id'] == id)]              
        _movie[0].update(movie) #actualizar el diccionario'''
        '''_movie[0]["title"] = movie.title            
        _movie[0]["overview"] = movie.overview
        _movie[0]["year"] = movie.year
        _movie[0]["rating"] = movie.rating
        _movie[0]["category"] = movie.category
        '''
        return JSONResponse(status_code=200, content={"mesagge":"Se ha actualizado la película"})  
   except Exception as e:        
        return JSONResponse(content={"mesagge":str(e)})  
   
#Metodo Delete
@movie_router.delete('/movies/{id}',tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) ->dict:
   try:
        #Delete en la bd
        ''' result = DB.query(MovieModel).filter(MovieModel.id == id).first()
        if(not result):
            return JSONResponse(status_code=404,content={"mesagge" : "Película no encontrada"})
        
        DB.delete(result)'''

        #Delete en diccionario
        '''movie = [item for item in movies if (item['id'] == id)] 
        movies.remove(movie[0])'''

        result = MovieService(DB).get_movie(id)
        if(not result):
            return JSONResponse(status_code=404,content={"mesagge" : "Película no encontrada"})
        
        MovieService(DB).delete_movie(id)

        return JSONResponse(status_code=200, content={"mesagge":"Se ha eliminado la película"}) 
   except Exception as e:        
        return JSONResponse(content={"mesagge":str(e)})   
