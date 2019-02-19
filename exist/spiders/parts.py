import scrapy

from exist.items import CarPart, CartPartItemLoader


class PartsSpider(scrapy.Spider):
    name = 'car_parts'

    def __init__(self, part_codes=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._url_pattern = 'https://exist.ua/price.aspx?pcode={part_code}'
        self.start_urls = [self._url_pattern.format(part_code=pcode) for pcode in part_codes.split(',')]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.css('#priceBody .rowOffers')
        for row in rows:
            loader = CartPartItemLoader(item=CarPart(), selector=row)
            loader.add_css('brand', '.art::text')
            loader.add_css('part_code', '.partno::text')
            loader.add_css('name', '.descr::text')
            loader.add_css('prices', '.all-offers .price::text')
            loader.add_css('dates', '.all-offers .stock-info p::text')
            loader.add_css('items_amount', '.all-offers .avail::text')
            yield loader.load_item()
