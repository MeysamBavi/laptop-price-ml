import scrapy
from scrapy import Selector


class LaptopsSpider(scrapy.Spider):
    name = "laptops"

    def start_requests(self):
        yield scrapy.Request(
            url="https://torob.com/p/c9e081d5-cc85-4cd5-98d3-116aa2b9aba2/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%84%D9"
                "%86%D9%88%D9%88-ideapad-3-4gb-ram-1tb-hdd-n4020-hd/",
        )

    def parse(self, response):
        yield {
            'title': response.css('.name h1::text').get(),
            'price': response.css('.price_text div::text').get()
        }
