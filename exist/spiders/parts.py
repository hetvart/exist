import scrapy


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
        rows_dicts = [self.get_row_as_dict(row) for row in rows]

        for row in rows_dicts:
            yield row

    @staticmethod
    def get_row_as_dict(row):
        brand = row.css('.art::text').get()
        part_code = row.css('.partno::text').get()
        name = row.css('.descr::text').get()
        dates = row.css('.all-offers .stock-info p::text').getall()
        prices = row.css('.all-offers .price::text').getall()
        items_available = row.css(' .all-offers .avail::text').getall()
        return {
            'Brand': brand,
            'Part Code': part_code,
            'Part Name': name,
            'Prices': prices,
            'Dates': dates,
            'Items Available': items_available
        }
