import scrapy


class LaptopsSpider(scrapy.Spider):
    name = "laptops"

    def start_requests(self):
        links_file = open('./links.txt')
        urls = links_file.readlines()
        for url in urls:
            yield scrapy.Request(
                url=url,
            )

    def parse(self, response):

        result = {
            'title': response.css('.name h1::text').get(),
        }

        price = response.css('.price_text div::text').get()
        if not price or 'دیگر' in price:
            price = response.css('.jsx-63b317fab2efbae.buy_box_text:nth-child(2)::text').get()
        result['price'] = price

        for detail in response.css('div.jsx-5b5c456cc255c2dc.header ~ div.jsx-5b5c456cc255c2dc'):
            feature = detail.css('.detail-title::text').get()
            value = detail.css('.detail-value::text').get()
            result[feature] = value

        yield result
