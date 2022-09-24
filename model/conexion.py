#se importa las librerias a utilizar, mysql.connector para conexion y Error para manejo de errores
import mysql.connector 
from mysql.connector import Error
from VO.constantes import host,database_name,user,mysql_pass

def conectar():
    #bloque de try-except para manejo de errores de conexion
    try:
        return mysql.connector.connect(host='localhost',
                                   database='mascotas',
                                   user='root',
                                   password='pach5321',
                                   port=3306)
    except Error as e:
        return e
    
