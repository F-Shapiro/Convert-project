# ImagePerformer.py
from configparser import ConfigParser
from PIL import Image
import os

config = ConfigParser()
config.read("config.ini")

class ImagePerformer:
    __img_width_max = int(config["image_size"]["img_width_max"])
    __img_height_max = int(config["image_size"]["img_height_max"])
    __path_temp_imgs = os.getcwd() + config["path"]["path_temp"]

    def convertImages(self, logManager):
        for img in os.listdir(self.__path_temp_imgs):
            try:
                with Image.open(os.path.join(self.__path_temp_imgs, img)) as image:
                    width, height = image.size
                    if width > self.__img_width_max or height > self.__img_height_max:
                        image = self.__resizeImage(image, width, height)
                    if img[img.rfind("."):].lower() == ".webp":
                        image.save(os.path.join(self.__path_temp_imgs, img))
                    else:
                        image.save(os.path.join(self.__path_temp_imgs, img.replace(img[img.rfind("."):], ".webp")), format = "WebP", lossless = True)
                os.remove(os.path.join(self.__path_temp_imgs, img))
            except Exception as err:
                # print(f"Convert image fault: {err}")
                logManager.writeFault(img[:img.rfind(".")])
                os.remove(os.path.join(self.__path_temp_imgs, img))
        logManager.updateStep(len(os.listdir(self.__path_temp_imgs)), 2)
    
    def __resizeImage(self, image, width, height):
        if width / height >= 1 and self.__img_width_max / self.__img_height_max >= 1:
            if width / height >= 1:
                if width / height >= self.__img_width_max / self.__img_height_max:
                    scale = self.__img_width_max / width
                else:
                    scale = self.__img_height_max / height
            else:
                if width / height <= self.__img_width_max / self.__img_height_max:
                    scale = self.__img_height_max / height
                else:
                    scale = self.__img_width_max / width
        else:
            scale = min(self.__img_width_max, self.__img_height_max) / max(width, height)
        return image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)