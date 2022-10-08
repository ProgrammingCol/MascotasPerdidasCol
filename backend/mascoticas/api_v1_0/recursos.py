from datetime import date
from flask import request, Blueprint
from flask_restful import Api, Resource

from app.mascoticas.api_v1_0.auth import token_required
from app.mascoticas.api_v1_0.schemas import UsuarioSchema,MascotaSchema,ReportesSchema, CiudadSchema, DepartamentoSchema, RazaSchema, SexoSchema, EspecieSchema
from app.mascoticas.modelos import Usuario, Mascota, Reportes, Ciudad, Departamento, Raza, Sexo, Especie

recursos_bp = Blueprint('recursos_bp',__name__,url_prefix='/api/v1/recursos')
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
        
        @token_required
        def get_user(request):
            return request
        user = get_user()
        
        if cambio:
            try:
                instance = Usuario.query.filter(Usuario.id_usuario == user.id_usuario)                
                instance.update(dict(put_data))
                user.fechaActualizacion = date.today()
                user.update_db()
                response_object ={
                        'status':'aceptada',
                        'message':'Cambio en usuario realizado'
                    }
                return response_object,201
            except Exception as e:
                    response_object ={
                        'status':'fail',
                        'message':error
                    }
                    print(e)
                    return response_object,500
        else:
            response_object ={
                    'status':'fail',
                    'message':'No se ha encontrado cambios, intente de nuevo.'
                }
            return response_object,401


api.add_resource(UsuarioResource,'/usuario',endpoint='modificar_usuario')  

class MascotasResouce(Resource):
    def get(self):
        mascotas = Mascota.get_all()
        respuesta = mascotas_schema.dump(mascotas,many=True)
        return respuesta,201

    @token_required
    def post(self,current_user):
        post_data = request.get_json()
        mascota = Mascota.simple_filter(nombre=post_data.get('nombre'),id_especie=post_data.get('id_especie'),id_ciudad=post_data.get('id_ciudad'),raza=post_data.get('raza'))
        if not mascota:
            try:
                @token_required
                def get_user(request):
                    return request
                user = get_user()
                print(post_data)
                mascota_nueva = mascotas_schema.load(post_data)
                print(mascota_nueva)
                mascota_nueva.id_usuario = user.id_usuario
                mascota_nueva.save()
                
                response_object ={
                    'status':'aceptada',
                    'message':'Se ha creado la mascota exitosamente',
                    'data':mascotas_schema.dump(mascota_nueva)
                }
                return response_object,201
            except Exception as e:
                response_object ={
                    'status':'fail',
                    'message':error
                }
                print(e)
                return response_object,500
                
        else:
            response_object ={
                    'status':'fail',
                    'message':'La mascota ya existe!'
                }
            return response_object,401
            
api.add_resource(MascotasResouce,'/mascotas',endpoint='registro_mascotas')    

class MascotasIdResouce(Resource):
    def get(self,idMascota):
        mascota = Mascota.get_by_id(idMascota)
        if not mascota: 
            respuesta ={'state':'fail',
                        'message':'Mascota no encontrada'}
            return respuesta,401
        respuesta = mascotas_schema.dump(mascota)
        return respuesta,201
    
    @token_required
    def put(self,current_user,idMascota):
        put_data = request.get_json()
        mascota = Mascota.get_by_id(idMascota)
        
        @token_required
        def get_user(request):
            return request
        user = get_user()
        if user == mascota.usuario:
            try:
                instance = Mascota.query.filter(Mascota.idMascota == mascota.idMascota)                
                instance.update(dict(put_data))
                mascota.update_db()
                response_object ={
                    'status':'aceptada',
                    'message':'Cambios registrados adecuadamente'
                }
                return response_object,201
            except Exception as e:
                response_object ={
                    'status':'fail',
                    'message':error
                }
                print(e)
                return response_object,500
        else:
            response_object ={
                    'status':'fail',
                    'message':'La mascota no le pertenece, procedimiento no autorizado'
                }
            return response_object,401
    
    @token_required    
    def delete(self,current_user,idMascota):
        mascota = Mascota.get_by_id(idMascota)
        @token_required
        def get_user(request):
            return request
        user = get_user()
        if mascota and user == mascota.usuario:
            try:
                mascota.delete()
                response_object ={
                    'status':'aceptada',
                    'message':'La mascota ha sido eliminada con exito',
                    'data':mascotas_schema.dump(mascota)
                }
                return response_object,201
            except Exception as e:
                response_object ={
                'status':'fail',
                'message':error
                }
                print(e)
                return response_object,500
        else:
            response_object ={
                'status':'fail',
                'message':'La mascota no existe o el usuario no tiene permiso para eliminarlo'
                }
            return response_object,401
        
