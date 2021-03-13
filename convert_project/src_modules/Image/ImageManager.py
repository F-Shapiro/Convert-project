# ImageManager.py
import os
import sys
from configparser import ConfigParser
from urllib3.poolmanager import PoolManager

config = ConfigParser()
config.read("config.ini")

class ImageManager:
    __path_temp_imgs = os.getcwd() + "/temp_imgs"
    __path_updated_imgs = os.getcwd() + "/updated_imgs"
    
    def __init__(self):
        pass

    def downloadImage(self, generator):
        poolmanager = PoolManager()
        for item in generator:
            try:
                req = poolmanager.request('GET', item.url)
                extension = item.url[item.url.rfind("."):]
                with open(self.__path_temp_imgs + f"/{item.getId()}{extension}", 'wb') as img:
                    img.write(req.data)
            except Exception as err:
                print(f"Download image fault: {err}")
    
    def __del__(self):
        pass