# DBManager.py
import mariadb
import sys

class DBManager:
    def getRecord(self):
        try:
            db_connect = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="products"
            )
            print("connect successful")
        except mariadb.Error as err:
            print(f"Error connecting to MariaDB Platform: {err}")
            sys.exit(1)

        cursor = db_connect.cursor()
        cursor.execute(
            "SELECT id, title_img FROM products LIMIT 7"
        )

        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
        # for (first_name, last_name) in cursor:
        #     print(f"First Name: {first_name}, Last Name: {last_name}")

        cursor.close()
