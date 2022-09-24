import datetime
from ..model.conexion import conectar

# fecha = datetime.date.strftime(datetime.date.today(),'%d,%m,%Y')


def test_conexion():
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute('Select database();')
        rta = cur.fetchone()
        return(rta)
    

print(test_conexion())