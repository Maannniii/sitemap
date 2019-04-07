# -*- coding: utf-8 -*-

from json import dumps

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from sitemap_crawler import settings


class SitemapCrawlerPipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(settings.DB_HOST, settings.DB_USER, settings.DB_PASSWORD, settings.DB_NAME)
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        # comment following 3 lines to stop clearing the existing data in DB
        self.cursor.execute("truncate sitemap")
        self.cursor.execute("alter table sitemap auto_increment=1")
        self.connection.commit()

    def process_item(self, item, spider):
        sql = "insert ignore into sitemap(url,external_urls,static_urls,urls) values('{}','{}','{}','{}')"
        try:
            formatted_sql = sql.format(dumps(item['url']), dumps(item['external_urls']), dumps(item['static_urls']),
                                       dumps(item['urls']))
            self.cursor.execute(formatted_sql)
        except Exception as e:
            print("Exception occured", e)
        return item

    def close_spider(self, spider):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
