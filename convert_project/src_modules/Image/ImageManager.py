# ImageManager.py
from configparser import ConfigParser
from urllib3.poolmanager import PoolManager
import shutil
import os

config = ConfigParser()
config.read("config.ini")

class ImageManager:
    __path_temp_imgs = os.getcwd() + "/temp_imgs"
    __path_updated_imgs = os.getcwd() + "/updated_imgs"

    def downloadImages(self, listObject):
        poolmanager = PoolManager()
        for item in listObject:
            if not item.isDownload():
                try:
                    req = poolmanager.request('GET', item.URL)
                    extension = item.URL[item.URL.rfind("."):]
                    with open(self.__path_temp_imgs + f"/{item.getId()}{extension}", 'wb') as img:
                        img.write(req.data)
                except Exception as err:
                    print(f"Download image fault: {err}")
    
    def relocateImages(self, listObject):
        for img in os.listdir(self.__path_temp_imgs):
            os.chmod(os.path.join(self.__path_temp_imgs, img), 0o0777)
            shutil.move(os.path.join(self.__path_temp_imgs, img), self.__path_updated_imgs)
        [item.setPath(self.__path_updated_imgs + f"/{item.getId()}") for item in listObject]