import re

import scrapy


class GetLinksSpider(scrapy.Spider):
    name = 'get_links'
    allowed_domains = ['index.minfin.com.ua']
    start_urls = ['https://index.minfin.com.ua/ua/russian-invading/casualties']

    def parse(self, response):
        prefix = "/month.php?month="
        for link in response.xpath('//div[@class="ajaxmonth"]/h4/a'):
            yield {
                "link": prefix + re.search(r"\d{4}-\d{2}", link.xpath(".//@href").get()).group()
            }
