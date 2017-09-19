# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112381/']

    def parse(self, response):
        # ----------------xpath 提取页面元素---------------------------

        # 文章标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()

        # 创建时间
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')
        create_date = create_date.extract()[0].strip().replace('·', '').strip()

        # 点赞数
        digg = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()')
        digg = int(digg.extract()[0])

        # 收藏数
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0

        # 评论数
        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        else:
            comment_nums = 0

        # 获取文章内容
        main_contents = response.xpath("//div[@class='entry']").extract()[0]

        # 获取分类标签
        category_tag = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # 对评论过滤
        category_tag = [element for element in category_tag if not element.strip().endswith("评论")]
        main_tag = category_tag[0]
        tags = category_tag[1::]
        tags = ",".join(tags)

        # --------------css 选择器提取页面元素----------------------
        # 伪类选择器
        # 文章标题
        css_title = response.css('.entry-header h1::text').extract()[0]

        # 创建时间
        css_create_time = response.css('p.entry-meta-hide-on-mobile::text')
        css_create_time = css_create_time.extract()[0].strip().replace('·', '').strip()

        # 点赞数
        css_like = response.css('span.vote-post-up h10::text').extract()[0]

        # 收藏数
        css_fav_nums = response.css('.bookmark-btn::text').extract()[0]
        match_re = re.match(".*?(\d+).*", css_fav_nums)
        if match_re:
            css_fav_nums = match_re.group(1)
        else:
            css_fav_nums = 0

        # 评论数
        css_comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*?(\d+).*", css_comment_nums)
        if match_re:
            css_comment_nums = match_re.group(1)

        # 正文
        css_content = response.css("div.entry").extract()[0]

        # 文章分类
        css_category_tag = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # 对评论过滤
        css_category_tag = [element for element in css_category_tag if not element.strip().endswith("评论")]
        # 主分类
        css_main_tag = css_category_tag[0]
        # 标签
        css_tags = css_category_tag[1::]
        css_tags = ",".join(css_tags)
        pass



