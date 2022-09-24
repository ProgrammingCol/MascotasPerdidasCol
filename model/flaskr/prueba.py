from VO.mascota import Mascota
from DAO.mascota_dao import registrar_mascota
import conexion as connect
from DAO.mascota_dao import to_binary

lucas = Mascota('akita','macho','lucas','con collar','/Users/pacho/Downloads/Beagle-standing-in-a-frosty-field-on-a-cold-morning.jpg','perdido',1,'leticia','perro')
registrar_mascota(lucas)

# with connect.conectar() as conn:
#     cur = conn.cursor()
#     cur.execute('SELECT foto from mascota where nombre ="lucas"')
#     print(cur.fetchone())

print(to_binary('/Users/pacho/Downloads/Beagle-standing-in-a-frosty-field-on-a-cold-morning.jpg'))
print(lucas.ubicacion_foto)