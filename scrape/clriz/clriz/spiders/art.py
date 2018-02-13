# -*- coding: utf-8 -*-
import scrapy


class ArtSpider(scrapy.Spider):
    name = 'art'
    allowed_domains = ['https://newyork.craigslist.org/search/sss']
    start_urls = ['http://https://newyork.craigslist.org/search/sss/']

    def parse(self, response):
        pass
