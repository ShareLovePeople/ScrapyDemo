# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Item作用
# 清理HTML数据
# 验证爬取的数据(检查item包含某些字段)
# 去重(并丢弃)【预防数据去重，真正去重是在url,即请求阶段做】
# 将爬取结果保存到数据库中
from hexSpider.items import FictionItem


class HexspiderPipeline(object):

    def process_item(self, item, spider):
        print(type(item) == FictionItem)  #判断数据的类型
        return item
