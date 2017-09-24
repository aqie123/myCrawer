# -*- coding: utf-8 -*-
import scrapy
import re
import json
import datetime


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

    headers = {
        "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com",
        "User-Agent": agent

    }

    def parse(self, response):
        pass

    def start_requests(self):
        # scrapy 中入口提供的异步ui,设置callback,否则默认调用哪个parse函数
        # 从登录页面获取数据
        return [scrapy.Request('https://www.zhihu.com/#signin', headers=self.headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text, re.DOTALL)
        # match_obj = re.findall(r'name="_xsrf" value="(.*?)"', response.text)
        zh_xsrf = ""
        if match_obj:
            zh_xsrf = match_obj.group(1)
            print(zh_xsrf)
        else:
            return ""
        if zh_xsrf:
            post_url = "https://www.zhihu.com/login/phone_num"
            post_data = {
                "_xsrf": zh_xsrf,
                "phone_num": '15533833058',
                "password": '123456kzl'
            }
            # 重写请求入口,返回表单提交
            return [scrapy.FormRequest(
                url=post_url,
                formdata=post_data,
                headers=self.headers,
                callback=self.check_login
            )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        text_json = json.loads(response.text)
        if "msg" in text_json and text_json["msg"] == "登录成功":
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)