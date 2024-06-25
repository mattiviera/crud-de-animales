# Configuro el motor de base de datos y la cadena de conxion


# Con SQite
STRCNX='sqlite:///animals.db'


## ---------------------------------------------------------------------------

# Con MySQL, debemos tenes instalado pymysql

# Basicos
# HOST='SU_HOST' 
# USER='SU_USER'
# PWDS='SU_PASSWORD'
# DBA='SU_BASE_DE_DATOS'
# PORT='SU_PUERTO'

# Ejemplo:
# HOST='192.168.0.10' 
# USER='root'
# PWDS='Dany5170#'
# DBA='sampledbpy'
# PORT='3306'
# STRCNX=f'mysql+pymysql://{USER}:{PWDS}@{HOST}:{PORT}/{DBA}'


SQLALCHEMY_DATABASE_URI=STRCNX

from models.models import Animal

var_globales= {
    'isLogued': False,
    'user': Animal,
    'title': 'Mi App de Flask',
    'mensaje': ''
}