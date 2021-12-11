
from sqlalchemy.orm import Session
import Models.peliculas
import Schemas.peliculas


def get_peliculas_by_peliculas_id(db: Session, id: int):
 
    return db.query(Models.peliculas).filter(Models.peliculas.id == id).first()


def get_peliculas_by_id(db: Session, id: int):

    return db.query(Models.peliculases).filter(Models.peliculas.id == id).first()


def get_peliculas(db: Session, skip: int = 0, limit: int = 100):
 
    return db.query(Models.peliculas).offset(skip).limit(limit).all()


def add_peliculas_details_to_db(db: Session, peliculas: Models.peliculasAdd):
 
    mv_details = Models.peliculas(
        Id=peliculas.Id,
        Nombre=peliculas.Nombre,
        Fecha=peliculas.Fecha,
        Comentario=peliculas.Comentario,
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return Models.peliculas(**peliculas.dict())


def update_peliculas_details(db: Session, id: int, details: Schemas.Updatepeliculas):
 
    db.query(Models.peliculas).filter(Models.peliculas.id == id).update(vars(details))
    db.commit()
    return db.query(Models.peliculases).filter(Models.peliculas.id == id).first()


def delete_peliculas_details_by_id(db: Session, id: str):

    try:
        db.query(Models.Movies).filter(Models.peliculas.id == id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)