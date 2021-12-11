from typing import Optional
from pydantic import BaseModel

class Peliculas(BaseModel):
    Id: int[Optional]
    Nombre: str
    Fecha: str
    Comentario: str

class PokemonAdd(Peliculas):
    Id: int[Optional]
    Nombre: str
    Fecha: str
    Comentario: Optional[str] = None

    class Config:
        orm_mode = True


class Peliculas(Peliculas):
    Id: int[Optional]

    class Config:
        orm_mode = True


class UpdatePeliculas(BaseModel):

    Id: int
    Nombre: str
    Fecha: str
    Comentario: str

    class Config:
        orm_mode = True