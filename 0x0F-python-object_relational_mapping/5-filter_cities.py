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
    cursor.execute("SELECT cities.name \
                    FROM cities \
                    INNER JOIN states \
                    ON cities.state_id=states.id \
                    WHERE states.name=%s \
                    ORDER BY cities.id ASC", (state_db,))

    data = cursor.fetchall()

    for filter in range(len(data)):
        print(''.join(data[filter]), end="")
        if filter < len(data) - 1:
            print(", ", end="")
    print()

    cursor.close()
    db.close()
