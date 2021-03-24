# DBManager.py
from configparser import ConfigParser
from functools import reduce
from operator import add
import mariadb
import sys

config = ConfigParser()
config.read("config.ini")

class DBManager:
    __connect_param = {
        "user": "",
        "password": "",
        "host": "",
        "port": 0,
        "database": ""
    }
    __step_limit = int(config["DBManager"]["step_limit"])
    __total_number_record = int(config["DBManager"]["total_number_record"])
    __current_number_record = 0

    def __init__(self):
        self.__getConnectParam()
        try:
            self.__db_connect = mariadb.connect(
                user = self.__connect_param["user"],
                password = self.__connect_param["password"],
                host = self.__connect_param["host"],
                port = self.__connect_param["port"],
                database = self.__connect_param["database"]
            )
            print("Connect successful")
        except mariadb.Error as err:
            print(f"Error connecting to MariaDB Platform: {err}")
            sys.exit(1)
        
        self.__cursor = self.__db_connect.cursor()
    
    @property
    def step_limit(self):
        return self.__step_limit
    
    @property
    def total_number_record(self):
        return self.__total_number_record
    
    @property
    def current_number_record(self):
        return self.__current_number_record

    def getRecords(self):
        self.__cursor.execute(
            f'''
            SELECT id, title_img FROM products
            WHERE title_img IS NOT NULL AND title_img LIKE 'http%'
            LIMIT {self.__step_limit} OFFSET {self.__current_number_record}
            '''
        )
        self.__current_number_record += self.__step_limit
        rows = self.__cursor.fetchall()
        return rows
    
    def updateData(self, listObject, logManager):
        query = f'''UPDATE products SET title_img = CASE id strCase ELSE title_img END'''
        strCase = " ".join(
            map(lambda item:
            " ".join(list(map(lambda id_product:
                                f"WHEN {id_product} THEN '{item.path}'"
                        , item.getNewIdList(reset=False))))
            , listObject)).replace("  ", " ")
        query = query.replace("strCase", strCase)
        try:
            self.__cursor.execute(query)
            self.__db_connect.commit()
            logManager.updateStep(reduce(add, map(lambda item: len(item.getNewIdList()), listObject)), 3)
        except mariadb.Error as err:
            print(f"Error updating to MariaDB Platform: {err}")
            idError = " ".join(
                map(lambda item:
                " ".join(list(map(lambda id_product:
                                    f"{id_product}"
                            , item.getNewIdList())))
                , listObject))
            logManager.writeFault(idError)

    def __getConnectParam(self):
        self.__connect_param["user"] = config["connect_param"]["user"]
        self.__connect_param["password"] = config["connect_param"]["password"]
        self.__connect_param["host"] = config["connect_param"]["host"]
        self.__connect_param["port"] = int(config["connect_param"]["port"])
        self.__connect_param["database"] = config["connect_param"]["database"]

    def __del__(self):
        self.__cursor.close()
        self.__db_connect.close()