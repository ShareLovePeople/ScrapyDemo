# -*- coding: utf-8 -*-
import scrapy


class ChapterspiderSpider(scrapy.Spider):
    name = 'chapterSpider'
    allowed_domains = ['haxtxt.net']
    start_urls = ['https://www.haxtxt.net/files/article/html/209/209171/67721909.html']

    def parse(self, response):
        print(response.text)
        pass
