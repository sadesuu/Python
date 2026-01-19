from typing import Literal
from pydantic import BaseModel, field_validator

class Perro(BaseModel):
    tipo: str
    name: str
    edad: int
    sexo: Literal["Macho", "Hembra"] = "Macho"
    
    def ladrar(self):
        return "Guau Guau"
    
    def paseo(self, pasos):
        return f"El perro ha dado {pasos} pasos durante el paseo."
    
    @property
    def get_tipo(self):
        return self.tipo
    
    @property
    def get_name(self):
        return self.name



miPerro = Perro(tipo="Pastor Alemán", name="Rex", edad=12, sexo="Macho")
print(f"Mi perro es un {miPerro.get_tipo} y se llama {miPerro.get_name} y su edad es {miPerro.edad} años y su sexo es {miPerro.sexo}.")
print(miPerro.ladrar())
print(miPerro.paseo(1000))