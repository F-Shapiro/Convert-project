# DBManager.py
from configparser import ConfigParser
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
    __total_number_of_record = int(config["DBManager"]["total_number_of_record"])
    __current_number_of_record = 0

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

    def getRecords(self):
        self.__cursor.execute(
            f'''
            SELECT id, title_img FROM {self.__connect_param["database"]}
            WHERE title_img IS NOT NULL AND title_img LIKE 'http%'
            LIMIT {self.__step_limit} OFFSET {self.__current_number_of_record}
            '''
        )
        self.__current_number_of_record += self.__step_limit
        rows = self.__cursor.fetchall()
        return rows
    
    def updateData(self, listObject):
        query = f'''UPDATE {self.__connect_param["database"]} SET title_img = CASE id strCase ELSE title_img END'''
        strCase = " ".join(
            map(lambda item:
            " ".join(list(map(lambda id_product:
                                f"WHEN {id_product} THEN '{item.path}'"
                        , item.getIdList())))
            , listObject))
        query = query.replace("strCase", strCase)
        print(query)
        self.__cursor.execute(query)
        self.__db_connect.commit()
    
    def dat(self):
        self.__cursor.execute(
            "UPDATE products SET title_img = 'https://i.ibb.co/QJy1syD/erck.png' WHERE title_img = '/var/www/shared_folder/convert_project/updated_imgs/251022'"
        )
        self.__db_connect.commit()

    def __getConnectParam(self):
        self.__connect_param["user"] = config["connect_param"]["user"]
        self.__connect_param["password"] = config["connect_param"]["password"]
        self.__connect_param["host"] = config["connect_param"]["host"]
        self.__connect_param["port"] = int(config["connect_param"]["port"])
        self.__connect_param["database"] = config["connect_param"]["database"]

    def __del__(self):
        self.__cursor.close()
        self.__db_connect.close()