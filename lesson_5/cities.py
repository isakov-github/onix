import csv
import sqlite3
import urllib.request


def is_table_exist(cur):
    # get the count of tables with the name cities
    cur.execute(
        """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='cities'""")

    # if the count is 1, then table exists
    if cur.fetchone()[0] == 1:
        return True
    else:
        print("The table 'cities' not found in the database.")
        return False


def create_table(cur):
    # create table cities if one doesn't exist
    sql = """
        CREATE TABLE cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT,
        city TEXT,
        city_id INTEGER
        );
        """
    try:
        cur.executescript(sql)
    except sqlite3.DatabaseError as err:
        print("Note: ", err)
        return(-1)
    else:
        print("The table 'cities' has been created successfully")
    return(0)


def is_table_empty(cur):
    # check if table cities is empty
    cur.execute("""SELECT COUNT(*) FROM cities""")
    if (cur.fetchone()[0] == 0):
        print("The table 'cities' is empty.")
        return(True)
    else:
        print("The table 'cities' has some data.")
        return(False)


def load_cities_from_url(cur, con, url):
    # load data from url to table cities
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines, delimiter=';', quotechar='"')

    sql = """
        INSERT INTO cities (country, city, city_id)
        VALUES (?, ?, ?)
        """

    arr = []
    for row in cr:
        if(not row):
            break
        arr.append(tuple(row))

    try:
        cur.executemany(sql, arr)
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        print("Data was successfully load into table 'cities'")
        con.commit()


def add_city(cur, con):
    country = input("Input country: ")
    city = input("Input a name of city: ")
    city_id = input("City ID: ")

    sql = """
        INSERT INTO cities (country, city, city_id)
        VALUES (?, ?, ?)
        """

    cur_city = (country, city, city_id)
    try:
        cur.execute(sql, cur_city)
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        print("City was successfully insert into db")
        con.commit()


def delete_city(cur, con):
    city_id = input("Input city id to delete: ")

    sql = """
        DELETE FROM cities WHERE city_id = ?
        """

    if find_city(cur, city_id) == -1:
        return -1

    try:
        cur.execute(sql, (city_id,))
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        print("City was successfully delete")
        con.commit()


def find_city(cur, id=0):
    if not id:
        city_id = input("Input city id you're looking for: ")
    else:
        city_id = id

    sql = """
        SELECT id, country, city, city_id FROM cities WHERE city_id = ?
        """

    try:
        cur.execute(sql, (city_id,))
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        resp = cur.fetchone()
        if(resp):
            print(resp)
            return 0
        else:
            print("A city with this id not found")
            return -1


def print_table(cur):
    cur.execute("SELECT * FROM cities")
    while(True):
        row = cur.fetchone()
        if row:
            print(row)
        else:
            return 0


def menu(cur, con):
    choice = str()
    while(True):
        print("1. Add city")
        print("2. Delete city by id")
        print("3. Search by id")
        print("4. Show cities")
        print("0. Exit")
        choice = input("Make a choice: ")

        if choice == '0':
            return
        elif choice == '1':
            add_city(cur, con)
        elif choice == '2':
            delete_city(cur, con)
        elif choice == '3':
            find_city(cur)
        elif choice == '4':
            print_table(cur)
        else:
            print("Please, make a right choice")
