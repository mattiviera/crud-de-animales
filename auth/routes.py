from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.forms import LoginForm, RegistrationForm
from models.models import Duenio, Animal
from db import session

auth_bp = Blueprint('auth', __name__, template_folder="templates", static_folder="static")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(Duenio).filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    form.animal_id.choices = [(animal.id, animal.name) for animal in Animal.query.all()]
    if form.validate_on_submit():
        
        user = Duenio(
            name=form.name.data,lastname=form.lastname.data,localidad=form.localidad.data,animal_id=form.animal_id.data,username=form.username.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        flash('Tu cuenta ha sido creada. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)