#-----------------------------------------------------
# Spider for scraping www.saavn.com music site
#-----------------------------------------------------

import scrapy
from scrapy.selector import Selector
from ..itemModels.album import Album


class SaavnSpider(scrapy.Spider):
    name = 'saavn'
    allowed_domains = ['www.saavn.com']
    start_urls = ['https://www.saavn.com/new-releases/hindi']

    def __init__(self):
        self.loggerName = self.__class__.__name__

    def showAlbumDetails(self, album):
        self.logger.debug("[%s] ==> Id: %d   Title: '%s' Artist: '%s'" % (self.loggerName, album['num'], album['title'], album['artist']))

    def fetchLatestAlbums(self, text):
        self.logger.debug("[%s]=============================================================" % self.loggerName)
        # fetch albums details
        albumData = Selector(text=text).xpath('//div[contains(@class, "album-details")]').extract()
        for num, album_detail in enumerate(albumData):
            album = Album()
            albm = Selector(text=album_detail)
            self.showAlbumDetails(album)
        self.logger.debug("[%s]=============================================================" % self.loggerName)

    def parse(self, response):
        self.logger.debug("[%s] Fetching latest movie titles from 'www.saavn.com'" % self.loggerName)
        self.fetchLatestAlbums(response.text)