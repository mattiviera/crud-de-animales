# Son las diferentes formas de aceptar o devolver los datos
from pydantic import BaseModel, Field

class CreateAnimal(BaseModel):
    name : str #= Field(..., description="Nombre del usuario", example="Juan")
    photo : str
    characteristic1 : str
    characteristic2 : str
    characteristic3 : str
    characteristic4 : str
    
class AnimalDTO(BaseModel):
    id: int
    name : str
    photo : str
    characteristic1 : str
    characteristic2 : str
    characteristic3 : str
    characteristic4 : str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "myuser",
                "photo": "foto.jpg",
                "characteristic1":"dato1",
                "characteristic2": "dato2",
                "characteristic3": "dato3",
                "characteristic4": "dato4"
            }
        }
            
class UpdateAnimalDTO(BaseModel):
    name : str
    photo : str
    characteristic1 : str
    characteristic2 : str
    characteristic3 : str
    characteristic4 : str
    
class DeleteAnimalDTO(BaseModel):
    id: int
    deleted : bool