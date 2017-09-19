# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112503/']

    def parse(self, response):
        # ----------------xpath 提取页面元素---------------------------

        # 文章标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()

        pass



