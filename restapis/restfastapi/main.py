from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/", response_model=List[schemas.ItemBase])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return [i.serialize for i in items]


@app.get("/items/{name}", response_model=schemas.ItemBase)
def read_item(name: str, db: Session = Depends(get_db)):
    item = crud.get_item_by_name(db, name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.serialize
