from datetime import date
from flask import request, Blueprint, make_response , jsonify
from flask_restful import Api, Resource

from app.mascoticas.api_v1_0.auth import token_required
from app.mascoticas.api_v1_0.schemas import UsuarioSchema,MascotaSchema,ReportesSchema, CiudadSchema, DepartamentoSchema, RazaSchema, SexoSchema, EspecieSchema
from app.mascoticas.modelos import Usuario, Mascota, Reportes, Ciudad, Departamento, Raza, Sexo, Especie

recursos_bp = Blueprint('recursos_bp',__name__,url_prefix='/api/v1')
api = Api (recursos_bp)

#generacion de esquemas a utilizar
usuarios_schema = UsuarioSchema()
mascotas_schema = MascotaSchema()
reportes_schema = ReportesSchema()
ciudad_schema = CiudadSchema()
departamentos_schema = DepartamentoSchema()
raza_schema = RazaSchema()
sexo_schema = SexoSchema()
especie_schema = EspecieSchema()

#constantes
error='Algo salio mal!, por favor intenta de nuevo'

#recursos para adicionar a la api

class UsuarioResource(Resource):
    @token_required
    def put(self,current_user):
        put_data = request.get_json()
        cambio = usuarios_schema.load(put_data)
        if cambio:
            try:
                if cambio.nombre: current_user.nombre = cambio.nombre
                if cambio.apellidoP: current_user.apellidoP = cambio.apellidoP
                if cambio.apellidoM: current_user.apellidoM = cambio.apellidoM
                if cambio.idciudad: current_user.nombre = cambio.idciudad
                if cambio.mascota: current_user.mascota = cambio.mascota
                if cambio.password: current_user.set_password(cambio.password)
                current_user.fecha = date.today()
                current_user.save()
                response_object ={
                        'status':'aceptada',
                        'message':'Cambio en usuario realizado'
                    }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                    response_object ={
                        'status':'fail',
                        'message':error
                    }
                    print(e)
                    return make_response(jsonify(response_object)),500
        else:
            response_object ={
                    'status':'fail',
                    'message':'No se ha encontrado cambios, intente de nuevo.'
                }
            return make_response(jsonify(response_object)),401


api.add_resource(UsuarioResource,'/usuario/',endpoint='modificar_usuario')  

class MascotasResouce(Resource):
    def get(self):
        mascotas = Mascota.get_all()
        respuesta = mascotas_schema.dump(mascotas)
        return respuesta,201

    @token_required
    def post(self,current_user):
        post_data = request.get_json()
        mascota = Mascota.simple_filter(nombre=post_data.get('nombre'),id_especie=post_data.get('id_especie'),id_ciudad=post_data.get('id_ciudad'),raza=post_data.get('raza'))
        if mascota:
            try:
                mascota = mascotas_schema.load(post_data)
                mascota.id_usuario = current_user.id_usuario
                mascota.save()
                
                response_object ={
                    'status':'aceptada',
                    'message':'Se ha creado la mascota exitosamente'
                }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                response_object ={
                    'status':'fail',
                    'message':error
                }
                print(e)
                return make_response(jsonify(response_object)),500
                
        else:
            response_object ={
                    'status':'fail',
                    'message':'La mascota ya existe!'
                }
            return make_response(jsonify(response_object)),401
            
api.add_resource(MascotasResouce,'/mascotas',endpoint='registro_mascotas')    

class MascotasIdResouce(Resource):
    def get(self,idMascota):
        mascota = Mascota.get_by_id(idMascota)
        respuesta = mascotas_schema.dump(mascota)
        return respuesta,200
    
    @token_required
    def put(self,current_user,idMascota):
        put_data = request.get_json()
        mascota = Mascota.get_by_id(idMascota)
        
        if current_user in mascota.usuario:
            try:
                cambios = mascotas_schema.load(put_data)
                if cambios.nombre: mascota.nombre = cambios.nombre
                if cambios.descripcion: mascota.descripcion = cambios.descripcion
                if cambios.estado: mascota.estado = cambios.estado
                if cambios.id_ciudad: mascota.id_ciudad = cambios.id_ciudad
                if cambios.id_especie: mascota.id_especie = cambios.id_especie
                if cambios.id_raza: mascota.id_raza = cambios.id_raza
                if cambios.id_sexo: mascota.id_sexo = cambios.id_sexo
                mascota.save()
                response_object ={
                    'status':'aceptada',
                    'message':'Nueva mascota creada'
                }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                response_object ={
                    'status':'fail',
                    'message':error
                }
                print(e)
                return make_response(jsonify(response_object)),500
        else:
            response_object ={
                    'status':'fail',
                    'message':'La mascota no le pertenece, procedimiento no autorizado'
                }
            return make_response(jsonify(response_object)),401
    
    @token_required    
    def delete(self,current_user,idMascota):
        mascota = Mascota.get_by_id(idMascota)
        if mascota and current_user in mascota.usuario:
            try:
                mascota.delete()
                response_object ={
                    'status':'aceptada',
                    'message':'La mascota ha sido eliminada con exito'
                }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                response_object ={
                'status':'fail',
                'message':error
                }
                print(e)
                return make_response(jsonify(response_object)),500
        else:
            response_object ={
                'status':'fail',
                'message':'La mascota no existe o el usuario no tiene permiso para eliminarlo'
                }
            return make_response(jsonify(response_object)),401
        
