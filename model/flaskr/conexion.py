#se importa las librerias a utilizar, mysql.connector para conexion y Error para manejo de errores
import mysql.connector 
from mysql.connector import Error
from constantes import host,database_name,user,mysql_pass

def conectar():
    #bloque de try-except para manejo de errores de conexion
    try:
        return mysql.connector.connect(host=host,
                                   database=database_name,
                                   user=user,
                                   password=mysql_pass,
                                   port=3306)
    except Error as e:
        return e
    
