from dataclasses import dataclass
from datetime import date

@dataclass
class usuario:
    id_usuario:int
    nombre:str
    apellido_p:str
    apellido_m:str
    telefono:str
    fecha_actualizacion:date
    correo:str
    token:str
    id_ciudad:int