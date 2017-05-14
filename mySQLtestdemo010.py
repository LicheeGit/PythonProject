# -*- coding: utf-8 -*-

import MySQLdb as mdb 
import sys
try:
    conn = mdb.connect('localhost', 'testuser', 
        'test623', 'testdb');
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Writers WHERE Id = 5")
    cursor.execute("DELETE FROM Writers WHERE Id = 4")
    cursor.execute("DELETE FROM Writer WHERE Id = 3")

    conn.commit()
except mdb.Error as e:
    conn.rollback()
    print("Error %d: %s" % (e.args[0],e.args[1]), ...)
    sys.exit(1)

    cursor.close()
    conn.close()