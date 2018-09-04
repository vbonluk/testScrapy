# encoding:UTF-8
from scrapy.spiders import Spider
import requests

class spider(Spider):
    name = 'hpv9'
    start_urls = [
        'http://www.kwh.org.mo/'
    ]

    def __init__(self):
        pass

    def parse(self, response):
        titles = response.xpath('//b').extract()
        for title in titles:
            text = title.strip()
            print(text)