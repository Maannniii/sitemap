# -*- coding: utf-8 -*-
from urllib.parse import urlparse, urljoin

import re
import scrapy
from sitemap_crawler.items import SitemapCrawlerItem as Item
from sitemap_crawler.settings import CRAWL_START_URL


class SitemapcrawlerSpider(scrapy.Spider):
    name = 'sitemap'

    def __init__(self):
        self.start_urls = map(self.clean,[CRAWL_START_URL])
        self.whitespace_pattern = r"""[\n\t\r\x0b\x0c'"]*"""
        self.url_details = urlparse(CRAWL_START_URL)

    def parse(self, response):
        '''Crawls the url to get list of urls to next pages, urls to other sites, urls to static contents'''
        item = Item()
        log = self.logger
        base_url = self.clean(response.url.strip())
        log.info("crawling {}".format(base_url))
        static_urls = set(response.xpath("//*/@src").getall())
        # script url are considered as junk if needs to be included set junk_urls = {} or junk_urls = set()
        junk_urls = set(response.xpath("//script/@src").getall())
        # generates a list of unique static_urls
        item['static_urls'] = [urljoin(base_url, x) for x in map(self.clean, static_urls.difference(junk_urls)) if
                               bool(x)]
        # Url of the current page
        item['url'] = base_url
        urls = set(response.xpath('//*/@href').getall())
        urls = set(map(self.remove_same_pages, urls))
        external_urls = set(filter(lambda x: urlparse(x).netloc != self.url_details.netloc, urls))
        urls = [urljoin(base_url, x) for x in
                map(self.clean, urls.difference(external_urls).difference({response.url, CRAWL_START_URL})) if bool(x)]
        # urls = [] if len(urls) == 0 else [urls[0]]
        external_urls = [urljoin(base_url, x) for x in map(self.clean, external_urls) if bool(x)]
        # unique list of urls which doesn't belong to crawled domain
        item['external_urls'] = external_urls
        # list of links found in the current page
        item['urls'] = urls
        for url in urls:
            log.info("Yielding {}".format(url))
            yield response.follow(url, callback=self.parse)
        yield item

    def clean(self, data):
        '''removes whitespaces and respective escape sequences. Also removes trailing / at the end'''
        return re.sub(self.whitespace_pattern, '', data).strip().strip("/")

    def remove_same_pages(self, x):
        '''returns url which removes same page urls as #idname point to same pages'''
        return x.split('#')[0]
