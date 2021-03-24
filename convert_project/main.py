# main.py
from src_modules.DBManager import DBManager
from src_modules.Image.ImageManager import ImageManager
from src_modules.URLId import ListURLId
# from src_modules.Image import ImagePerformer
from src_modules.LogManager import LogManager
import datetime
import time

class Program:
    def __init__(self):
        self.dbManager = DBManager()
        self.listUrlId = ListURLId()
        self.imageManager = ImageManager()
        self.logManager = LogManager(self.dbManager.total_number_record / self.dbManager.step_limit)
    
    def launch(self):
        self.listUrlId.updateList(self.dbManager.getRecords())
        self.logManager.updateStep(self.listUrlId.countNewId(), 0)
        if self.listUrlId.countNewId() != 0:
            self.imageManager.downloadImages(self.listUrlId.getList(), self.logManager)
            self.imageManager.relocateImages(self.listUrlId.getList(), self.logManager)
            # self.listUrlId.show()
            self.dbManager.updateData(self.listUrlId.getList(), self.logManager)
        print(self.dbManager.current_number_record,  self.dbManager.total_number_record)
        if self.dbManager.current_number_record < self.dbManager.total_number_record:
            self.logManager.addStepLog()
            self.logManager.writeLog()
            self.launch()
        else:
            self.logManager.updateTotal(datetime.datetime.now().strftime("%H:%M:%S"), 5)
            self.logManager.addStepLog()
            self.logManager.addTotalLog()
            self.logManager.writeLog()

def main():
    print(time.ctime())
    program = Program()
    program.launch()
    print(time.ctime())

if __name__ == "__main__":
    main()