"""crawl/crawl/spiders/zelda_items.py"""
from scrapy import Request, Spider


class ZeldaItemsSpider(Spider):
    """
    Defines the ZeldaItemsSpider
    """

    name = "zelda_items"
    base_url = "http://zelda.gamepedia.com"
    allowed_domains = ["zelda.gamepedia.com"]
    start_urls = [f"{base_url}/Items_in_The_Legend_of_Zelda"]

    def parse(self, response):
        """
        Retrieve the links to the items
        """
        selector = "li.gallerybox .gallerytext p a::attr(href)"
        for href in response.css(selector).extract():
            yield Request(f"{self.base_url}{href}", callback=self.parse_item)

    def parse_item(self, response):
        """
        Retrieve the item details
        """
        name_sel = "meta[property='og:title']::attr(content)"
        price_sel = "//tr[th//text()[contains(., 'Cost(s)')]]/td/div/text()"
        name = response.css(name_sel).get()
        price = response.xpath(price_sel).get()
        if price and price.strip().isdigit():
            yield {"name": name, "price": int(price)}
