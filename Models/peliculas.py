from sqlalchemy import Column, Integer, String
from Config.peliculas import Base

class Peliculas(Base):

    __tablename__ = "peliculas"
    Id = Column(Integer, index=True, nullable=False)
    Nombre = Column(String(15), primary_key=True, unique=True, index=True, nullable=False)
    Fecha = Column(String(30), index=True, nullable=False)
    Comentario = Column(String(100), index=True, nullable=False)
