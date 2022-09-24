from ast import Bytes
from dataclasses import dataclass

@dataclass
class Mascota:
    raza:str
    sexo:str
    nombre:str
    descripcion:str
    ubicacion_foto:str
    estado:str
    id_usuario:int
    ciudad:str
    especie:str
    
    def __post_init__ (self):
        pass


