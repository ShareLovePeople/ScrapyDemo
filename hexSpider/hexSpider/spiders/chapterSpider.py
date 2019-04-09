# -*- coding: utf-8 -*-
import scrapy


class ChapterspiderSpider(scrapy.Spider):
    name = 'chapterSpider'
    allowed_domains = ['haxtxt.net']
    start_urls = ['https://www.haxtxt.net/files/article/html/209/209171/67721909.html']

    def parse(self, response):
        from hexSpider.items import ChapterItem
        item = ChapterItem()
        item["name"] = response.xpath("//div[@id='BookCon']/h1/text()").extract_first()
        item["content"] = "".join(response.xpath("//div[@id='BookText']/text()").extract())

        yield item
        urls = response.xpath("//div[@class='link xb']/a")

        next_url = ""
        for a in urls:
            text = a.xpath("text()").extract_first()

            if "下一页" == text:
                next_url = "https://www.haxtxt.net" + str(a.xpath("@href").extract_first())
                break

        if next_url.strip() != "":
            yield scrapy.Request(url=next_url, callback=self.parse)
