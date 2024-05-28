from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'

db = SQLAlchemy(app)

class Base(DeclarativeBase):
    pass

class Animal(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    photo: Mapped[str] = mapped_column(nullable=False)
    characteristic1: Mapped[str] = mapped_column(nullable=False)
    characteristic2: Mapped[str] = mapped_column(nullable=False)
    characteristic3: Mapped[str] = mapped_column()
    characteristic4: Mapped[str] = mapped_column()

with app.app_context():

    db.create_all()
title = 'Mi App de Flask'


@app.route('/')
@app.route('/home')
def index():
    animals = Animal.query.all()
    return render_template('index.html', animals=animals)

@app.route('/create', methods=['GET', 'POST'])
def create():
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
            db.session.add(newanimal)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            return f'Error al crear el animal: {e}'

    return render_template('create.html')

@app.route('/animal/<int:id>')
def detail(id):
    animal = Animal.query.get(id)
    return render_template('detail.html', animal=animal)

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):

    animal = Animal.query.get(id)
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
                db.session.commit()
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                return f'Error al actualizar el animal: {e}'

    return render_template('update.html', animal=animal)

@app.route('/delete/<int:id>')
def delete(id):
    animal = Animal.query.get(id)
    if animal:
        try:
            db.session.delete(animal)
            db.session.commit()
        except Exception as e:
            print(f'Error al eliminar. {e}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
