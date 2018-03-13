# -*- coding: utf-8 -*-
import scrapy


class Album(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()

class Radio(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
