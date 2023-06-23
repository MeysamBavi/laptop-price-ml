import scrapy
import logging
from urllib.parse import urlparse
import requests


class LaptopsSpider(scrapy.Spider):
    name = "laptops"

    def __init__(self, links_file='./links.txt', **kwargs):
        super().__init__(**kwargs)
        self.links_file = links_file

    def start_requests(self):
        links = open(self.links_file)
        urls = links.readlines()
        for i in range(len(urls)):
            if i > 0 and i % 50 == 0:
                self.log(f'crawled {i} pages', level=logging.INFO)
            yield scrapy.Request(
                url=urls[i],
            )

    def parse(self, response):
        purl = urlparse(response.url)
        laptop_id = purl.path.split('/')[2]

        json_data = requests.get(f'https://api.torob.com/v4/base-product/details-log-click/?prk={laptop_id}').json()

        result = {'clean-' + k: v for k, v in json_data['attributes'].items()}
        result['id'] = laptop_id
        result['title'] = response.css('.name h1::text').get()

        price = json_data.get('price_text')
        if not price:
            price = json_data.get('price')
        result['price'] = price

        for detail in response.css('div.header ~ div'):
            feature = detail.css('.detail-title::text').get()
            value = detail.css('.detail-value::text').get()
            result[feature] = value

        yield result
