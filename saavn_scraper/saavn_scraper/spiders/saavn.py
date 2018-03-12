#-----------------------------------------------------
# Spider for scraping www.saavn.com music site
#-----------------------------------------------------

import scrapy
from scrapy.selector import Selector
from ..itemModels.album import Album


class SaavnSpider(scrapy.Spider):
    name = 'saavn'
    allowed_domains = ['www.saavn.com']


    def __init__(self):
        self.loggerName = self.__class__.__name__

    def start_requests(self):
        yield scrapy.FormRequest('https://www.saavn.com/new-releases/hindi', callback=self.parseAlbums)
        yield scrapy.FormRequest('https://www.saavn.com/radio/hindi', callback=self.parseRadio)

    def showAlbumDetails(self, album):
        self.logger.debug("[%s] ==> Id: %d   Title: '%s' Artist: '%s'" % (self.loggerName, album['num'], album['title'], album['artist']))

    def fetchLatestAlbums(self, text):
        self.logger.debug("[%s]=============================================================" % self.loggerName)
        # fetch albums details
        albumData = Selector(text=text).xpath('//div[contains(@class, "album-details")]').extract()
        for num, album_detail in enumerate(albumData):
            album = Album()
            albm = Selector(text=album_detail)
            album['num'], album['title'], album['artist'] = num+1, albm.xpath('//p/text()').extract_first(), albm.xpath('//span/text()').extract_first()

            self.showAlbumDetails(album)
        self.logger.debug("[%s]=============================================================" % self.loggerName)

    def parseAlbums(self, response):
        self.logger.debug("[%s] Fetching latest movie titles from 'www.saavn.com'" % self.loggerName)
        self.fetchLatestAlbums(response.text)

    # method for fetching radio list
    def parseRadio(self, response):
        self.logger.debug("[%s] Fetching latest Radio from 'www.saavn.com'" % self.loggerName)
        #self.fetchLatestRadio(response.text)