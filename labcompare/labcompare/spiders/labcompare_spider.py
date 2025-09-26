# -*- coding: utf-8 -*-
#https://docs.scrapy.org/en/latest/intro/tutorial.html

from pathlib import Path
import scrapy
import unicodedata
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
import re
#from patentes.items import PatentesItem

from scrapy.http import Response, Request


class QuotesSpider(scrapy.Spider):
    name = 'labcompare'
    allowed_domains = ['www.labcompare.com']

    start_urls = [
        "https://www.labcompare.com/",
        "https://www.labcompare.com/2-Lab-Products/",
        "https://www.labcompare.com/Spectroscopy/106-Spectrophotometer/"
    ]

    rules = [Rule (LinkExtractor(allow=(r".*", ),
                                     restrict_xpaths=('//div[@class="title"]/div[@class="product-name"]/h3/a',))
             , follow= True),  
             Rule(LinkExtractor(allow=['www.labcompare.com'],
                                    restrict_xpaths=('//div/h3/a',)),
                                    callback='parse_item')]


    def parse(self, response):
        yield {
            "title": response.xpath("//li/span[itemprop='name']/text()").get(),
            "manufacturer": response.xpath("//li/span[itemprop='nufacturer']/text()").get(),
            "sku": response.xpath("//li/span[itemprop='sku']/text()").get(),
        }
        next_page = response.xpath("//li/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

