# main.py
from src_modules.DBManager import DBManager
from src_modules.Image.ImageManager import ImageManager
from src_modules.URLId import ListURLId
import time
# from src_modules.Image import ImagePerformer
# from src_modules.LogManager import

def main():
    print(time.ctime())
    dbmanager = DBManager()
    listurlid = ListURLId()
    imagemanager = ImageManager()
    listurlid.updateList(dbmanager.getRecords())
    listurlid.show()
    imagemanager.downloadImage(listurlid.getList())
    print(time.ctime())

if __name__ == "__main__":
    main()