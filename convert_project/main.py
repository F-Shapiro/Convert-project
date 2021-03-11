# main.py
import time
import configparser
from src_modules.DBManager import DBManager
from src_modules.Image import ImageManager
# from src_modules.Image import ImagePerformer
# from src_modules.LogManager import

def main():
    print(time.ctime())
    dbmanager = DBManager()
    dbmanager.getRecords()
    del dbmanager
    print(time.ctime())

if __name__ == "__main__":
    main()