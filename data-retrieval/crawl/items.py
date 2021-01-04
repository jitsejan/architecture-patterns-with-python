"""crawl/crawl/items.py"""
from scrapy import Field, Item


class ZeldaItem(Item):
    """ Definition of the ZeldaItem """

    name = Field()
    price = Field()
