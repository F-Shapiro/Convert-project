import configparser
import mariadb
import sys
 
try:
    db_connect = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="products"
    )
except mariadb.Error as err:
    print(f"Error connecting to MariaDB Platform: {err}")
    sys.exit(1)

cur = db_connect.cursor()