from sqlalchemy import Column, Integer, String
from typing import Dict
from .database import Base


class Item(Base):
    """
    Defines the items model
    """

    __tablename__ = "items"

    name = Column(String, primary_key=True)
    price = Column(Integer)

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"<Item {self.name}>"

    @property
    def serialize(self) -> Dict[str, int]:
        """
        Return item in serializeable format
        """
        return {"name": self.name, "price": self.price}
