import mysql.connector 
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(host='localhost',
                                   database='mascotas',
                                   user='root',
                                   password='pach5321')
    
conectar()

    
