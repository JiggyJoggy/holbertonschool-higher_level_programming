#!/usr/bin/python3
"""takes in the name of a state as an argument
and lists all cities of that state, using
the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    state_name = sys.argv[4]

    cursor.execute("""SELECT cities.name, states.name
                   FROM cities JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id;""")
    cities = cursor.fetchall()

    print_cities = [item[0] for item in cities if item[1] == sys.argv[4]]
    print(', '.join(print_cities))
