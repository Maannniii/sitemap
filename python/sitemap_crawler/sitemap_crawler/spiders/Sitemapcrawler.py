# -*- coding: utf-8 -*-
import scrapy,re
from urllib.parse import urlparse,urljoin
from sitemap_crawler.items import SitemapCrawlerItem as Item

class SitemapcrawlerSpider(scrapy.Spider):
    name = 'Sitemapcrawler'
    crawl_start_url = 'https://wiprodigital.com'
    allowed_domains = [crawl_start_url]
    start_urls = [crawl_start_url]
    whitespace_pattern = r"""[\n\t\r\x0b\x0c'"]*"""
    url_details=urlparse(crawl_start_url)

    def parse(self, response):
        item=Item()
        static_urls=set(response.xpath("//*/@src").getall())
        junk_urls=set(response.xpath("//script/@src").getall())
        item['static_urls']=[x for x in map(self.clean,static_urls.difference(junk_urls)) if bool(x)]
        item['url']=self.clean(response.url.strip())
        urls=set(response.xpath('//*/@href').getall())
        urls=set(map(self.remove_same_pages,urls))
        external_urls=set(filter(lambda x: urlparse(x).netloc!=self.url_details.netloc ,urls))
        urls=[x for x in map(self.clean,urls.difference(external_urls).difference({response.url,self.crawl_start_url})) if bool(x)]
        urls=[] if len(urls)==0 else [urls[0]]
        external_urls=[x for x in map(self.clean,external_urls) if bool(x)]
        item['external_urls']=external_urls
        item['urls'] = urls
        for url in urls:
            yield response.follow(url, callback=self.parse)
        yield item
        
    def clean(self,data):
         return re.sub(self.whitespace_pattern,'',data).strip()

    def remove_same_pages(self,x):
         return x.split('#')[0]
