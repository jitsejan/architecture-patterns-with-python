import scrapy



class ZeldaItemsSpider(scrapy.Spider):
    name = 'zelda_items'
    base_url = "http://zelda.gamepedia.com"
    allowed_domains = ['zelda.gamepedia.com']
    start_urls = [f'{base_url}/Items_in_The_Legend_of_Zelda']

    def parse(self, response):
        selector = "li.gallerybox .gallerytext p a::attr(href)"
        for href in response.css(selector).extract():
            yield scrapy.Request(f"{self.base_url}{href}",
                                 callback=self.parse_item)

    def parse_item(self, response):
        try:
            name = response.css("meta[property='og:title']::attr(content)").get()
            price = int(response.xpath("//tr[th//text()[contains(., 'Cost(s)')]]/td/div/text()").get())
            yield {
                'name': name,
                'price': price
            }
        except:
            pass # No price given
