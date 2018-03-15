#-----------------------------------------------------
# Spider for scraping www.saavn.com music site
#-----------------------------------------------------

import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from ..itemModels.album import *


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

    def showRadioDetails(self, radioDetails):
        for num, radioDetail in enumerate(radioDetails.get("name")):
            self.logger.debug("[%s] ==>  Id:%d,   Name: '%s'" % (self.loggerName, num+1, str(radioDetail)))

    def fetchLatestAlbums(self, text):
        self.logger.debug("[%s]=============================================================" % self.loggerName)
        albumList = []
        # fetch albums details
        albumData = Selector(text=text).xpath('//div[contains(@class, "album-details")]').extract()
        for num, album_detail in enumerate(albumData):
            album = Album()
            albm = Selector(text=album_detail)
            # load data to items
            album['num'], album['title'], album['artist'] = num+1, albm.xpath('//p/text()').extract_first(), albm.xpath('//span/text()').extract_first()
            albumList.append(album)
            self.showAlbumDetails(album)
        self.logger.debug("[%s]=============================================================" % self.loggerName)
        return albumList

    def parseAlbums(self, response):
        self.logger.debug("[%s] Fetching latest movie titles from 'www.saavn.com'" % self.loggerName)
        albumList = self.fetchLatestAlbums(response.text)
        for album in albumList:
            yield album

    def fetchLatestRadio(self, response):
        self.logger.debug("[%s]=====================Saavn Radio list ========================================" % self.loggerName)
        # fetch albums details
        loader = ItemLoader(item=Radio(), response=response)
        radioLoader = loader.nested_xpath('//div[contains(@class, "album-details")]')
        radioLoader.add_xpath('name', 'p/text()')
        loadedRadios = radioLoader.load_item()
        self.showRadioDetails(loadedRadios)
        self.logger.debug("[%s]=============================================================" % self.loggerName)

    # method for fetching radio list
    def parseRadio(self, response):
        self.logger.debug("[%s] Fetching latest Radio from 'www.saavn.com'" % self.loggerName)
        self.fetchLatestRadio(response)

