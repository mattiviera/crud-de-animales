# Contiene todas las funciones que manejan la logica de Negocio (QUE ACCIONES REALIZO con la BD)
from animalitos.entity import Animal
from config.cnx import sessionlocal
from animalitos.dto import CreateAnimal, DeleteAnimalDTO, UpdateAnimalDTO, AnimalDTO

# Devuelve todos los Usuarios Activos
def getAnimales():
    try:
        db = sessionlocal()
        animales = db.query(Animal).filter(Animal.deleted == False).all()
        if animales:
            return animales
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve todos los Usuarios Inactivos
def getAnimalesInactive():
    try:
        db = sessionlocal()
        animales = db.query(Animal).filter(Animal.deleted == True).all()
        if animales:
            return animales
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve los datos del Usuario Inactivo o Activo
def getAnimal(id: int):
    try:
        db = sessionlocal()
        animal = db.query(Animal).filter(Animal.id == id).first()
        if animal:
            return animal
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Crea un Usuario dentro de la Base de Datos (POST)
def createAnimal(animal: CreateAnimal):
    try:
        db = sessionlocal()
        animal_new = Animal(
            name = animal.name,
            photo = animal.photo,
            characteristic1 = animal.characteristic1,
            characteristic2 = animal.characteristic2,
            characteristic3 = animal.characteristic3,
            characteristic4 = animal.characteristic4
            
        )
        db.add(animal_new)
        db.commit()
        db.refresh(animal_new)
        db.close()
        return animal_new
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Actualizacion de Datos del Usuario        
def updateAnimal(animalupdate: UpdateAnimalDTO):
    try:
        db = sessionlocal()
        animal_update = db.query(Animal).filter(Animal.id == int(animalupdate.id)).first()
        if animal_update:
            animal_update.name = animalupdate.name
            animal_update.photo = animalupdate.photo
            animal_update.characteristic1 = animalupdate.characteristic1
            animal_update.characteristic2 = animalupdate.characteristic2
            animal_update.characteristic3 = animalupdate.characteristic3
            animal_update.characteristic4 = animalupdate.characteristic4
            
            db.commit()
            db.refresh(animal_update)
            return animal_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Borrado LOGICO de Datos de Usuario 
def deleteAnimal(animaldelete: DeleteAnimalDTO):
    try:
        db = sessionlocal()
        animal_delete = db.query(Animal).filter(Animal.id == animaldelete.id).first()
        if animal_delete:
            animal_delete.deleted = animaldelete.deleted
            db.commit()
            db.refresh(animal_delete)
            return animal_delete
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()