from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_login import login_required, current_user
from models.models import Duenio, Animal
from db import session
from config import var_globales

duenios_bp = Blueprint (
    "duenios_bp", __name__, template_folder="templates", static_folder="static"
)

@duenios_bp.route('/perfil')
@login_required
def perfil():
    duenio = session.query(Duenio).get(current_user.id)
    return render_template('duenios/perfil.html', duenio=duenio)



# CRUD Dueño
#@duenios_bp.route('/indexduenio')
#def index_duenios():
#    duenios = session.query(Duenio).all()
#    return render_template('duenios/indexduenio.html', duenios=duenios)

#@duenios_bp.route('/createduenio', methods=['GET', 'POST'])
#def create_duenio():
#    if request.method == 'POST':
#        name = request.form['name']
#        lastname = request.form['lastname']
#        localidad = request.form['localidad']
#        animal_id = request.form['animal_id']

#        newduenio = Duenio(
#            name=name,
#            lastname=lastname,
#            localidad=localidad,
#            animal_id=animal_id
#        )
#        try:
#            session.add(newduenio)
#            session.commit()
#            return redirect(url_for('/duenios'))
#        except Exception as e:
#            session.rollback()
#            return f'Error al crear el dueño: {e}'
#    
#    animals = session.query(Animal).all()
#    return render_template('duenios/createduenio.html', animals=animals)

#@duenios_bp.route('/duenio/<int:id>')
#def detail_duenio(id):
#    duenio = session.query(Duenio).get(id)
#    return render_template('duenios/detailduenio.html', duenio=duenio)

#@duenios_bp.route('/updateduenio/<int:id>', methods=["GET", "POST"])
#def update_duenio(id):

#    duenio = session.query(Duenio).get(id)
#    if duenio:
#        if request.method == 'POST':

#            name = request.form['name']
#            lastname = request.form['lastname']
#            localidad = request.form['localidad']
#            

#            duenio.name = name
#            duenio.lastname = lastname
#            duenio.localidad = localidad
#            
#            
#            try:
#                session.commit()
#                return redirect(url_for('/duenios'))
#            except Exception as e:
#                session.rollback()
#                return f'Error al actualizar el animal: {e}'

#    return render_template('duenios/updateduenio.html', duenio=duenio)

#@duenios_bp.route('/deleteduenio/<int:id>')
#def delete_duenio(id):
#    duenio = session.query(Duenio).get(id)
#    if duenio:
#        try:
#            session.delete(duenio)
#            session.commit()
#        except Exception as e:
#            print(f'Error al eliminar. {e}')
#    return redirect(url_for('/duenios'))

