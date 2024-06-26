from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from models.models import Animal
from db import session
from config import var_globales

animales_bp = Blueprint (
    "animales_bp", __name__, template_folder="templates", static_folder="static"
)

@animales_bp.route('/home')
def index_animals():
    animals = session.query(Animal).all()
    return render_template('animales/index.html', animals=animals)

@animales_bp.route('/create', methods=['GET', 'POST'])
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
            return redirect(url_for('/animales'))
        except Exception as e:
            session.rollback()
            return f'Error al crear el animal: {e}'

    return render_template('animales/create.html')

@animales_bp.route('/animal/<int:id>')
def detail_animal(id):
    animal = session.query(Animal).get(id)
    return render_template('animales/detail.html', animal=animal)

@animales_bp.route('/update/<int:id>', methods=["GET", "POST"])
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
                return redirect(url_for('/animales'))
            except Exception as e:
                session.rollback()
                return f'Error al actualizar el animal: {e}'

    return render_template('animales/update.html', animal=animal)

@animales_bp.route('/delete/<int:id>')
def delete_animal(id):
    animal = session.query(Animal).get(id)
    if animal:
        try:
            session.delete(animal)
            session.commit()
        except Exception as e:
            print(f'Error al eliminar. {e}')
    return redirect(url_for('/animales'))