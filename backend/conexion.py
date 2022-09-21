#se importa las librerias a utilizar, mysql.connector para conexion y Error para manejo de errores
import mysql.connector 
from mysql.connector import Error

def conectar():
    #bloque de try-except para manejo de errores de conexion
    try:
        return mysql.connector.connect(host='localhost',
                                   database='mascotas',
                                   user='mascotas',
                                   password='mascotas123')
    except Error as e:
        return e
    

    
# user='pruebas_mascotas',
#                                    password='mascotas123'