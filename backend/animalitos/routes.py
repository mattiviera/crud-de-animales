# Rutas de pedido en el Navegador, tambien se conoce como CONTROLADOR
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from animalitos.dto import *
from animalitos.service import *

animal = APIRouter()

# Metodo o Controlador
@animal.get('/', response_model=List[AnimalDTO], status_code=200)
def animales():
    try:
        animales = getAnimales()
        if animales:
            return animales
        return JSONResponse(content=f'Usuarios no econtrados', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Usuarios: {e}', status_code=500)

@animal.get('/{id}', response_model=AnimalDTO, status_code=200)
def get_animal(id: int):
    try:
        animal = getAnimal(id=id)
        if animal:
            return animal
        return JSONResponse(content=f'Usuario no econtrado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al recuperar Usuario: {e}', status_code=500)

@animal.post('/', response_model=AnimalDTO, status_code=200)
def create(animalpost: CreateAnimal):
    try:
        animal_new = createAnimal(animal=animalpost)
        if animal_new:
            return animal_new
        return JSONResponse(content=f'Usuario no Creado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al Crear Usuario: {e}', status_code=500)

@animal.put('/', response_model=AnimalDTO, status_code=200)
def update(animalupdate: UpdateAnimalDTO):
    try:
        animal_update = updateAnimal(animalupdate=animalupdate)
        if animal_update:
            return animal_update
        return JSONResponse(content=f'Usuario no actualizado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al actualizar el Usuario: {e}', status_code=500)

@animal.delete('/', response_model=AnimalDTO, status_code=200)
def delete(animaldelete: DeleteAnimalDTO):
    try:
        animal_delete = deleteAnimal(animaldelete=animaldelete) 
        if animal_delete:
            return animal_delete
        return JSONResponse(content=f'Usuario no Eliminado', status_code=404)
    except Exception as e:
        return HTTPException(detail=f'Error al eliminar el Usuario: {e}', status_code=500)