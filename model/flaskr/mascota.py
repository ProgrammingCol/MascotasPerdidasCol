from dataclasses import dataclass, field

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
    foto:bytes = field(init=False)
    
    def __post_init__ (self):
        self.ubicacion_foto


