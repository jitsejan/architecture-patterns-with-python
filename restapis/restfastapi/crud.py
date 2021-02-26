from sqlalchemy.orm import Session

from . import schemas
from .models import Item


def get_item_by_name(db: Session, name: str):
    return db.query(Item).filter(Item.name == name).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()
