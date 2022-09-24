#se importan librerias a utilizar sha256 para proteger contraseñas, conectar para hacer conexion a base de datos, 
#error para manejo de errores y datetime para manejo de fechas
from hashlib import sha256
from conexion import conectar
from mysql.connector import Error
import datetime


#Login y registro
def auth(email,password):#
    '''audita a una persona, devuelve un id y token si funciona, None si no'''
    # ejecuta el codigo en un try-except para manejo de errores
    try:
        # prepara la peticion a la base de datos
        query = """SELECT id_usuario , token
        FROM usuario
        WHERE correo = %s AND token = %s"""
        
        # Se utiliza el with para abrir y cerrar conexion con BD.
        with conectar() as conn:
            # se crea cursor para ejecutar las peticiones
            cursor = conn.cursor(dictionary=True)
            
            # se realiza ocultamiento de contrasena
            password = sha256(password.encode('utf-8')).hexdigest()
            
            # Se ejecuta la peticion
            cursor.execute(query,[email,password])
            
            # Se maneja la respuesta dependiendo de su valor
            respuesta = cursor.fetchone()
            if respuesta: return respuesta
            else: return cursor.fetchone()
            
    except Error as e:
        return [False,e]

def to_binary(archivo):
    '''Lee un archivo y lo convierte en binario'''
    try:
        with open(archivo,'rb') as data:
            data_binario = data.read()
            return data_binario
    except Exception as e:
        return e

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
    except Error as e:
        return e

def ingresar_usuario(email, password):
    '''Se ingresa un correo y una contrase;a, retorna id y token para activar sesion '''
    autorizacion = auth(email,password)
    
    if autorizacion:
        return autorizacion
    else:
        return False
    
def modificar_contraseña(id: int,token: str,new_password: str):
    '''ingresa el id y token del usuario en sesion y la nueva contrase;a, retorna Boleano con resultado de operacion'''
    try:
        #plantilla de query
        query = """UPDATE usuario 
        SET token = %s
        WHERE id_usuario = %s AND token = %s
        """
        
        #coneccion y ejecucion
        with conectar() as conn:
            new_password = sha256(new_password.encode()).hexdigest()
            token = sha256(token.encode()).hexdigest()
            values = [new_password,id,token]
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
            return bool(cursor.rowcount)
    except Error as e:
        return [False,e]

def registrar_mascota(nombre: str,raza: str,sexo: str,estado: str,especie: str,descripcion: str,ciudad: str,id_usuario: int,ubicacion_foto: str): #
    ''''adquiere los datos de una mascota encontrada/perdida y la almacena en base de datos'''
    try: 
        #Se construye la peticion a la base de datos.
        query = """INSERT INTO mascota VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        #Se inician los valores para la peticion
        raza = f"(SELECT id_raza FROM raza WHERE raza ilike {raza})"
        sexo = f"(SELECT id_sexo FROM sexo WHERE sexo ilike {sexo})"
        ciudad = f"(SELECT idciudad FROM ciudad WHERE ciudad ilike {ciudad})"
        especie = f"(SELECT id_especie FROM especie WHERE especie ilike {especie})"
        foto_binaria = to_binary(ubicacion_foto)
        
        values = [raza,sexo,nombre,descripcion,foto_binaria,estado,id_usuario,ciudad,especie]
        
        #Se inicia el with para mantener cerradas las conexiones a base de datos en caso de error
        #Se ejecuta la petición
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
        return 'Mascota registrada correctamente'
    except Error as e:
        return e

def registrar_reporte(fecha:datetime.date,datos_adicionales: str,tipo: str,id_mascota: int):
    #preparacion de peticion
    query = 'INSERT INTO reportes VALUES(%s,%s,%s,%s)'
    #preparar los datos
    fecha = datetime.date.strftime(fecha,'%Y,%m,%d')
    
    values = [fecha,datos_adicionales,tipo,id_mascota]
    #ejecutar la peticion
    try:    
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
        return bool(cursor.rowcount)
    except Error as e:
        return e 
    
#Procesos de base de datos
def listar_usuarios():
    '''Genera un diccionario con los usuarios actuales'''
    try:
        query = """SELECT CONCAT(nombre,' ', apellidoP,' ', apellidoM) AS nombre, telefono,correo,c.ciudad,d.depto
                    FROM usuario 
                    JOIN ciudad c 
                    USING (idciudad)
                    JOIN departamento d
                    USING (iddepto)"""
        
        with conectar() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
    except Error as e:
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
    try:
        with conectar() as conn:
            query='''SELECT
                            m.nombre,
                            s.sexo,
                            r.raza,
                            e.especie ,
                            m.descripcion ,
                            m.estado,
                            m.foto,
                            concat(u.nombre, ' ', u.apellidoP) as usuario,
                            u.telefono ,
                            u.correo
                        FROM
                            mascota m
                        JOIN usuario u
                                USING (id_usuario)
                        JOIN raza r 
                        ON
                            m.raza = r.id_raza
                        JOIN especie e 
                        ON
                            r.especie = e.id_especie
                        JOIN sexo s
                        ON
                            m.sexo = s.id_sexo
                        JOIN ciudad c
                        ON
                            m.id_ciudad = c.idciudad'''
            
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
    except Error as e:
        return e       

    
# registrar_usuario('maria del pilar','cardozo','galvis','3187412133','mpcardozo2004@yahoo.es','maria123','1')
# permiso = auth('mpcardozo2004@yahoo.es','maria123')
# print(modificar_contraseña(1,'maria456','maria123')).


