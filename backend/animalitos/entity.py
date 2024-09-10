# Declaracion del Modelo de Datos que se conecta con la BD

from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class Animal(Base):
    __tablename__ = 'animales'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    photo = Column(String(100), nullable=False)
    characteristic1 = Column(String(100))
    characteristic2 = Column(String(100))
    characteristic3 = Column(String(100))
    characteristic4 = Column(String(100))