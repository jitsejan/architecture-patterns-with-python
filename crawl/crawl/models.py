from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from crawl import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_items_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Items(DeclarativeBase):
    """Defines the items model"""
    __tablename__ = "items"

    name = Column('name', String, primary_key=True)
    price = Column("price", Integer)
