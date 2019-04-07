# -*- coding: utf-8 -*-
import scrapy

from myspider.myspider.items import SunspiderItem

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0869.com']
    start_urls = ['http://www.sun0769.com/']

    def parse(self, response):
        item = SunspiderItem()
        pass
