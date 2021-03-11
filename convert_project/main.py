# main.py
import time
from src_modules.DBManager import DBManager
from src_modules.Image.ImageManager import ImageManager
# from src_modules.Image import ImagePerformer
# from src_modules.LogManager import

def main():
    print(time.ctime())
    dbmanager = DBManager()
    imagemanager = ImageManager()
    imagemanager.downloadImage(dbmanager.getRecords())
    del dbmanager
    print(time.ctime())

if __name__ == "__main__":
    main()