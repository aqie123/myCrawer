#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 一： 爬取知名技术文章网站(http://www.jobbole.com/)

    1.http://blog.jobbole.com/   爬取文章
        a. 找到所有文章,爬取下一页
        b. 可以知道总页数,拼接出链接
    2.新建虚拟环境 article
        a. 安装scrapy   pip install -i https://pypi.douban.com/simple scrapy
        b. 到myCrawer 新建项目名称
           workon article
           scrapy startproject ArticleSpider
           cd ArticleSpider
           scrapy genspider jobbole blog.jobbole.com
        c. 新建main.py
            安装  pip install pypiwin32
            在上面目录执行 scrapy crawl jobbole
            继续配置 main.py
            settings.py 设置robots  False
            在 jobbole.py 断点调试
    3.xpath
        a.使用路径表达式在xml和html中进行导航
        b.包含标准函数库
        c.w3c的标准
        d.节点关系
            1.父节点
            2.子节点
            3.同胞节点
            4.先辈节点
            5.后代节点
        e.语法
            1.article  选取所有子节点
            2./article  选取根元素article
            3.article/a  选取属于article的子元素
            4.//div 选取所有div子元素
            5.article//div 选取属于article元素的后代div
            6.选取所有名为class的属性

"""