# -*- coding: utf-8 -*-
import logging

import scrapy

logger = logging.getLogger(__name__)
# 创建爬虫               爬虫名  爬取范围
# scrapy genspider itcast itcast.cn

# scrapy crawl  itcast  使用该爬虫爬取



class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求点URL地址

    def parse(self, response):
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        li_list = response.xpath("//div[@class='tea_con']//li")


        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract()[0]
            item["title"]=li.xpath(".//h4/text()").extract_first()
            yield  item #将解析的数据放入管道进行下一步处理

        logging.warning("打印WARNING级别信息")
        logger.warning("打印WARNING级别信息") #建议使用这种