# URLId.py
from itertools import groupby

class URLIdSaver:
    __URL = ""
    __path = ""
    __id_list = []
    
    def __init__(self, URL, list_id_product):
        self.__URL = URL
        self.__id_list = list_id_product
    
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

    def getId(self):
        return self.__id_list[0]
    
    def getIdList(self):
        return self.__id_list
    
    def isDownload(self):
        return True if len(self.__path) != 0 else False
    
    def show(self):
        print("item:")
        print(self.__URL)
        print(self.__path)
        for item in self.__id_list:
            print(item, end= " ")
        print()

class ListURLId:
    __list_urlofidsaver = []

    def __init__(self):
        pass

    def __addURLofIdSaver(self, urlidsaver):
        self.__list_urlofidsaver.append(urlidsaver)
    
    def updateList(self, listRecords):
        for URL, group in groupby(listRecords, lambda pair: pair[1]):
            if self.__isIncorrectURL(URL):
                self.__correctingURL(URL)

            if self.__isExistURL(URL):
                self.__list_urlofidsaver[self.__findByURL(URL)].addIdList([id_product for id_product, _ in group])
            else:
                self.__addURLofIdSaver(URLIdSaver(URL, [id_product for id_product, _ in group]))
        
    def __isExistURL(self, URL):
        for item in self.__list_urlofidsaver:
            if item.URL == URL:
                return True
        return False
    
    def __findByURL(self, URL):
        for item in self.__list_urlofidsaver:
            if item.URL == URL:
                return self.__list_urlofidsaver.index(item)
        return -1
    
    def __isIncorrectURL(self, URL):
        if URL.find(" ") != -1:
            return True
        return False
    
    def __correctingURL(self, URL):
        return URL[:URL.find(" ")]

    def getList(self):
        return self.__list_urlofidsaver
    
    def show(self):
        for item in self.__list_urlofidsaver:
            item.show()