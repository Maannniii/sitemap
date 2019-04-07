# -*- coding: utf-8 -*-
from urllib.parse import urlparse, urljoin

import re
import scrapy
from sitemap_crawler.items import SitemapCrawlerItem as Item
from sitemap_crawler.settings import CRAWL_START_URL


class SitemapcrawlerSpider(scrapy.Spider):
    name = 'Sitemapcrawler'
    start_urls = [CRAWL_START_URL]
    whitespace_pattern = r"""[\n\t\r\x0b\x0c'"]*"""
    url_details = urlparse(CRAWL_START_URL)

    def parse(self, response):
        item = Item()
        log = self.logger
        base_url = self.clean(response.url.strip())
        log.info("crawling {}".format(base_url))
        static_urls = set(response.xpath("//*/@src").getall())
        junk_urls = set(response.xpath("//script/@src").getall())
        item['static_urls'] = [urljoin(base_url, x) for x in map(self.clean, static_urls.difference(junk_urls)) if
                               bool(x)]
        item['url'] = base_url
        urls = set(response.xpath('//*/@href').getall())
        urls = set(map(self.remove_same_pages, urls))
        external_urls = set(filter(lambda x: urlparse(x).netloc != self.url_details.netloc, urls))
        urls = [urljoin(base_url, x) for x in
                map(self.clean, urls.difference(external_urls).difference({response.url, CRAWL_START_URL})) if bool(x)]
        # urls = [] if len(urls) == 0 else [urls[0]]
        external_urls = [urljoin(base_url, x) for x in map(self.clean, external_urls) if bool(x)]
        item['external_urls'] = external_urls
        item['urls'] = urls
        for url in urls:
            log.info("Yielding {}".format(url))
            yield response.follow(url, callback=self.parse)
        yield item

    def clean(self, data):
        return re.sub(self.whitespace_pattern, '', data).strip()

    def remove_same_pages(self, x):
        return x.split('#')[0]
