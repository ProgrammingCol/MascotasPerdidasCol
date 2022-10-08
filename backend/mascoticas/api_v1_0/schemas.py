from xml.dom import ValidationErr
from marshmallow import fields,post_load
from app.ext import ma
from app.mascoticas.modelos import Departamento, Mascota, Reportes, Usuario

class BytesField(fields.Field):
    def _validate(self, value):
        if not isinstance(value, bytes):
            raise ValidationErr('Invalid input type.')

        if value is None or value == b'':
            raise ValidationErr('Invalid value')


class DepartamentoSchema(ma.Schema):
    iddepto = fields.Integer(dump_only=True)
    depto = fields.String()
    ciudades = fields.Nested('CiudadSchema',many=True)
    
    @post_load
    def crear_depto(self,data,**kwargs):
        return Departamento(**data) 
    class Meta:
        ordered =True
class CiudadSchema(ma.Schema):
    idciudad = fields.Integer(dump_only=True)
    ciudad = fields.String()
    
    usuario = fields.Nested('UsuarioSchema',exclude=('ciudad',))
    departamento = fields.Nested('DepartamentoSchema')
    class Meta:
        ordered =True

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
    
    class Meta:
        ordered =True

class EspecieSchema(ma.Schema):
    id_especie = fields.Integer(dump_only=True)
    especie = fields.String()
    class Meta:
        ordered =True
class SexoSchema(ma.Schema):
    id_sexo = fields.Integer(dump_only=True)
    sexo = fields.String()
    class Meta:
        ordered =True
class RazaSchema(ma.Schema):
    id_raza = fields.Integer(dump_only=True)
    raza = fields.String()
    class Meta:
        ordered =True
class MascotaSchema(ma.Schema):
    idMascota = fields.Integer(dump_only=True)
    nombre = fields.String ()
    sexo = fields.Nested('SexoSchema')
    especie = fields.Nested('EspecieSchema')
    raza = fields.Nested('RazaSchema')
    ciudad = fields.Nested('CiudadSchema')
    usuario = fields.Nested('UsuarioSchema',exclude=('mascota',))
    estado = fields.String()
    descripcion = fields.String()
    foto = BytesField()
    id_usuario = fields.Integer(load_only=True)
    id_raza = fields.Integer(load_only=True)
    id_sexo = fields.Integer(load_only=True)
    id_ciudad = fields.Integer(load_only=True)
    id_especie = fields.Integer(load_only=True)
    
    reporte = fields.Nested('Reportes',exclude=('mascota',))
    
    @post_load
    def make_mascota(self,data,**kwargs):
        return Mascota(**data) 
    class Meta:
        ordered =True
class ReportesSchema(ma.Schema):
    idReporte = fields.Integer(dump_only=True)
    fecha = fields.Date()
    datosAdicionales = fields.String()
    tipo = fields.String()
    idMascota = fields.Integer(load_only=True)
    
    mascota = fields.Nested('MascotaSchema')
    
    @post_load
    def make_reporte(self,data,**kwargs):
        return Reportes(**data) 
    
    class Meta:
        ordered =True
class BlacklistSchema(ma.Schema):
    id = fields.Integer(dump_only= True)
    token = fields.String()
    blacklisted_on = fields.DateTime()
    