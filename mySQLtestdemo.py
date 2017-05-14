 #-*- coding:utf-8 -*-
 # 这个脚本将获取并打印MySQL数据库的版本

import _mysql
import sys

con = None

try:
    con = _mysql.connect('localhost', 'testuser',
        'test623', 'testdb')
    con.query("SELECT VERSION()")
    result = con.use_result()
    print("MySQL version is:%s" % result.fetch_row()[0])
except _mysql.Error as e:
    print("Error %d:%s" % (e.args[0], e.args[1]))
    sys.exit(1)
finally:
    if con:
        con.close()
