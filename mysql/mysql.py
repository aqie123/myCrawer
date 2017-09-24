
"""
mysql 表示时间：datetime timestamp date int

timestamp会跟随设置的时区变化而变化，而datetime保存的是绝对值不会变化。
占用存储空间不同。timestamp储存占用4个字节，
datetime储存占用8个字节：http://dev.mysql.com/doc/refm...
可表示的时间范围不同。timestamp可表示范围:1970-01-01 00:00:00~2038-01-09 03:14:07，
datetime支持的范围更宽1000-01-01 00:00:00 ~ 9999-12-31 23:59:59
索引速度不同。timestamp更轻量，索引相对datetime更快。

"""