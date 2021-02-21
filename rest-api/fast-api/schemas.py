from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: int
