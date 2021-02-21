from sqlalchemy import Column, Integer, String
from .database import Base


class Item(Base):
    """
    Defines the items model
    """

    __tablename__ = "items"

    name = Column(String, primary_key=True)
    price = Column(Integer)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"<Item {self.name}>"

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"name": self.name, "price": self.price}
