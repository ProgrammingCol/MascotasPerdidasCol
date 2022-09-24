from VO.mascota import Mascota
from mysql.connector import Error
from conexion import conectar

def registrar_mascota(mascota:Mascota):
    ''''adquiere los datos de una mascota encontrada/perdida y la almacena en base de datos'''
    try: 
        #Se construye la peticion a la base de datos.
        query = """INSERT INTO mascota VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        #Se inician los valores para la peticion
        raza = f"(SELECT id_raza FROM raza WHERE raza ilike {mascota.raza})"
        sexo = f"(SELECT id_sexo FROM sexo WHERE sexo ilike {mascota.sexo})"
        ciudad = f"(SELECT idciudad FROM ciudad WHERE ciudad ilike {mascota.ciudad})"
        especie = f"(SELECT id_especie FROM especie WHERE especie ilike {mascota.especie})"
        foto_binaria = to_binary(mascota.ubicacion_foto)
        
        values = [raza,sexo,mascota.nombre,mascota.descripcion,foto_binaria,mascota.estado,mascota.id_usuario,ciudad,especie]
        
        #Se inicia el with para mantener cerradas las conexiones a base de datos en caso de error
        #Se ejecuta la petición
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
        return 'Mascota registrada correctamente'
    except Error as e:
        return e
    
def to_binary(archivo):
    '''Lee un archivo y lo convierte en binario'''
    try:
        with open(archivo,'rb') as data:
            data_binario = data.read()
            return data_binario
    except Exception as e:
        return e
