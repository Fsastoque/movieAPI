
from pydantic import BaseModel, Field
from typing import Optional

#Esquema o modelo de datos de peliculas
class Movie(BaseModel):#Hereda de BaseModel
    #id: int | None = None #Puede ser un valor opcional
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)#Validaciones adicionales
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=20)

    #Se utiliza para asignar los valores por defecto
    class Config:      
            json_schema_extra = {                    
                        "example": {
                            "id": 1,
                            "title": "Mi película",
                            "overview": "Descripción de la película",
                            "year": 2024,
                            "rating": 9.8,
                            "category": "Acción"
                        }              
            }