from dataclasses import dataclass
from datetime import date
import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import db, BaseModelMixin
import jwt

from config.default import SECRET_KEY

@dataclass
class Usuario(db.Model, BaseModelMixin, UserMixin):
    __tablename__ = 'usuario'
    id_usuario: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String)
    apellidoP: str = db.Column(db.String)
    apellidoM: str = db.Column(db.String)
    telefono: str = db.Column(db.String)
    fechaActualizacion: date = db.Column(db.Date)
    correo: str = db.Column(db.String)
    password: str = db.Column(db.String)
    token: str = db.Column(db.String, unique=True)
    
    idciudad: int = db.Column(db.Integer, db.ForeignKey('ciudad.idciudad'))
    ciudad = db.relationship('Ciudad', back_populates='usuario')

    mascota = db.relationship('Mascota', back_populates='usuario')

    def __post_init__(self):
        self.fechaActualizacion = date.today()

    def hide_sensible_data(self):
        self.password = None
        self.token = None

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=1, minutes=30, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token inhabilitado, por favor vuelva a iniciar sesion'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String, unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False

@dataclass
class Ciudad(db.Model, BaseModelMixin):
    __tablename__ = 'ciudad'
    idciudad: int = db.Column(db.Integer, primary_key=True)
    ciudad: str = db.Column(db.String)
    
    iddepto: int = db.Column(db.Integer, db.ForeignKey('departamento.iddepto'))
    departamento = db.relationship('Departamento',backref='ciudad')
    
    usuario = db.relationship('Usuario', back_populates='ciudad')
    mascota = db.relationship('Mascota', back_populates='ciudad')

@dataclass
class Departamento(db.Model, BaseModelMixin):
    __tablename__ = 'departamento'
    iddepto: int = db.Column(db.Integer, primary_key=True)
    depto = db.Column(db.String)

@dataclass
class Mascota(db.Model, BaseModelMixin):
    __tablename__ = 'mascota'
    idMascota: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String)
    descripcion: str = db.Column(db.String)
    estado: str = db.Column(db.String)
    foto = db.Column(db.LargeBinary)
    
    id_usuario: int = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    usuario = db.relationship('Usuario',back_populates='mascota')
    
    id_ciudad: int = db.Column(db.Integer, db.ForeignKey('ciudad.idciudad'))
    ciudad = db.relationship('Ciudad',back_populates='mascota')
    
    id_especie: int = db.Column(db.Integer, db.ForeignKey('especie.id_especie'))
    especie = db.relationship('Especie')
    
    id_raza: int = db.Column(db.Integer, db.ForeignKey('raza.id_raza'))
    raza = db.relationship('Raza')
    
    id_sexo: int = db.Column(db.Integer, db.ForeignKey('sexo.id_sexo'))
    sexo = db.relationship('Sexo')
    
    reportes = db.relationship('Reportes', back_populates='mascota')

@dataclass
class Raza(db.Model, BaseModelMixin):
    __tablename__ = 'raza'
    id_raza: int = db.Column(db.Integer, primary_key=True)
    raza: str = db.Column(db.String)

@dataclass
class Sexo(db.Model, BaseModelMixin):
    __tablename__ = 'sexo'
    id_sexo: int = db.Column(db.Integer, primary_key=True)
    sexo: str = db.Column(db.String)

@dataclass
class Especie(db.Model, BaseModelMixin):
    __tablename__ = 'especie'
    id_especie: int = db.Column(db.Integer, primary_key=True)
    especie: str = db.Column(db.String)

@dataclass
class Reportes(db.Model, BaseModelMixin):
    __tablename__ = 'reportes'
    idReporte: int = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    datosAdicionales: str = db.Column(db.String)
    tipo: str = db.Column(db.String)
    
    idMascota: int = db.Column(db.Integer, db.ForeignKey('mascota.idMascota'))
    mascota = db.relationship('Mascota', back_populates='reportes')
    
    def __post_init__(self):
        self.fecha = date.today()