api.add_resource(MascotasIdResouce,'/mascotas/<int:idMascota>',endpoint='registro_mascota_id')          

class ReportesResource(Resource):
    def get(self):
        reporte = Reportes.get_all()
        resultado = reportes_schema.dump(reporte,many=True)
        if not resultado:return {"message":"No se encontraron reportes"},204
        return resultado,201
    
    @token_required
    def post(self,current_user):
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
                    'message':'Nuevo reporte creado',
                    'data':reportes_schema.dump(nuevo_reporte)
                }
                return response_object,201
            except Exception as e:
                response_object ={
                    'status':'fail',
                    'message':error
                }
                print(e)
                return response_object,500
        else:
            response_object ={
                    'status':'fail',
                    'message':'El reporte ya existe!'
                }
            return response_object,401
               
api.add_resource(ReportesResource,'/reportes',endpoint='registro_reportes') 


class ReporteIdResource(Resource):
    def get(self,idReporte):
        reporte = Reportes.get_by_id(idReporte)
        resultado = reportes_schema.dump(reporte)
        return resultado,201
    
    @token_required
    def put(self,current_user,idReporte):
        reporte = Reportes.get_by_id(idReporte)
        put_data = request.get_json()
        @token_required
        def get_user(request):
            return request
        user = get_user()
        print(reporte.mascota,user.mascota)
        if reporte.mascota in user.mascota:
            try:
                instance = Reportes.query.filter(Reportes.idReporte == reporte.idReporte)                
                instance.update(dict(put_data))
                reporte.fecha = date.today()
                reporte.update_db()
                response_object ={
                    'status':'aceptada',
                    'message':'Reporte modificado con exito',
                    'data':reportes_schema.dump(reporte)
                }
                return response_object,201
            except Exception as e:
                response_object ={
                'status':'fail',
                'message':error
                }
                print(e)
                return response_object,401
        else:
            response_object ={
                'status':'fail',
                'message':'La mascota no le pertenece'
            }
            return response_object,401
    
    @token_required    
    def delete(self,current_user,idReporte):
        reporte = Reportes.get_by_id(idReporte)
        if reporte and current_user:
            try:
                reporte.delete()
                response_object ={
                    'status':'aceptada',
                    'message':'El reporte ha sido eliminado con exito',
                    'data':reportes_schema.dump(reporte)
                }
                return response_object,201
            except Exception as e:
                response_object ={
                'status':'fail',
                'message':error
                }
                print(e)
                return response_object,500
        else:
            response_object ={
                'status':'fail',
                'message':'El reporte no existe o el usuario no tiene permiso para eliminarlo'
                }
            return response_object,401
            
api.add_resource(ReporteIdResource,'/reportes/<int:idReporte>',endpoint='registro_reportes_id')        

class EspecieResouce(Resource):
    def get(self):
        especies = Especie.get_all()
        resultado = especie_schema.dump(especies,many=True)
        return resultado,201
api.add_resource(EspecieResouce,'/especies',endpoint='get_especie')  

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
        return resultado,201
api.add_resource(DepartamentosResouce,'/departamentos',endpoint='get_departamentos')      

class CiudadesResouce(Resource):
    def get(self):
        try:
            ciudad_arg = request.args.get('ciudad')
            # departamento_arg = request.args.get('departamento',default=None)
            # if departamento_arg:
            #     formato = "{}%".format(departamento_arg)
            #     busqueda = Departamento.query.filter(Departamento.depto.ilike(formato)).all()
            #     print(busqueda)
            #     depto = departamentos_schema.load(busqueda)
            #     print(depto.depto)
            #     ciudades = Ciudad.simple_filter(ciudad=ciudad_arg,departamento=busqueda.depto)
            #     resultado = ciudad_schema.dump(ciudades,many=True)
            #     return resultado,201
            
            ciudad = Ciudad.query.filter(Ciudad.ciudad.ilike("{}%".format(ciudad_arg)))
            resultado = ciudad_schema.dump(ciudad, many=True)
            return resultado,201
        except Exception as e:
            return f"Error: {e}"
api.add_resource(CiudadesResouce,'/ciudad',endpoint='listar_ciudades')  

class CiudadeIdResouce(Resource):
    def get(self,id):
        ciudades = Ciudad.get_by_id(id)
        resultado = ciudad_schema.dump(ciudades)
        return resultado,201
api.add_resource(CiudadeIdResouce,'/ciudad/<int:id>',endpoint='get_ciudades')       
