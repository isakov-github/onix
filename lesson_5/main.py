import sqlite3
import cities

# create a connection and a cursor
con = sqlite3.connect('testdb.db')
cur = con.cursor()

# check if the table 'cities' already exist. if not create it.
if(cities.is_table_exist(cur)):
    cities.create_table(cur)

# if the table is empty - fill it from url.
if(cities.is_table_empty(cur)):
    url = 'https://worldweather.wmo.int/en/json/full_city_list.txt'
    cities.load_cities_from_url(cur, con, url)

cities.menu(cur, con)

cur.close()
con.close()
