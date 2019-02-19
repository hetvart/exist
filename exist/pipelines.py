# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

from scrapy.exporters import JsonItemExporter


class AlignScrapedDataPipeline(object):
    def process_item(self, item, spider):
        # replacing all non-digital characters to get clear price values
        item['Prices'] = [re.sub(r'\D', '', price) for price in item['Prices']]
        item['Items Available'] = [re.sub(r'\D', '', item) for item in item['Items Available']]
        return item


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        file_name_from_settings = spider.settings.get('FILE_NAME')
        file_name = file_name_from_settings if file_name_from_settings else '%s.json' % spider.name
        ensure_ascii = spider.settings.get('ENSURE_ASCII', True)
        encoding = spider.settings.get('ENCODING', 'utf-8')
        self.file = open(file_name, 'wb')
        self.exporter = JsonItemExporter(file=self.file, encoding=encoding, ensure_ascii=ensure_ascii)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.exporter.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
