from datetime import date
from urllib import response
from flask import request, Blueprint, make_response, jsonify
from flask_restful import Api, Resource
from functools import wraps
from app.db import db
from app.mascoticas.api_v1_0.schemas import UsuarioSchema
from app.mascoticas.modelos import BlacklistToken, Usuario
from config.default import SECRET_KEY


def token_required(f):
    '''Decorador para segurar que tiene token valido'''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            try:
                token = request.headers["Authorization"].split(" ")[1]
            except IndexError:
                response_object ={
                    'status':'fail',
                    'mesage':'Bearer token mal formado, revise sintaxis.'
                }
                return response_object,401
        if not token:
            return {
                "message": "El Token no existe!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            user_id=Usuario.decode_auth_token(token)
            current_user=Usuario.query.get(user_id)
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated

auth_bp = Blueprint('auth_bp',__name__,url_prefix='/api/v1/auth')

usuario_schema = UsuarioSchema()

api = Api(auth_bp)

class UserRegisterResource(Resource):
    def post(self):
        '''Entrada:
        Body keys: nombre, apellidoP, apellidoM, telefono, 
        fechaActualizacion, correo, password, idciudad
        respuesta: json(usuario registrado,token), json(error), json(usuario existente)'''
        post_data = request.get_json()
        user = Usuario.query.filter_by(correo=post_data.get('correo')).first()
        print('usuario',user)
        n = usuario_schema.load(post_data)
        
        print('load',n)
        if not user:
            try:
                print(type(post_data)) 
                new_user = usuario_schema.load(post_data)
                print('hola!')

                new_user.set_password(post_data.get('password'))
                new_user.fechaActualizacion = date.today()
                new_user.save()
                auth_token = new_user.encode_auth_token(new_user.id_usuario)
                response_object={
                    'status':'Aceptada',
                    'message':'Usuario registrado satisfactoriamente.',
                    'data':auth_token                    
                }
                print(response_object)
                return response_object,201
            except Exception as e:
                response_object={
                    'status':'fail',
                    'message':'Ocurrio algun error, intente de nuevo',
                    'data':str(e)                    
                }
                return response_object,500
        else: 
            print('hola')
            response_object={
                    'status':'fail',
                    'message':'El usuario ya existe o ese correo ya esta en uso'
                }
            return response_object,202

api.add_resource(UserRegisterResource,'/register',endpoint='user_register')

class UserLoginResource(Resource):
    def post(self):
        '''Comprueba los correos y contrasena, devolviendo token 
        Entrada: correo, password
        Salida: json(datos usuario), json(error)'''
        post_data = request.get_json()
        try:
            data_user = usuario_schema.load(post_data)
            user = Usuario.query.filter_by(
                correo=data_user.correo
            ).first()
            if user.check_password(post_data.get('password')):
                user_token = user.encode_auth_token(user.id_usuario)
            else: user_token = None
            
            if user_token:
                response_object = {
                    'status': 'success',
                    'message': 'Inicio de sesion adecuado.',
                    'auth_token': user_token
                }
                return response_object, 200
            else:
                response_object = {
                    'status':'fail',
                    'message':'Usuario o contrasena invalidos'
                }
                return response_object,400
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500
        
    def get(self):
        '''Entrada:  
        header: 'Authorization':token
        Salida:
        json(datos de usuario),json(respuesta fallida),json(token invalido)
        '''
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                response_object ={
                    'status':'fail',
                    'mesage':'Bearer token mal formado, revise sintaxis.'
                }
                return response_object,401
        else:
            auth_token = ''
        
        if auth_token:
            resp = Usuario.decode_auth_token(auth_token)
            if not isinstance(resp,str):
                user = Usuario.query.filter_by(id_usuario =resp).first()
                response_object = {
                    'status':'aceptada',
                    'data': usuario_schema.dump(user),                    
                }
                return response_object,200
            response_object={
                'status':'fail',
                'mesage':resp
            }
            return response_object,401
        else: 
            response_object={
                'status':'fail',
                'mesage':'Envie un token valido.'
            }
            return response_object
        
    def put(self):
        '''Cambio de password
        Entrada: body: correo,telefono
        salida: json(str), 201 o json(str),401/500'''
        put_data = request.get_json()
        usuario = Usuario.simple_filter(correo = put_data.get('correo'),telefono = put_data.get('telefono'))
        
        if usuario:
            try:
                user_token = usuario.encode_auth_token(usuario.id_usuario)
                response_object = {
                    'status': 'success',
                    'message': 'Inicio de sesion adecuado.',
                    'auth_token': user_token
                }
                return response_object, 201
            except Exception as e:
                print(e)
                response_object = {
                'status': 'fail',
                'message': 'Ocurrio un error, vuelve a intentar'
                }
                return response_object, 500
        else:
            response_object = {
                'status':'fail',
                'message':'correo o telefono invalidos, intente nuevamente'
            }
            return response_object,401
        
api.add_resource(UserLoginResource,'/login',endpoint='user_login')
        
class UserLogoutResource(Resource):
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                response_object ={
                    'status':'fail',
                    'mesage':'Bearer token mal formado, revise sintaxis.'
                }
                return response_object,401
        else:
            auth_token = ''
        if auth_token:
            resp = Usuario.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    # insert the token
                    db.session.add(blacklist_token)
                    db.session.commit()
                    response_object = {
                        'status': 'aceptada',
                        'message': 'Sesion cerrada satisfactoriamente.'
                    }
                    return response_object, 200
                except Exception as e:
                    response_object = {
                        'status': 'fail',
                        'message': e
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Envie un token valido.'
            }
            return response_object, 403
  
api.add_resource(UserLogoutResource,'/logout',endpoint='user_logout')
