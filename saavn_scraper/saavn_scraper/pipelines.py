# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from itemModels.album import *

output_album_json = 'output/album.json'



class SaavnPipeline(object):



    def open_spider(self, spider):
        print("opening spider...")
        self.album_file= open(output_album_json, 'wb')
        self.radio_file = open(output_radio_json, 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"

        return item

    def close_spider(self, spider):
        print('closing spider..')

