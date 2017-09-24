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
        k.新建 JsonWithEncodingPipeline 将数据保存到 article.json
        l.JsonExporterPipleline 调用scrapy自带保存进articleexport.json
        m.通过pipeline将数据保存到数据库中 (同步 MysqlPipeline)
            1. 新建jobbole.sql
            2. 存数据库时转换为date类型,(保存进json会出问题)
            3. 安装mysql驱动 pip install mysqlclient
               (linux下面：
               乌班图： sudo apt-get install libmysqlclient-dev
               centos: sudo yum install python-devel mysql-devel)
            4.自定义MysqlPipeline 存入数据库
        n.通过异步方式写入数据库 (MysqlTwistedPipeline)
            1. settings.py 配置 mysql相关参数
        o.item-loader
            1.


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

二：爬取知乎问答：
    1. session(根据用户名密码生成session_id)
    2. cookie(本地存储机制)
        a.键值对
        b.浏览器 (请求)-> 服务器(生成session_id,返回浏览器将id存进cookie,下一次请求带着cookie)
    3.通过request完成知乎模拟登陆
        a.Request URL:
            https://www.zhihu.com/login/email
            https://www.zhihu.com/login/phone_num
        b.Form Data
            1._xsrf
            2.password
            3.email
            4.captcha_type
        c.utils/zhihu_login_requests.py
            1. pip install requests
        d.请求头信息
            1.User-Agent
            2.header
    4. 进入ArticleSpider,进入article, 新建工程目录 scrapy genspider zhihu www.zhihu.com
        1.知乎页面分两版：https://www.zhihu.com/question/65528115/answer/234283280
            Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
        2.查看旧版样式 ：scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0" https://www.zhihu.com/question/65528115/answer/234283280
        3.with open("e:/zhihu.html","wb") as f:
            f.write(response.text.encode("utf-8"))

"""
"""
https://www.zhihu.com/api/v4/questions/29372574/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=23

"""
print("\u767b\u5f55\u8fc7\u4e8e\u9891\u7e41\uff0c\u8bf7\u7a0d\u540e\u91cd\u8bd5")
print("\u9a8c\u8bc1\u7801\u4f1a\u8bdd\u65e0\u6548")
