# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SitemapCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # stores url
    url = scrapy.Field(serializer=str)
    # list of external Urls
    external_urls = scrapy.Field(serializer=list)
    # list of Static Urls
    static_urls = scrapy.Field(serializer=list)
    # list of available urls
    urls = scrapy.Field(serializer=list)
