from faker import Faker
# from conexion import conectar
import sys

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix

# lucas = Mascota('akita','macho','lucas','con collar','/Users/pacho/Downloads/Beagle-standing-in-a-frosty-field-on-a-cold-morning.jpg','perdido',1,'leticia','perro')
# registrar_mascota(lucas)


# with connect.conectar() as conn:
#     cur = conn.cursor()
#     cur.execute('SELECT foto from mascota where nombre ="lucas"')
#     print(cur.fetchone())

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
        # cursor.execute(query)
        # conn.commit()
        

# with conectar() as conn:
#     cursor= conn.cursor()        
#     for dato in json:
#         for ciudad in dato['ciudades']:
#             id=int(dato['id'])+1
#             ciudad_prev = ciudad[:9]+'%'
#             if len(ciudad)>10 and id<13:
#                 query = f"UPDATE ciudad SET ciudad = %s where ciudad like %s and iddepto = %s"
#                 cursor.execute(query,(ciudad,ciudad_prev,id))
#                 conn.commit()

# for dato in json:
#     for ciudad in dato['ciudades']:
#         id=int(dato['id'])+1
#         if len(ciudad)>10 and id <13: 
#             print(ciudad,ciudad[:9]+'%', id)
from faker.providers import BaseProvider 

fake = Faker()

print(fake.name(),fake.name(),fake.name(),fake.name())
