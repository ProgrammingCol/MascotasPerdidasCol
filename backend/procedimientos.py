from hashlib import sha256
from conexion import conectar
import datetime

#Login y registro hechos
def registrar_usuario(nombre: str, apellidoP: str, apellidoM: str, telefono: str, correo: str ,passwd:str, ciudad:str):
    '''Registra un usuario, retorna True si fue adecuadamente aceptado o False y error'''
    #entra a un ciclo try-except por si no se logra la conexion
    try: 
        #Se construye la peticion a la base de datos
        query = """INSERT INTO usuario VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        #Se realiza un cifrado sencillo de la contraseña
        passwd = sha256(passwd.encode('utf-8')).hexdigest()
        #Se toma la fecha actual del registro
        fecha = datetime.date.strftime(datetime.date.today(),'%Y,%m,%d')
        #Se inician los valores para la peticion
        values = [nombre,apellidoP,apellidoM,telefono,fecha,correo,passwd,ciudad]
        
        #Se inicia el with para mantener cerradas las conexiones a base de datos en caso de error
        #Se ejecuta la petición
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
        return 'Usuario registrado correctamente'
    except Exception as e:
        return e

def auth(email,password):
    '''audita a una persona, devuelve un id si funciona, None si no'''
    try:
        query = """SELECT id_usuario
        FROM usuario
        WHERE correo = %s AND token = %s"""
        with conectar() as conn:
            cursor = conn.cursor()
            password = sha256(password.encode('utf-8')).hexdigest()
            cursor.execute(query,[email,password])
            respuesta = cursor.fetchone()
            if respuesta: return respuesta[0]
            else: return cursor.fetchone()
            
    except Exception as e:
        return [False,e]

def ingresar_usuario(email, password):
    autorizacion = auth(email,password)
    
    if autorizacion:
        return True
    else:
        return False
    
def modificar_contraseña(email,old_password,new_password):
    try:
        #plantilla de query
        query = """UPDATE usuarios 
        SET password = %s
        WHERE id = %s"""
        
        #coneccion y ejecucion
        with conectar() as conn:
            pase = auth(email,old_password)
            if pase:
                values = [new_password,pase]
                cursor = conn.cursor()
                cursor.execute(query,values)
                return True
            else: 
                return False
    except Exception as e:
        return [False,e]
    

#Procesos de base de datos
def listar_usuarios():
    '''Genera una lista de tuplas con los usuarios actuales'''
    try:
        query = """SELECT id, email, tipo FROM usuarios"""
        
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
    except Exception as e:
        return [False,e]

def cargar_datos(nombre_tabla,datos:list, columnas:str = None):
    with conectar() as conn:
        cursor= conn.cursor()
        if datos is list:
            lis = ['%s' for _ in range(len(datos))]
            cantidad = ','.join(lis)  
        else:
            cantidad = '%s'
          
        query = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({cantidad})"
        print(query)
        cursor.execute(query)
        conn.commit()

def listar_mascotas():
    '''Lista todas las mascotas y las carga en forma de diccionario/JSON'''
    pass

def registrar_mascota():
    ''''adquiere los datos de una mascota encontrada/perdida y la almacena en base de datos'''
    pass
    
# registrar_usuario('maria del pilar','cardozo','galvis','3187412133','mpcardozo2004@yahoo.es','maria123','1')
print(auth('mpcardozo2004@yahoo.es','maria123'))