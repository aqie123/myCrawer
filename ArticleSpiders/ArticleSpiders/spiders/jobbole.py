# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        :param response:
        :return:
        1. 获取文章列表页中的文章url,并交给scrapy下载后进行解析
        2. 获取下一页的url并交给scrapy下载，并交给解析函数parse进行具体字段解析
        """
        # 解析列表页中的所有文章url,交给scrapy下载后进行解析
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()

        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.css_parse_detail)
            # print(post_url)

        # 提取下一页url并交给scrapy下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def xpath_parse_detail(self, response):
        # 提取文章具体字段
        # ----------------xpath 提取页面元素---------------------------
        # extract_first() 替换为 extract_first()
        # 文章标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()

        # 创建时间
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')
        create_date = create_date.extract_first().strip().replace('·', '').strip()

        # 点赞数
        digg = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()')
        digg = int(digg.extract_first())

        # 收藏数
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract_first()
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0

        # 评论数
        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract_first()
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        else:
            comment_nums = 0

        # 获取文章内容
        main_contents = response.xpath("//div[@class='entry']").extract_first()

        # 获取分类标签
        category_tag = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # 对评论过滤
        category_tag = [element for element in category_tag if not element.strip().endswith("评论")]
        main_tag = category_tag[0]
        tags = category_tag[1::]
        tags = ",".join(tags)


    def css_parse_detail(self, response):
        # --------------css 选择器提取页面元素----------------------
        # 伪类选择器
        # 文章标题
        css_title = response.css('.entry-header h1::text').extract_first()

        # 创建时间
        css_create_time = response.css('p.entry-meta-hide-on-mobile::text')
        css_create_time = css_create_time.extract_first().strip().replace('·', '').strip()

        # 点赞数
        css_like = response.css('span.vote-post-up h10::text').extract_first()

        # 收藏数
        css_fav_nums = response.css('.bookmark-btn::text').extract_first()
        match_re = re.match(".*?(\d+).*", css_fav_nums)
        if match_re:
            css_fav_nums = match_re.group(1)
        else:
            css_fav_nums = 0

        # 评论数
        css_comment_nums = response.css("a[href='#article-comment'] span::text").extract_first()
        match_re = re.match(".*?(\d+).*", css_comment_nums)
        if match_re:
            css_comment_nums = match_re.group(1)

        # 正文
        css_content = response.css("div.entry").extract_first()

        # 文章分类
        css_category_tag = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # 对评论过滤
        css_category_tag = [element for element in css_category_tag if not element.strip().endswith("评论")]
        # 主分类
        css_main_tag = css_category_tag[0]
        # 标签
        css_tags = css_category_tag[1::]
        css_tags = ",".join(css_tags)




