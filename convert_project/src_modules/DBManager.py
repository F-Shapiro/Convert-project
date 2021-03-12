# DBManager.py
from configparser import ConfigParser
import mariadb
import sys

config = ConfigParser()
config.read("config.ini")

class DBManager:
    __connectParam = {
        "user": "",
        "password": "",
        "host": "",
        "port": 0,
        "database": ""
    }
    __step_limit = int(config["DBManager"]["step_limit"])
    __total_number_of_record = int(config["DBManager"]["total_number_of_record"])
    __current_number_of_record = 0

    def __init__(self):
        self.__getConnectParam()
        try:
            self.__db_connect = mariadb.connect(
                user = self.__connectParam["user"],
                password = self.__connectParam["password"],
                host = self.__connectParam["host"],
                port = self.__connectParam["port"],
                database = self.__connectParam["database"]
            )
            print("Connect successful")
        except mariadb.Error as err:
            print(f"Error connecting to MariaDB Platform: {err}")
            sys.exit(1)
        
        self.__cursor = self.__db_connect.cursor()

    def getRecords(self):
        self.__cursor.execute(
            f'''SELECT id, title_img FROM products
            WHERE title_img IS NOT NULL AND title_img LIKE 'http%'
            LIMIT {self.__step_limit}'''
        )
        self.__current_number_of_record += self.__step_limit
        rows = self.__cursor.fetchall()

        print('Total Row(s):', self.__cursor.rowcount)
        for row in rows:
            print(row)
        
        return rows
    
    def __sortRecord(self):
        pass

    def __getConnectParam(self):
        self.__connectParam["user"] = config["connectParam"]["user"]
        self.__connectParam["password"] = config["connectParam"]["password"]
        self.__connectParam["host"] = config["connectParam"]["host"]
        self.__connectParam["port"] = int(config["connectParam"]["port"])
        self.__connectParam["database"] = config["connectParam"]["database"]

    def __del__(self):
        self.__cursor.close()
        self.__db_connect.close()
