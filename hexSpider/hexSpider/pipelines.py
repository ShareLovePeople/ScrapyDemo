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
        """
        必须实现：对Item进行处理
        :param item:
        :param spider:
        :return:
        """
        print(type(item) == FictionItem)  #判断数据的类型
        return item

    def from_crawler(self, cls, crawler):
        """
        不必须：启用spider时候执行，早于open
        :param cls:
        :param crawler:
        :return:
        """
        pass

    def open_spider(self, spider):
        """
        不必须：打开spider时候执行,一般进行一些初始化操作，如连接数据库
        :param spider:
        :return:
        """
        print("open_spider")
        pass

    def close_spider(self, spider):
        """
        不必须：关闭spider时候执行，一般进行一些收尾操作，如关闭数据库
        :param spider:
        :return:
        """
        print("close_spider")
