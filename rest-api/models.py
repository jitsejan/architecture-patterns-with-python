from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ItemsModel(db.Model):
    """
    Defines the items model
    """

    __tablename__ = "items"

    name = db.Column("name", db.String, primary_key=True)
    price = db.Column("price", db.Integer)

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
