# -*- coding: utf-8 -*-
# 学习内容参考：http://kodango.com/mysql-python-tutorial-part-two,非常感谢

import MySQLdb as mdb 
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    for row in rows:
        print("%s %s" % (row["Id"], row["Name"]), ...)