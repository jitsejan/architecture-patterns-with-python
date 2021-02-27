from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore

from . import crud, models
from .database import SessionLocal, engine
from .schemas import ItemBase

models.Base.metadata.create_all(bind=engine)
itemrouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@itemrouter.get("/items/", response_model=List[ItemBase])
def read_items(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    items = crud.get_items(session=session, skip=skip, limit=limit)
    return [i.serialize for i in items]


@itemrouter.get("/items/{name}", response_model=ItemBase)
def read_item(name: str, session: Session = Depends(get_session)):
    item = crud.get_item_by_name(session=session, name=name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.serialize
