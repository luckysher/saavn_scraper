# -*- coding: utf-8 -*-
import scrapy


class SaavnSpider(scrapy.Spider):
    name = 'saavn'

    def start_requests(self):
        urls = ['http://www.saavn.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("response from saavn:", response)
        log()
