# -*- coding: utf-8 -*-
import scrapy


class SaavnSpider(scrapy.Spider):
    name = 'saavn'
    allowed_domains = ['https://www.saavn.com']
    start_urls = ['https://www.saavn.com/']

    def __init__(self):
        self.loggerName = self.__class__.__name__

    def parse(self, response):
        self.logger.debug("[%s] Response from saavn: %s" % (self.loggerName, response.text))
