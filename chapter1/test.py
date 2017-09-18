#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from mylibs.myregex import sayhello
from mylibs.myregex import myreg

line = 'aooooooooooooooabaabbbbbbabaqie123'
regex_str = '.*?(a.*?a).*'
# 返回匹配结果
match_obj = re.match(regex_str, line)
if match_obj:
    # 提取第一个括号
    # 左边问号防止(贪婪模式: 匹配到最右边 只提取bb,反向匹配)
    # 右边加问号防止(贪婪模式拿到右边aa)
    print(match_obj.group(1))
else:
    print("no")

# 只会提取aba(任意多个字符)
# regex_str = '.*(a.*a).*'

# 只会提取aba(至少一个字符)
# regex_str = '.*(a.+a).*'

# 提取abaa (至少两个字符)
# regex_str = '.*(a.{2}a).*'

# 提取abaa(两到五个字符)
regex_str = '.*(a.{2,5}a).*'

myreg(regex_str, line)

# -------- () |----------

line = 'boobby123'
# boobby()先匹配左边的
# regex_str = '(bobby|boobby)123'

# 提取整个字符串 boobby123 group(2)会提取booby
regex_str = '((bobby|boobby)123)'
myreg(regex_str, line)

# ---------[]---------
line = '15533833058'
# [代表匹配里面任意一个字符,多用于提取号码]
# [.* 不代表任何其他含义]
regex_str = '(1[3578][0-9]{9})'
myreg(regex_str, line)

# -----\s \S -------
line = "啊 切"
regex_str = "(啊\s切)"
myreg(regex_str, line)

line = "啊udas切"
# \S 只要有一个字符就行, +至少出现一次
regex_str = "(啊\S+切)"
myreg(regex_str, line)

line = "啊udas切"
# \S 只要有一个字符就行, +至少出现一次
regex_str = "(啊\S+切)"
myreg(regex_str, line)

# [A-Za-z0-9_] 和 \w 等同
line = "啊aqie切"
regex_str = "(啊\w+切)"
myreg(regex_str, line)

# \W 不以这些字符开头
line = "啊： 切"
regex_str = "(啊\W+切)"
myreg(regex_str, line)

# 提取连续汉字
line = "study in 南京大学"
# 贪婪匹配
regex_str = ".*?([\u4E00-\u9FA5]+大学)"
myreg(regex_str, line)

line = 'xxx 出生于2008,死于2017'
regex_str = '.*?(\d+).*'
myreg(regex_str, line)

# 正则表达式处理多个格式日期

line = " xxx 出生于2017年9月18日"
# line = " xxx 出生于2017年9月"
# line = " xxx 出生于2017/9/18"
# line = " xxx 出生于2017-9-18"
# line = " xxx 出生于2017-09-18"
# line = " xxx 出生于2017-09"


regex_str = '.*出生于?(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}日|[月]$|[月/-]\d{1,2}|$))'
myreg(regex_str, line)
