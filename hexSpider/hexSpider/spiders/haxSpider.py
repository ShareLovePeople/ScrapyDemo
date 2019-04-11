# -*- coding: utf-8 -*-
import scrapy

from hexSpider.items import FictionItem, ChapterItem

HEXHOST = "https://www.haxtxt.net"

class ChapterspiderSpider(scrapy.Spider):
    name = 'chapterSpider'
    allowed_domains = ['haxtxt.net']
    start_urls = ['https://www.haxtxt.net/']

    def parse(self, response):
        url = "https://www.haxtxt.net/xiaoshuo/20/1.htm"
        yield scrapy.Request(url=url, callback=self.lwlist)
        pass

    def lwlist(self, response):
        """
        抓取小说连接列表
        :param response:
        :return:
        """
        list = response.xpath("//ul[@class='item-con']//span[@class='s2']/a[1]/@href").extract()

        for a in list:
            url = HEXHOST + a
            yield scrapy.Request(url=url, callback=self.finfo)

    def finfo(self, response):
        """
        抓取小说信息页内容
        :param response:
        :return:
        """
        murl = HEXHOST + response.xpath("//div[@class='book-link']/a[2]/@href").extract_first()
        yield scrapy.Request(url=murl, callback=self.fiction)
        pass

    def fiction(self, response):
        """
        抓取小说目录页内容
        :param response:
        :return:
        """
        item = FictionItem()

        item["name"] = response.xpath("//div[@class='btitle']/h1/text()").extract_first()
        item["author"] = response.xpath("//div[@class='btitle']//a/text()").extract_first()
        item["type"] = response.xpath("//div[@class='crumbs']//a[2]/text()").extract_first()
        item["intro"] = "".join(response.xpath("//p[@class='intro']/text()").extract())
        yield item

        first_url = response.xpath("//dl[@class='chapterlist']/dd[1]/a[1]/@href").extract_first()

        first_url = HEXHOST + first_url
        yield scrapy.Request(url=first_url, callback=self.chapter)

        pass

    def chapter(self, response):
        """
        抓取所有章节内容 (循环下一页抓取)
        :param response:
        :return:
        """
        # print(response.meta["meta"])

        item = ChapterItem()
        item["name"] = response.xpath("//div[@id='BookCon']/h1/text()").extract_first()
        item["content"] = "".join(response.xpath("//div[@id='BookText']/text()").extract())

        yield item

        # 开始抓取下一页
        urls = response.xpath("//div[@class='link xb']/a")
        next_url = ""
        for a in urls:
            text = a.xpath("text()").extract_first()

            if "下一页" == text:
                next_url = "https://www.haxtxt.net" + str(a.xpath("@href").extract_first())
                break

        if next_url.strip() != "":
            yield scrapy.Request(url=next_url, callback=self.chapter)
        pass
