# -*- coding: utf-8 -*-
import scrapy


class SitemapcrawlerSpider(scrapy.Spider):
    name = 'Sitemapcrawler'
    allowed_domains = ['https://wiprodigital.com']
    start_urls = ['http://https://wiprodigital.com/']

    def parse(self, response):
        pass
