# URLofId.py

class URLofIdSaver:
    __url = ""
    __path = ""
    __id_list = []
    
    def __init__(self, url, id_product = None):
        self.__url = url
        if id_product is not None:
            self.addId(id_product)
    
    def addId(self, id_product):
        self.__id_list.append(id_product)

    def getId(self):
        return self.__id_list[len(self.__id_list)-1]
    
    @property
    def url(self):
        return self.__url
    
    def show(self):
        print("item:")
        print(self.__url)
        for item in self.__id_list:
            print(item, end= " ")
        print()
    
    def __del__(self):
        self.__url = None
        self.__path = None
        self.__id_list.clear()

class StackURLofId:
    __list_urlofidsaver = []

    def __init__(self):
        pass

    def addUrlofidsaver(self, urlofidsaver):
        self.__list_urlofidsaver.append(urlofidsaver)
    
    def updateList(self, listRecords):
        id_list = []
        URL_list = []
        for id_product, url in listRecords:
            id_list.append(id_product)
            URL_list.append(url)
        listRecords.clear()

        i = 0
        while len(URL_list) != 0:
            print()
            answer, index = self.__checkExistURL(URL_list[i])
            if answer:
                self.__list_urlofidsaver[index].addId(id_list.pop(i))
                URL_list.pop(i)
            elif URL_list.count(URL_list[i]) > 1:
                urlofidsaver = URLofIdSaver(URL_list[i])
                urlofidsaver.show()
                for j in range(len(URL_list)-1, -1, -1):
                    if URL_list[j] == URL_list[i]:
                        urlofidsaver.addId(id_list.pop(j))
                        URL_list.pop(j)
                self.addUrlofidsaver(urlofidsaver)
            else:
                urlofidsaver = URLofIdSaver(URL_list[i], id_list.pop(i))
                URL_list.pop(i)
                self.addUrlofidsaver(urlofidsaver)
        
    def __checkExistURL(self, url):
        for item in self.__list_urlofidsaver:
            if item.url == url:
                return (True, self.__list_urlofidsaver.index(item))
        return (False, -1)

    # def pop(self):
    #     return self.__list_urlofidsaver.pop(len(self.__list_urlofidsaver)-1)

    def getGenerator(self):
        for item in self.__list_urlofidsaver:
            yield item
    
    def show(self):
        for item in self.__list_urlofidsaver:
            item.show()
    
    def __del__(self):
        self.__list_urlofidsaver.clear()