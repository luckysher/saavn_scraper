# -*- coding: utf-8 -*-
import scrapy


# Album item
class Album(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()


# Radio Item
class Radio(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
