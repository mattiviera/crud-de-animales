from fastapi import FastAPI
from default.defaultmodel import Base
from config.cnx import engine

# Ruotes
from default.routes import default
from animalitos.routes import animal
#from task.routes import task

app = FastAPI(
    title="API Rest FastAPI",
    description="Ejemplo de API Rest con FASTAPI",
    version="0.0.1",
        contact={
        "name": "Soporte Técnico",
        "email": "soporte@miempresa.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Ruotes Apps
app.include_router(default, prefix='', tags=['App Routes Default'])
app.include_router(animal, prefix='/animales', tags=['Users Endpoints'])
#app.include_router(task, prefix='/task', tags=['Tasks Endpoints'])

Base.metadata.create_all(bind=engine)