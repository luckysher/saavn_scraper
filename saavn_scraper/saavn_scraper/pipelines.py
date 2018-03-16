# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from itemModels.album import *

output_album_json = 'output/album.json'
output_radio_json = 'output/radio.json'


class SaavnPipeline(object):

    def __init__(self):
        self.radio_file = None
        self.album_file = None

    def open_spider(self, spider):
        print("opening spider...")
        self.album_file= open(output_album_json, 'wb')
        self.radio_file = open(output_radio_json, 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        if isinstance(item, Radio):
            self.radio_file.write(line)
        if isinstance(item, Album):
            self.album_file.write(line)
        return item

    def close_spider(self, spider):
        print('closing spider..')
        self.album_file.close()
        self.radio_file.close()
