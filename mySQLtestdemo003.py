# -*- coding: utf-8 -*-
# 今天的学习内容参考：http://kodango.com/mysql-python-tutorial-part-one，非常感谢

import MySQLdb as mdb 
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    numrows = int(cur.rowcount)
    for i in range(numrows):
        row = cur.fetchone()
        print(row[0], row[1])