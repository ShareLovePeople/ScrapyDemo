# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ChapterItem(scrapy.Item):
    # define the fields for your item here like:
    # 小说章节
    name = scrapy.Field()
    content = scrapy.Field()
    pass


class FictionItem(scrapy.Item):
    # define the fields for your item here like:
    # 小说内容
    name = scrapy.Field()  # 名称
    author = scrapy.Field()  # 作者
    intro = scrapy.Field()  # 简介
    type = scrapy.Field()  # 小说类别
    pass
