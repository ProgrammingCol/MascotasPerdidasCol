import os
from flask import Flask


def create_app(test_config=None):
    #crear y configurar la aplicacion
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        #configura una llave secreta para el acceso a modulo de base de datos
        SECRET_KEY='dev',
        #configura el PATH a la base de datos
        DATABASE=os.path.join(app.instance_path,'flask_sqlite')
    )

    if test_config == None:
        #carga la configuracion de instancia, si esta existe, cuando no esta en modo testeo
        app.config.from_pyfile('config.py',silent=True)
    else:
        #carga configuracion de test si se pasa
        app.config.from_mapping(test_config)