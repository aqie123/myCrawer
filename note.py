"""
blog : http://projectsedu.com/
数据分析服务
互联网金融
数据建模
信息聚类
自然语言处理
医疗病例分析
数据分析服务

一：配置环境 基础知识
    1.正则表达式
    2.深度优先和广度优先遍历算法
    3.url去重常见策略

二：爬取真实数据
    1.知名技术社区
        http://www.jobbole.com/
    2.知名问答网站
    3.知名招聘网站

    xpath + css
    模拟登陆
    Scrapy:
        spider, item, item loader, pipeline, feed export, CrawlSpider


三：scrapy 突破反爬虫技术
    1.网络打码，实现图片验证码
    2.ip 访问频率限制
    3. user-agent 随机切换

四：scrapy 进阶
    1.scrapy 原理

    2.scrapy 中间件开发

    a.动态网站的抓取处理
    b.selenium 和 phantomjs 集成到scrapy
    c.scrapy log 配置
    d. email 发送
    f.scrapy 信号

五：scrapy redis 分布式爬虫
    1. 理解scrapy-redis 分布式爬虫
    2. 集成 bloomfilter 到 scrapy-redis 中

六：elasticsearch django 实现搜索引擎


总结：
    1.开发爬虫所需要用到技术以及网站分析技巧
    2.理解scrapy 原理和所有组件使用
    3.理解分布式爬虫scrapy-redis使用及原理
    4.django快速搭建网站
"""

'''
一：技术选型
    1.scrapy(基于twisted框架,异步IO)  vs  requests + beautifulsoup(库)
        a.内置 css xpath selector

    2.常见服务类型
        a.webservice(restapi)
        b.静态网页
        c.动态网页
二：爬虫用途
    1.搜索引擎,垂直领域搜索引擎
    2.推荐引擎(进入头条)
    3. 机器学习的数据样本
    4.数据分析,舆情分析

'''
