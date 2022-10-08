from flask import Flask, jsonify
from flask_restful import Api
from app.db import db 
from app.ext import ma
from app.mascoticas.api_v1_0.auth import auth_bp
from app.mascoticas.api_v1_0.recursos import recursos_bp
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass



from config.default import SECRET_KEY, SQLALCHEMY_DATABASE_URI

def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    
    if test_config is None:
        app.config.from_pyfile('default.py')
    else: 
        app.config.from_object(test_config)
    
    db.init_app(app)
    ma.init_app(app)
    Api(app,catch_all_404s=True)
    
    #manejo de errores
    register_error_handlers(app)
    app.url_map.strict_slashes=False

    #Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(recursos_bp)
    
    @app.route('/')
    def hello():
        return "<h1>Bienvenido</h1>"
    return app

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500
    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405
    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
