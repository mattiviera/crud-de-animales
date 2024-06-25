from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base
from models.models import Animal
from cryptography.fernet import Fernet
import config
import db

# BluePrint's
from animales.routes import animales_bp
from duenios.routes import duenios_bp

app = Flask(__name__)
# Se genera un clave secreta que permitira mas adelante encriptar datos
app.secret_key = Fernet.generate_key()
app.register_blueprint(animales_bp, url_prefix='/animales')
app.register_blueprint(duenios_bp, url_prefix='/duenios')

# Retorna un diccionario con las variables que quieres compartir entre los templates y rutas
@app.context_processor
def inject_variables():
    return config.var_globales

# Se genera un clave secreta que permitira mas adelante encriptar datos
#app.secret_key = Fernet.generate_key()
# Definir un filtro personalizado para formatear la fecha

@app.template_filter('format_datetime')
def format_datetime(value, format="%d/%m/%Y %H:%M:%S"):
    return value.strftime(format)

@app.route('/home')
@app.route('/')
def index_animals():
    animals = db.session.query(Animal).all()
    return render_template('base.html', animals=animals)

if __name__ == '__main__':
    app.run(debug=True)