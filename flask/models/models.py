from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from typing import Optional
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

Base = declarative_base()

class Duenio(UserMixin, Base):
    __tablename__ = 'duenios'
    id= mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(unique=False, nullable=False)
    lastname: Mapped[str] = mapped_column(unique=False, nullable=False)
    localidad: Mapped[str] = mapped_column(unique=False, nullable=False)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animals.id'), nullable=True)
    username: Mapped[str] = mapped_column(String(25))
    password : Mapped[str] = mapped_column(String(128))
    
    animal: Mapped['Animal'] = relationship(back_populates="duenios")
    
    def set_password(self, password_to_hash):
        self.password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_hash):
        return check_password_hash(self.password, password_to_hash)

class Animal(Base):
    __tablename__ = 'animals'
    id= mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    photo: Mapped[str] = mapped_column(nullable=False)
    characteristic1: Mapped[str] = mapped_column(nullable=False)
    characteristic2: Mapped[str] = mapped_column(nullable=False)
    characteristic3: Mapped[str] = mapped_column()
    characteristic4: Mapped[str] = mapped_column()
    
    duenios : Mapped[List['Duenio']] = relationship(back_populates="animal")
    
    # Se instalan las librerias con flask_wtf y wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Optional

# Clase para Login de User
class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[
        DataRequired(message='Por favor, introduce tu nombre de usuario.'),
        Length(min=4, max=25, message='El nombre de usuario debe tener entre 4 y 25 caracteres.')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='Por favor, introduce tu contraseña.')
    ])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar sesión')

# Clase para Registracion de User
class RegistrationForm(FlaskForm):
    name = StringField('Nombre', validators=[
        DataRequired(message='Por favor, introduce tu nombre.'),
        Length(min=4, max=25, message='El nombre de usuario debe tener entre 4 y 25 caracteres.')
    ])
    lastname = StringField('Apellido', validators=[
        DataRequired(message='Por favor, introduce tu apellido.'),
        Length(min=4, max=25, message='El nombre de usuario debe tener entre 4 y 25 caracteres.')
    ])
    localidad = StringField('Localidad', validators=[
        DataRequired(message='Por favor, introduce tu localidad.'),
        Length(min=4, max=25, message='El nombre de usuario debe tener entre 4 y 25 caracteres.')
    ])
    animal_id = SelectField('Mascota',validators=[Optional()])
    
    username = StringField('Nombre de usuario', validators=[
        DataRequired(message='Por favor, introduce tu nombre de usuario.'),
        Length(min=4, max=25, message='El nombre de usuario debe tener entre 4 y 25 caracteres.')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='Por favor, introduce tu contraseña.'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres.')
    ])
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message='Por favor, confirma tu contraseña.'),
        EqualTo('password', message='Las contraseñas deben coincidir.')
    ])
    submit = SubmitField('Registrarse')
    
    
    