# ImageManager.py
import os
import shutil
from configparser import ConfigParser
from urllib3.poolmanager import PoolManager

config = ConfigParser()
config.read("config.ini")

class ImageManager:
    __path_temp_imgs = os.getcwd() + "/temp_imgs"
    __path_updated_imgs = os.getcwd() + "/updated_imgs"

    def downloadImages(self, listObject):
        poolmanager = PoolManager()
        for item in listObject:
            try:
                req = poolmanager.request('GET', item.url)
                extension = item.url[item.url.rfind("."):]
                with open(self.__path_temp_imgs + f"/{item.getId()}{extension}", 'wb') as img:
                    img.write(req.data)
            except Exception as err:
                print(f"Download image fault: {err}")
    
    def relocateImages(self):
        [shutil.move(os.path.join(self.__path_temp_imgs, img), self.__path_updated_imgs) for img in os.listdir(self.__path_temp_imgs)]