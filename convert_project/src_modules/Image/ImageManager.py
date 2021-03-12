# ImageManager.py
import os
import sys
from configparser import ConfigParser
from urllib3.poolmanager import PoolManager

config = ConfigParser()
config.read("config.ini")

class ImageManager:
    __path = os.getcwd() + "/temp_imgs"
    
    def __init__(self):
        pass

    def downloadImage(self, listRecords):
        poolmanager = PoolManager()
        for id_product, url in listRecords:
            try:
                req = poolmanager.request('GET', url)
                with open(self.__path + f"/{id_product}.png", 'wb') as img:
                    img.write(req.data)
            except Exception as err:
                print(f"Download image fault: {err}")
    def __del__(self):
        pass