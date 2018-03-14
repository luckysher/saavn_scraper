# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

output_json = 'output/album.json'

class AlbumPipeline(object):

    def open_spider(self, spider):
        print("opening spider...")
        self.file = open(output_json, 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        print('closing spider..')
        self.file.close()
