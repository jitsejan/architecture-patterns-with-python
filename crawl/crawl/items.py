import scrapy


class ZeldaItem(scrapy.Item):
    """ Definition of the ZeldaItem """
    name = scrapy.Field()
    price = scrapy.Field()
