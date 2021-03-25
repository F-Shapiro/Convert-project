# ImageManager.py
from urllib3.poolmanager import PoolManager
from configparser import ConfigParser
import shutil
import os

config = ConfigParser()
config.read("config.ini")

class ImageManager:
    __path_temp_imgs = os.getcwd() + config["path"]["path_temp"]
    __path_updated_imgs = os.getcwd() + config["path"]["path_update"]

    def downloadImages(self, listObject, logManager):
        poolmanager = PoolManager()
        for item in listObject:
            if not item.isDownload():
                try:
                    req = poolmanager.request('GET', item.URL)
                    extension = item.URL[item.URL.rfind("."):]
                    with open(self.__path_temp_imgs + f"/{item.getId()}{extension}", 'wb') as img:
                        img.write(req.data)
                except Exception as err:
                    # print(f"Download image fault: {err}")
                    # print(item.URL)
                    logManager.writeFault(item.getId())
        logManager.updateStep(len(os.listdir(self.__path_temp_imgs)), 1)
    
    def relocateImages(self, listObject, logManager):
        count_relocate = 0
        for img in os.listdir(self.__path_temp_imgs):
            try:
                os.chmod(os.path.join(self.__path_temp_imgs, img), 0o0777)
                shutil.move(os.path.join(self.__path_temp_imgs, img), self.__path_updated_imgs)
                count_relocate += 1
            except OSError as err:
                # print(f"Relocate image fault: {err}")
                logManager.writeFault(img[:img.rfind(".")])
        for item in listObject:
            if item.isDownload():
                continue
            if str(item.getId()) + ".webp" in os.listdir(self.__path_updated_imgs):
                item.setPath(self.__path_updated_imgs + f"/{item.getId()}") 
        logManager.updateStep(count_relocate, 3)