#!/usr/bin/python3
"""
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
                host='localhost',
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
                )
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name=\'{}\'"
                    "ORDER BY states.id".format(sys.argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error: [%d] - [%s]" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: [%s]" % str(e))
    finally:
        if 'cur' in locals() and cur is not None:
            cur.close()
        if 'db' in locals() and db is not None:
            db.close()
