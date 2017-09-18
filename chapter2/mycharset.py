#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python2
# 调用 encode 编码前,编码必须转换为unicode
s = 'abc'   # string
su = u'abc'  # unicode
s.encode('utf8')  # 'abc'
su.encode('utf8')   # 'abc'

sz = "啊切"
sz.decode('gb2312').encode('utf8')

szu = u'啊切'
szu.encode('utf8')

# python3
s3 = '啊切'  # 统一为 unicode
s3.encode('utf8')
