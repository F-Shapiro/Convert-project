# main.py
import configparser
from src_modules.DBManager import DBManager

def main():
    dbmanager = DBManager()
    dbmanager.getRecord()
    del dbmanager

if __name__ == "__main__":
    main()