# -*- coding:utf-8 -*-

import MySQLdb as mdb 
import sys

try:
    conn = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
    cursor = conn.cursor()
    cursor.execute("SELECT Data FROM Images LIMIT 1")
    fout = open('image.png', 'wb')
    fout = write(cursor.fetchone()[0])
    fout.close()
    cursor.close()
    conn.close()
except IOError as e:
    print("Error %d: %s" % (e.args[0], e,args[1]), ...)
    sys.exit(1)