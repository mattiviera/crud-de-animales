from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Animal, Duenio
#from cryptography.fernet import Fernet
import config

app = Flask(__name__)

# Se genera un clave secreta que permitira mas adelante encriptar datos
#app.secret_key = Fernet.generate_key()

# Configuro el motor de base de datos y la cadena de conexion importando las constantes
# significativas para la app.
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
title = 'Mi App de Flask'


@app.route('/')
@app.route('/home')
def index_animals():
    animals = session.query(Animal).all()
    return render_template('index.html', animals=animals)

@app.route('/create', methods=['GET', 'POST'])
def create_animal():
    if request.method == 'POST':
        name = request.form['name']
        photo = request.form['photo']
        characteristic1 = request.form['characteristic1']
        characteristic2 = request.form['characteristic2']
        characteristic3 = request.form.get('characteristic3', '')
        characteristic4 = request.form.get('characteristic4', '')

        newanimal = Animal(
            name=name,
            photo=photo,
            characteristic1=characteristic1,
            characteristic2=characteristic2,
            characteristic3=characteristic3,
            characteristic4=characteristic4
        )
        try:
            session.add(newanimal)
            session.commit()
            return redirect(url_for('index_animals'))
        except Exception as e:
            session.rollback()
            return f'Error al crear el animal: {e}'

    return render_template('create.html')

@app.route('/animal/<int:id>')
def detail_animal(id):
    animal = session.query(Animal).get(id)
    return render_template('detail.html', animal=animal)

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update_animal(id):

    animal = session.query(Animal).get(id)
    if animal:
        if request.method == 'POST':

            name = request.form['name']
            photo = request.form['photo']
            characteristic1 = request.form['characteristic1']
            characteristic2 = request.form['characteristic2']
            characteristic3 = request.form.get('characteristic3', '')
            characteristic4 = request.form.get('characteristic4', '')

            animal.name = name
            animal.photo = photo
            animal.characteristic1 = characteristic1
            animal.characteristic2 = characteristic2
            animal.characteristic3 = characteristic3
            animal.characteristic4 = characteristic4
            
            try:
                session.commit()
                return redirect(url_for('index_animals'))
            except Exception as e:
                session.rollback()
                return f'Error al actualizar el animal: {e}'

    return render_template('update.html', animal=animal)

@app.route('/delete/<int:id>')
def delete_animal(id):
    animal = session.query(Animal).get(id)
    if animal:
        try:
            session.delete(animal)
            session.commit()
        except Exception as e:
            print(f'Error al eliminar. {e}')
    return redirect(url_for('index_animals'))

# CRUD Dueño
@app.route('/indexduenio')
def index_duenios():
    duenios = session.query(Duenio).all()
    return render_template('indexduenio.html', duenios=duenios)

@app.route('/createduenio', methods=['GET', 'POST'])
def create_duenio():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        localidad = request.form['localidad']
        animal_id = request.form['animal_id']

        newduenio = Duenio(
            name=name,
            lastname=lastname,
            localidad=localidad,
            animal_id=animal_id
        )
        try:
            session.add(newduenio)
            session.commit()
            return redirect(url_for('index_duenios'))
        except Exception as e:
            session.rollback()
            return f'Error al crear el dueño: {e}'
    
    animals = session.query(Animal).all()
    return render_template('createduenio.html', animals=animals)

@app.route('/duenio/<int:id>')
def detail_duenio(id):
    duenio = session.query(Duenio).get(id)
    return render_template('detailduenio.html', duenio=duenio)

@app.route('/updateduenio/<int:id>', methods=["GET", "POST"])
def update_duenio(id):

    duenio = session.query(Duenio).get(id)
    if duenio:
        if request.method == 'POST':

            name = request.form['name']
            lastname = request.form['lastname']
            localidad = request.form['localidad']
            

            duenio.name = name
            duenio.lastname = lastname
            duenio.localidad = localidad
            
            
            try:
                session.commit()
                return redirect(url_for('index_duenios'))
            except Exception as e:
                session.rollback()
                return f'Error al actualizar el animal: {e}'

    return render_template('updateduenio.html', duenio=duenio)

@app.route('/deleteduenio/<int:id>')
def delete_duenio(id):
    duenio = session.query(Duenio).get(id)
    if duenio:
        try:
            session.delete(duenio)
            session.commit()
        except Exception as e:
            print(f'Error al eliminar. {e}')
    return redirect(url_for('index_duenios'))

if __name__ == '__main__':
    app.run(debug=True)
