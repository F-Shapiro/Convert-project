# URLId.py
from itertools import groupby

class URLIdSaver:
    __path = ""
    
    def __init__(self, URL, list_id_product):
        self.__URL = URL
        self.__id_list = list_id_product
        self.__new_id_index = self.__id_list.index(list_id_product[0])
    
    @property
    def URL(self):
        return self.__URL
    
    @property
    def path(self):
        return self.__path
    
    def setPath(self, path):
        self.__path = path
    
    def addIdList(self, list_id_product):
        self.__id_list.extend(list_id_product)
        self.__new_id_index = self.__id_list.index(list_id_product[0])

    def getId(self):
        return self.__id_list[0]
    
    def getNewIdList(self, reset=True):
        index = self.__new_id_index
        if reset:
            self.__new_id_index = len(self.__id_list)
        return self.__id_list[index:]
    
    def isDownload(self):
        return len(self.__path) != 0
    
    def show(self):
        print("item:")
        print(self.__URL)
        print(self.__path)
        for item in self.__id_list:
            print(item, end= " ")
        print()

class ListURLId:
    __list_urlIdSaver = []

    def __addURLIdSaver(self, urlIdSaver):
        self.__list_urlIdSaver.append(urlIdSaver)
    
    def updateList(self, listRecords):
        for URL, group in groupby(listRecords, lambda pair: pair[1]):
            print(URL)
            if self.__isTwiceURL(URL):
                URL = self.__correctingURL(URL)

            if self.__isIncorrectURL(URL):
                continue

            if self.__isIncorrectExtension(URL):
                continue

            if self.__isExistURL(URL):
                self.__list_urlIdSaver[self.__findByURL(URL)].addIdList([id_product for id_product, _ in group])
            else:
                self.__addURLIdSaver(URLIdSaver(URL, [id_product for id_product, _ in group]))
        
    def __isExistURL(self, URL):
        for item in self.__list_urlIdSaver:
            if item.URL == URL:
                return True
        return False
    
    def __findByURL(self, URL):
        for item in self.__list_urlIdSaver:
            if item.URL == URL:
                return self.__list_urlIdSaver.index(item)
        return -1
    
    def __isIncorrectURL(self, URL):
        return URL.count(" ") > 0
    
    def __isIncorrectExtension(self, URL):
        extensions = [".jpg", ".jpeg", ".png", ".webp"]
        return URL[URL.rfind("."):].lower() not in extensions

    def __isTwiceURL(self, URL):
        return URL.count("http") > 1
    
    def __correctingURL(self, URL):
        return URL[:URL.rfind(" http")]

    def getList(self):
        return self.__list_urlIdSaver
    
    def countNewId(self):
        count = 0
        for item in self.__list_urlIdSaver:
            count += len(item.getNewIdList(reset=False))
        return count
    
    def show(self):
        for item in self.__list_urlIdSaver:
            item.show()