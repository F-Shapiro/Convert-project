# main.py
from src_modules.DBManager import DBManager
from src_modules.Image.ImageManager import ImageManager
from src_modules.URLofId import StackURLofId
import time
# from src_modules.Image import ImagePerformer
# from src_modules.LogManager import

def main():
    print(time.ctime())
    dbmanager = DBManager()
    stackurlofid = StackURLofId()
    imagemanager = ImageManager()
    stackurlofid.updateList(dbmanager.getRecords())
    # stackurlofid.show()
    # imagemanager.downloadImage(stackurlofid.getGenerator())
    del dbmanager
    del stackurlofid
    del imagemanager
    print(time.ctime())

if __name__ == "__main__":
    main()