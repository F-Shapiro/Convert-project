# main.py
import time
import configparser
from src_modules.DBManager import DBManager

def main():
    print(time.ctime())
    dbmanager = DBManager()
    dbmanager.getRecord()
    del dbmanager
    print(time.ctime())

if __name__ == "__main__":
    main()