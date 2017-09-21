# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

from scrapy.pipelines.images import ImagesPipeline
# scrapy 自带转json
from scrapy.exporters import JsonItemExporter

# 连接数据库
import MySQLdb
import MySQLdb.cursors

# mysql操作变成异步操作
from twisted.enterprise import adbapi


class ArticlespidersPipeline(object):
    def process_item(self, item, spider):
        # 将图片保存到数据库
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # pass
        # 将图片保存进自定义路径
        if "front_image_url" in item:
            image_file_path = ''
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path

        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        # 避免编码方式问题
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        # 转化成字典
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipeline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        # 二进制打开
        self.file = open('articleexport.json', 'wb')
        # 传递exporter进来
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        # 停止导出,关闭文件
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'root', 'article_spider', charset="utf8", use_unicode=True)
        # 通过cursor执行数据库操作
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole(url_object_id, title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["url_object_id"], item["title"], item["url"], item["create_date"],
                                         item["fav_nums"]))
        self.conn.commit()


class MysqlTwistedPipeline(object):
    # 采用异步方式写入数据库(爬取速度超过数据库写入速度2)
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        # 将参数变为dict
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # 使用 MySQLdb模块
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行(自定义函数,插入数据)
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)


