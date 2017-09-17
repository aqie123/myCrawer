"""
1.vitualenv 和 virtualenvwrapper 安装配置
    a. pip install virtualenv
    b. pip install django
    c.查看python 路径 python -c "import sys; print sys.executable"
    d. pip install virtualenvwrapper
    e.pip install virtualenvwrapper-win
        1. workon
        2. mkvirtualenv py3  创建虚拟环境统一放在 WORKON_HOME 目录下面 (推荐)
            退出 ： deactivate
            进入 ： workon py3
        3.mkvirtualenv --python=D:\python27\python.exe py27Scrapy
    f.
        1.virtualenv scrapytest 新建虚拟环境
        2.进入虚拟环境/scripts activate.bat
        3.退出虚拟环境 deactivate.bat
        4. virtualenv -p D:\python27\python.exe py27
    g.  豆瓣源
        pip install -i https://pypi.douban.com/simple scrapy
            1.地址 www.lfd.uci.edu/~gohlke/pythonlibs
            2. 进入当前目录,在进入到虚拟环境
            3. http://aka.ms/vcpython27
        pip install requests

2.interpreter

3.
"""

"""
正则表达式
1.特殊字符
    a. ^ $ * ? {2} {2,} (2,5} |
    b. [] [^] [a-z]
    c. \s \S \w \W
    d. [\u4E00-\u9FA5]  ()  \d

"""