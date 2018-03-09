# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class SaavnSpider(scrapy.Spider):
    name = 'saavn'
    allowed_domains = ['https://www.saavn.com']
    start_urls = ['https://www.saavn.com/']

    def __init__(self):
        self.loggerName = self.__class__.__name__

    def fetchLatestMovieTitles(self):
        pass

    def parse(self, response):
        self.logger.debug("[%s] Response from saavn: %s" % (self.loggerName, response.text))
