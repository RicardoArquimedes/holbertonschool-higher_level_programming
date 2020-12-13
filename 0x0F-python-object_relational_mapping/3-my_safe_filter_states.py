#!/usr/bin/python3
"""Module doc"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    user_db = argv[1]
    pass_db = argv[2]
    name_db = argv[3]
    state_db = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user_db,
                         passwd=pass_db,
                         db=name_db,
                         charset="utf8")

    cursor = db.cursor()
    cursor.execute("SELECT * \
             FROM states \
             WHERE name=%s \
             ORDER BY id ASC", (state_db,))

    data = cursor.fetchall()

    for states in data:
        print(states)

    cursor.close()
    db.close()
