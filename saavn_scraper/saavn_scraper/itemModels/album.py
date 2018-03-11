# -*- coding: utf-8 -*-
import scrapy


class Album(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()

