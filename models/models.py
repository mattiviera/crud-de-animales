from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Optional, List

Base = declarative_base()

class Animal(Base):
    __tablename__ = 'animals'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    photo: Mapped[str] = mapped_column(nullable=False)
    characteristic1: Mapped[str] = mapped_column(nullable=False)
    characteristic2: Mapped[str] = mapped_column(nullable=False)
    characteristic3: Mapped[str] = mapped_column()
    characteristic4: Mapped[str] = mapped_column()
    
    #duenios = Mapped[List['Duenio']] = relationship(back_populates="animal")
    duenios = relationship("Duenio", back_populates="animal")
    
class Duenio(Base):
    __tablename__ = 'duenios'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    lastname: Mapped[str] = mapped_column(unique=False, nullable=False)
    localidad: Mapped[str] = mapped_column(unique=False, nullable=False)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animals.id'))

    animal = relationship("Animal", back_populates="duenios")
    
    #animal: Mapped['Animal'] = relationship(back_populates="duenios")
    #animal_id = Column(Integer, ForeignKey('animals.id'), nullable=False)
    #animal = Mapped[List["Animal"]] = relationship(back_populates="duenios")
    