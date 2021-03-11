# DBManager.py
import configparser
import mariadb
import sys

config = configparser.ConfigParser()
config.read("config.ini")

class DBManager:
    __connectParam = {
        "user":"root",
        "password":"",
        "host":"localhost",
        "port":3306,
        "database":"products"
    }
    __step_limit = int(config["DBManager"]["step_limit"])
    __total_number_of_record = int(config["DBManager"]["total_number_of_record"])
    __current_number_of_record = 0

    def __init__(self):
        try:
            self.__db_connect = mariadb.connect(
                user = self.__connectParam["user"],
                password = self.__connectParam["password"],
                host = self.__connectParam["password"],
                port = self.__connectParam["port"],
                database = self.__connectParam["database"]
            )
            print("Connect successful")
        except mariadb.Error as err:
            print(f"Error connecting to MariaDB Platform: {err}")
            sys.exit(1)
        
        self.__cursor = self.__db_connect.cursor()

    def getRecord(self):
        self.__cursor.execute(
            f'''SELECT id, title_img FROM products
            WHERE title_img IS NOT NULL AND title_img LIKE 'http:%'
            LIMIT {self.__step_limit}'''
        )
        self.__current_number_of_record += self.__step_limit
        rows = self.__cursor.fetchall()
        print('Total Row(s):', self.__cursor.rowcount)
        for row in rows:
            print(row)

    def __del__(self):
        self.__cursor.close()
