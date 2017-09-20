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

class ArticlespidersPipeline(object):
    def process_item(self, item, spider):
        # 将图片保存到数据库
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # pass
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

