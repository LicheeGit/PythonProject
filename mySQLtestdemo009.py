# -*- coding: utf-8 -*-

import MySQLdb as mdb 
import sys
try:
    conn = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
    cursor = conn.cursor()
    cursor.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
        ("Leo Tolstoy", "1"))
    cursor.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
        ("Boris Pasternak", "2"))
    cursor.execute("UPDATE Writer SET Name = %s WHERE Id = %s",
        ("Leonid Leonov", "3"))
    conn.commit()
    cursor.close()
    conn.close()
except mdb.Error as e:
    conn.rollback()
    print("Error %d: %s" % (e.args[0],e.args[1]), ...)
    sys.exit(1)
