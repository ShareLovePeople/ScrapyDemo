# -*- coding: utf-8 -*-
import scrapy

#创建爬虫               爬虫名  爬取范围
# scrapy genspider itcast itcast.cn
class ItcastSpider(scrapy.Spider):
    name = 'itcast'  #爬虫名
    allowed_domains = ['itcast.cn']  #爬取点域名访问
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
