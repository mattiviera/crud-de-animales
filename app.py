from flask import Flask, render_template
from flask_login import LoginManager
from models.models import Animal, Duenio
from werkzeug.exceptions import BadRequest, NotFound
import db

app = Flask(__name__)
app.config.from_object('config')

# Lo vinculamos con la app de Flask
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Define la ruta de login
login_manager.init_app(app)

# Decorador de Flask Login para el manejo de la carga del Id de Usuario
@login_manager.user_loader
def load_user(user_id):
    # Aca se pueden agregar acciones que necesitemos hacer cuando el usuario se carga
    return db.session.query(Duenio).get(int(user_id))

# Cuando la ruta existe pero no estoy autorizado a verla
@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html')

# BluePrint's
from main.routes import main_bp
from auth.routes import auth_bp
from animales.routes import animales_bp
from duenios.routes import duenios_bp

app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(animales_bp, url_prefix='/animales')
app.register_blueprint(duenios_bp, url_prefix='/duenios')

# Personalizacion de Errores
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

@app.errorhandler(NotFound)
def handle_not_found(e):
    return render_template('404.html')

# Retorna un diccionario con las variables que quieres compartir entre los templates y rutas
from config import var_globales
@app.context_processor
def inject_variables():
    return var_globales

# Definir un filtro personalizado para formatear la fecha
@app.template_filter('format_datetime')
def format_datetime(value, format="%d/%m/%Y %H:%M:%S"):
    return value.strftime(format)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])