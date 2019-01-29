# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:10:53 2019

@author: Razva
"""


import scrapy
from imdb2.items import Imdb2Item
import csv
import re
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request

class ThirdSpider(scrapy.Spider):
    name = "imdbtestspider"
    #allowed_domains = []

    def start_requests(self):
        with open('links.csv') as f:
            for url in f.readlines():
                yield Request(url.strip())

    def parse(self, response):
        item = Imdb2Item()
        item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
        item['production'] = response.xpath('//h4[contains(text(), "Production Co")]/following-sibling::a/text()').extract()
        yield item
		
	