#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.cmdline import execute

import sys
import os

# D:\myCrawer\ArticleSpiders
# print(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 执行spider命令
execute(["scrapy", "crawl", "jobbole"])
