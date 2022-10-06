from xml.dom import ValidationErr
from marshmallow import fields,post_load
from app.ext import ma
from app.mascoticas.modelos import Mascota, Reportes, Usuario

class BytesField(fields.Field):
    def _validate(self, value):
        if not isinstance(value, bytes):
            raise ValidationErr('Invalid input type.')

        if value is None or value == b'':
            raise ValidationErr('Invalid value')

class CiudadSchema(ma.Schema):
    idciudad = fields.Integer(dump_only=True)
    ciudad = fields.String()
    
    # usuario = fields.Nested('UsuarioSchema',exclude=('ciudad',))
    departamento = fields.Nested('DepartamentoSchema')

class DepartamentoSchema(ma.Schema):
    iddepto = fields.Integer(dump_only=True)
    depto = fields.String()

class UsuarioSchema(ma.Schema):
    id_usuario = fields.Integer(dump_only=True)
    nombre = fields.String()
    apellidoP = fields.String()
    apellidoM = fields.String()
    telefono = fields.String()
    fechaActualizacion = fields.Date()
    correo = fields.Email()
    password = fields.String(load_only=True)
    token = fields.String(load_only=True)
    idciudad = fields.Integer(load_only=True)
    
    mascota = fields.Nested('MascotaSchema',exclude=('usuario',),many=True)
    ciudad = fields.Nested('CiudadSchema', exclude=('usuario',))
    
    @post_load
    def crear_usuario(self,data,**kwargs):
        return Usuario(**data) 

class EspecieSchema(ma.Schema):
    id_especie = fields.Integer(dump_only=True)
    especie = fields.String()

class SexoSchema(ma.Schema):
    id_sexo = fields.Integer(dump_only=True)
    sexo = fields.String()

class RazaSchema(ma.Schema):
    id_raza = fields.Integer(dump_only=True)
    raza = fields.String()

class MascotaSchema(ma.Schema):
    idMascota = fields.Integer(dump_only=True)
    nombre = fields.String ()
    descripcion = fields.String()
    estado = fields.String()
    foto = BytesField(required=True)
    usuario = fields.Nested('UsuarioSchema',exclude=('mascota',))
    raza = fields.Nested('RazaSchema')
    sexo = fields.Nested('SexoSchema')
    ciudad = fields.Nested('CiudadSchema')
    especie = fields.Nested('EspecieSchema')
    reporte = fields.Nested('Reportes',exclude=('mascota',))
    
    @post_load
    def make_mascota(self,data,**kwargs):
        return Mascota(**data) 
    
class ReportesSchema(ma.Schema):
    idReporte = fields.Integer(dump_only=True)
    fecha = BytesField(required=True)
    datosAdicionales = fields.String()
    tipo = fields.String()
    Mascota = fields.Nested('MascotaSchema',exclude=('reportes',))
    
    @post_load
    def make_reporte(self,data,**kwargs):
        return Reportes(**data) 

class BlacklistSchema(ma.Schema):
    id = fields.Integer(dump_only= True)
    token = fields.String()
    blacklisted_on = fields.DateTime()
    