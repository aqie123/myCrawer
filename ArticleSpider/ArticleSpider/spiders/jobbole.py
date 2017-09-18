# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112381/']

    def parse(self, response):
        # 下标从第三个开始
        # /html/body/div[3]/div[3]/div[1]/div[1]/h1  js 生成的不算
        # // *[ @ id = "post-112381"] / div[1] / h1
        title = response.xpath('//*[ @ id = "post-112381"]/div[1]/h1/text()')
        create_date = response.xpath('//*[@id="post-112381"]/div[2]/p/text()')
        create_date = date.extract()[0].strip().replace('·','').strip()
        pass
