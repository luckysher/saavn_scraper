# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class SaavnSpider(scrapy.Spider):
    name = 'saavn'
    allowed_domains = ['https://www.saavn.com']
    start_urls = ['https://www.saavn.com/']

    def __init__(self):
        self.loggerName = self.__class__.__name__

    def fetchLatestMovieTitles(self, text):
        num = 0
        title = ""
        artist = ""
        # fetch albums details
        albums_text = Selector(text=text).xpath('//div/album-grid').extract()
        albums_details = Selector(text=albums_text).xpath('//div/album-item').extract()
        for album_detail in albums_details:



    def parse(self, response):
        self.logger.debug("[%s] Fetching latest movie titles from 'www.saavn.com'" % self.loggerName)
        self.fetchLatestMovieTitles(response.text)