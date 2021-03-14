# URLId.py
from itertools import groupby

class URLIdSaver:
    __url = ""
    __path = ""
    __id_list = []
    
    def __init__(self, url, list_id_product):
        self.__url = url
        self.__id_list = list_id_product
    
    @property
    def url(self):
        return self.__url
    
    def addIdList(self, list_id_product):
        self.__id_list.extend(list_id_product)

    def getId(self):
        return self.__id_list[0]
    
    def show(self):
        print("item:")
        print(self.__url)
        for item in self.__id_list:
            print(item, end= " ")
        print()

class ListURLId:
    __list_urlofidsaver = []

    def __init__(self):
        pass

    def addURLofIdSaver(self, urlidsaver):
        self.__list_urlofidsaver.append(urlidsaver)
    
    def updateList(self, listRecords):
        for url, group in groupby(listRecords, lambda pair: pair[1]):
            isExistURL, index = self.__checkExistURL(url)
            if isExistURL:
                self.__list_urlofidsaver[index].addIdList([id_product for id_product, _ in group])
                continue
            self.addURLofIdSaver(URLIdSaver(url, [id_product for id_product, _ in group]))
        
    def __checkExistURL(self, url):
        for item in self.__list_urlofidsaver:
            if item.url == url:
                return (True, self.__list_urlofidsaver.index(item))
        return (False, -1)

    def getList(self):
        return self.__list_urlofidsaver
    
    def show(self):
        for item in self.__list_urlofidsaver:
            item.show()