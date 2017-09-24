#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

try:
    import cookielib
except:
    import http.cookiejar as cookielib

# request session 指代某一次请求,是一个长连接,实例化变量
# 将get_xsrf()中的request变为session.不用每次都请求
session = requests.session()
# cookie信息存入文件

session.cookies = cookielib.LWPCookieJar(filename="zhihu_cookies.txt")

try:
    session.cookies.load(ignore_discard=True)
except:
    print("zhihu_cookies加载失败")

agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
header = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent": agent

}


def is_login():
    # 通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/question/56250357/answer/148534773"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_xsrf():
    # 请求知乎登录页面 获取xsrf code
    response = session.get("https://www.zhihu.com", headers=header)
    # print(response.text)

    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    zh_xsrf = re.findall(r'name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        return match_obj.group(1)
    else:
        # print(zh_xsrf[0])
        return zh_xsrf[0]


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        # 写文件将unicode转为utf8编码
        f.write(response.text.encode("utf-8"))
    print("ok")


def get_captcha():
    import time
    t = str(int(time.time()*1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url, headers=header)
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)
        f.close()

    from PIL import Image
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass

    captcha = input("输入验证码\n>")
    return captcha


def zhihu_login(account, password):
    # 知乎登录
    if re.match("^1\d{10}", account):
        print("手机登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "phone_num": account,
            "password": password
        }

    else:
        if "@" in account:
            print("邮箱登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "email": account,
                "password": password
            }

    response_text = session.post(post_url, data=post_data, headers=header)

    # 将服务器返回保存到本地
    session.cookies.save()


# get_xsrf()
# zhihu_login('2924811900@qq.com', '123456kzl')
# zhihu_login('15533833058', '123456kzl')
# get_index()
# is_login()
get_captcha()
