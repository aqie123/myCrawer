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
           scrapy startproject ArticleSpiders
           cd ArticleSpiders
           scrapy genspider jobbole blog.jobbole.com
        c. 新建main.py
            安装  pip install pypiwin32
            在上面目录执行 scrapy crawl jobbole
            继续配置 main.py
            settings.py 设置robots  False
            在 jobbole.py 断点调试
        d.  对当前页面做调试 (目录中输入命令)
            scrapy shell http://blog.jobbole.com/all-posts/
                1. title = response.xpath('//*[ @ id = "post-112381"]/div[1]/h1/text()')
                   获取title 值 title.extract()
                2. 文章日期; date = response.xpath('//*[@id="post-112381"]/div[2]/p/text()')
                    date.extract()[0].strip().replace('·','').strip()
                3.点赞 digg = response.xpath('//*[@id="post-112381"]/div[3]/div[8]/span[1]/h10/text()')
                       digg.extract()[0]
        f.xpath 和css 选择器拿到数据,调试main.py
        g.在items新建两个类 JobBoleArticleItem,
        h.settings.py   修改 ITEM_PIPELINES
            同时可以过滤下载图片
        i. workon article  安装 pip install pillow 下载图片
        j,在pipelines  ArticleImagePipeline  自定义图片下载路径
        k.通过pipeline将数据保存到数据库中
        l.新建 JsonWithEncodingPipeline 将数据保存到

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
            谓语：
            7. /article/div[1]  第一个div
            8. /article/div[last()]  选取最后一个div元素
            9. /article/div[last()-1] 倒数第二个
            10. //div[@lang]  选取所有拥有lang属性的div元素
            11. //div[@lang='eng']  选取所有lang属性为eng的div元素
            其他
            12./div/*  选取div元素所有子节点
            13.//*     选取所有元素
            14.//div[@*]  选取所有带属性的title元素
            15./div/a | //div/p  选取所有div元素的a和p元素
            16.//span |//ul  选取文档中的span和ul元素
            17.article/div/p|//span  选取所有属于article元素的div元素的p元素
                                    以及文档中所有的span元素


"""