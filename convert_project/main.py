# main.py
from src_modules.DBManager import DBManager
from src_modules.Image.ImageManager import ImageManager
from src_modules.URLId import ListURLId
import time
# from src_modules.Image import ImagePerformer
# from src_modules.LogManager import

class Program:
    def __init__(self):
        self.dbmanager = DBManager()
        self.listurlid = ListURLId()
        self.imagemanager = ImageManager()
    
    def launch(self):
        self.listurlid.updateList(self.dbmanager.getRecords())
        self.imagemanager.downloadImages(self.listurlid.getList())
        self.imagemanager.relocateImages(self.listurlid.getList())
        self.listurlid.show()
        self.dbmanager.updateData(self.listurlid.getList())
        print(self.dbmanager.current_number_record,  self.dbmanager.total_number_record)
        if self.dbmanager.current_number_record < self.dbmanager.total_number_record:
            self.launch()

def main():
    print(time.ctime())
    program = Program()
    program.launch()
    print(time.ctime())

if __name__ == "__main__":
    main()