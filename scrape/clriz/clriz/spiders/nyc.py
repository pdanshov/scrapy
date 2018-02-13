# -*- coding: utf-8 -*-
import scrapy


class NycSpider(scrapy.Spider):
    name = 'nyc'
    allowed_domains = ['https://newyork.craigslist.org/search/sss']
    start_urls = ['http://https://newyork.craigslist.org/search/sss/']

    def parse(self, response):
        pass
