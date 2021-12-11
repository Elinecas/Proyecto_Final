from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import Routes.peliculas
import Models.peliculas
import Schemas.peliculas
from Config.peliculas import SessionLocal, engine

Models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Peliculas Details",
    description="Bienvenido a mi CRUD para peliculas",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_pokemon_details', response_model=List[Schemas.Pokemon])
def retrieve_all_pokemon_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pokemon = Routes.get_pokemon(db=db, skip=skip, limit=limit)
    return pokemon


@app.post('/add_new_pokemon', response_model=Schemas.PokemonAdd)
def add_new_pokemon(cedula: Schemas.PokemonAdd, db: Session = Depends(get_db)):
    cedula_id = Routes.get_pokemon_by_pokemon_id(db=db, cedula=cedula.cedula_id)
    if cedula_id:
        raise HTTPException(status_code=400, detail=f"Movie id {cedula.cedula_id} already exist in database: {cedula}")
    return Routes.add_pokemon_details_to_db(db=db, cedula=cedula)


@app.delete('/delete_pokemon_by_id')
def delete_pokemon_by_id(cedula: str, db: Session = Depends(get_db)):
    detalles = Routes.get_pokemon_by_id(db=db, cedula=cedula)
    if not detalles:
        raise HTTPException(status_code=404, detalles=f"No record found to delete")

    try:
        Routes.delete_pokemon_details_by_id(db=db, cedula=cedula)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_pokemon_details', response_model=Schemas.Pokemon)
def update_pokemon_details(cedula: str, update_param: Schemas.UpdatePokemon, db: Session = Depends(get_db)):
    detalles = Routes.get_pokemon_by_id(db=db, cedula=cedula)
    if not detalles:
        raise HTTPException(status_code=404, detalles=f"No record found to update")

    return Routes.update_pokemon_details(db=db, detalles=update_param, cedula=cedula)