api.add_resource(MascotasIdResouce,'/mascotas/<int:idMascota>',endpoint='registro_mascota_id')          

class ReportesResource(Resource):
    def get(self):
        reporte = Reportes.get_all()
        resultado = reportes_schema.dump(reporte,many=True)
        return resultado,201
    
    @token_required
    def post(self):
        data_request = request.get_json()
        reporte = Reportes().query.filter_by(tipo = data_request.get('tipo'),datosAdicionales=data_request.get('datosAdicionales')).first()
        if not reporte:
            try:
                nuevo_reporte = reportes_schema.load(data_request)
                nuevo_reporte.fecha = date.today()
                nuevo_reporte.mascota = Mascota.get_by_id(data_request.get('idMascota'))
                nuevo_reporte.save()
                response_object ={
                    'status':'aceptada',
                    'message':'Nuevo reporte creado'
                }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                response_object ={
                    'status':'fail',
                    'message':error
                }
                print(e)
                return make_response(jsonify(response_object)),500
        else:
            response_object ={
                    'status':'fail',
                    'message':'El reporte ya existe!'
                }
            return make_response(jsonify(response_object)),401
               
api.add_resource(ReportesResource,'/reportes',endpoint='registro_reportes') 


class ReporteIdResource(Resource):
    def get(self,idReporte):
        reporte = Reportes.querry.filter_by(idReporte).first()
        resultado = reportes_schema.dump(reporte)
        return resultado,201
    
    @token_required
    def put(self,current_user,idReporte):
        reporte = Reportes.simple_filter(idReporte)
        if reporte.mascota.idMascota == Mascota.simple_filter(id_usuario = current_user.id_usuario).idMascota:
            try:
                cambios = reportes_schema.load(request.get_json())
                if cambios.datosAdicionales:reporte.datosAdicionales=cambios.datosAdicionales
                if cambios.idMascota:reporte.idMascota=cambios.idMascota
                reporte.fecha = date.now()
                reporte.save()
                response_object ={
                    'status':'aceptada',
                    'message':'Reporte modificado con exito'
                }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                response_object ={
                'status':'fail',
                'message':error
                }
                print(e)
                return make_response(jsonify(response_object)),401
        else:
            response_object ={
                'status':'fail',
                'message':'La mascota no le pertenece'
            }
            return make_response(jsonify(response_object)),401
    
    @token_required    
    def delete(self,current_user,idReporte):
        reporte = Reportes.get_by_id(idReporte)
        if reporte and current_user:
            try:
                reporte.delete()
                response_object ={
                    'status':'aceptada',
                    'message':'El reporte ha sido eliminado con exito'
                }
                return make_response(jsonify(response_object)),201
            except Exception as e:
                response_object ={
                'status':'fail',
                'message':error
                }
                print(e)
                return make_response(jsonify(response_object)),500
        else:
            response_object ={
                'status':'fail',
                'message':'El reporte no existe o el usuario no tiene permiso para eliminarlo'
                }
            return make_response(jsonify(response_object)),401
            
api.add_resource(ReporteIdResource,'/reportes/<int:idReporte>',endpoint='registro_reportes_id')        

class EspecieResouce(Resource):
    def get(self):
        especies = Especie.get_all()
        resultado = especie_schema.dump(especies,many=True)
        return resultado,201
api.add_resource(EspecieResouce,'/especie',endpoint='get_especie')  

class SexoResouce(Resource):
    def get(self):
        sexo = Sexo.get_all()
        resultado = sexo_schema.dump(sexo,many=True)
        return resultado
api.add_resource(SexoResouce,'/sexo',endpoint='get_sexo')  

class RazaResouce(Resource):
    def get(self):
        raza = Raza.get_all()
        resultado = raza_schema.dump(raza,many=True)
        return resultado,201
api.add_resource(RazaResouce,'/raza',endpoint='get_raza')  

class DepartamentosResouce(Resource):
    def get(self):
        departamentos = Departamento.get_all()
        resultado = departamentos_schema.dump(departamentos,many=True)
        print(type(resultado))
        return resultado,201
api.add_resource(DepartamentosResouce,'/departamentos',endpoint='get_departamentos')      

class CiudadesResouce(Resource):
    def get(self):
        ciudades = Ciudad.get_all()
        resultado = ciudad_schema.dump(ciudades, many=True)
        return resultado,201
api.add_resource(CiudadesResouce,'/ciudades',endpoint='get_ciudades')      
