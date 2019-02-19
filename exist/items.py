# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, Compose, Identity


def align_int_values(values):
    a = [re.sub(r'\D', '', val) for val in values]
    return [int(i) for i in a]


class CarPart(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    part_code = scrapy.Field()
    prices = scrapy.Field()
    dates = scrapy.Field()
    items_amount = scrapy.Field()


class CartPartItemLoader(ItemLoader):
    default_output_processor = Join()
    prices_out = Compose(align_int_values)
    items_amount_out = Compose(align_int_values)
    dates_out = Identity()
