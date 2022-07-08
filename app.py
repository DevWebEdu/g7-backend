from flask import Flask
from config import conexion
from models.participante import Participante
from dotenv import load_dotenv
# environ > me devuelve todas las variables de entorno en forma de un diccionario
from os import environ

# carga todas las variables declaradas en el archivo .env como si fuesen variables de entorno para que puedan ser accedidas desde el metodo 'environ'
load_dotenv()

app = Flask(__name__)
# URI dialect://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']

# sqlalchemy hace un seguimiento a las modificaciones que haremos a la bd pero actualmente tiene un valor predeterminado PERO en futuras versiones tendremos que OBLIGATORIAMENTE indicar si queremos hacer el seguimiento o no
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# inicializo mi conexion de mi sqlalchemy con la base de datos PERO todavia no me he conectado
conexion.init_app(app)

# se ejecuta la conexion y se crearan las tablas PERO si no hay ningun tabla a crear entonces no lanzara error de credenciales invalidas
conexion.create_all(app=app)


if __name__ == '__main__':
    app.run(debug=True)
