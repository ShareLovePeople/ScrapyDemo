# -*- coding: utf-8 -*-
import scrapy

#创建爬虫               爬虫名  爬取范围
# scrapy genspider itcast itcast.cn

#scrapy crawl  itcast  使用该爬虫爬取
class ItcastSpider(scrapy.Spider):
    name = 'itcast'  #爬虫名
    allowed_domains = ['itcast.cn']  #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']   #最开始请求点URL地址

    def parse(self, response):
        ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        print(ret1)
