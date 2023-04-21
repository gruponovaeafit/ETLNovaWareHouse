from trello.lists.trello_objects_list import trelloObjectsList
from trello.singles.list import list as trelloList
from overrides import override
import requests
import pandas as pd


class listsList(trelloObjectsList):
    def __init__(self, boardId:str):
        self.__boardId = boardId
        self.__listsListJson:list = self.requestTrelloObjectJson()
        self.__listsList:list = self.setListsList()
        self.checkListType()
        self.checkItemsInListTypes()
    
    
    @override
    def requestTrelloObjectJson(self) -> list:
        #pedirle a trello el Json de las listas en un tablero
        requestUrl = f"https://api.trello.com/1/boards/{self.__boardId}/lists"
        query = trelloObjectsList.getTrelloApiCredentials()
        trelloResponse = requests.request(
            "GET",
            requestUrl,
            params=query
        )
        if trelloResponse.status_code != 200:
            raise Exception(f"Error requesting trello members list json for board id {self.__boardId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
     
    
    def setListsList(self) -> list:
        #[{"id":###, "name":###},{"id":###, "name":###},{"id":###, "name":###}]
        listsList = []
        for listing in self.__listsListJson:
            if listing["name"].lower() != "proyectos": #no guardar proyectos como tareas
                listsList.append(
                    trelloList(listing["id"])
                )
        return listsList
    
    
    @override
    def checkListType(self):
        assert isinstance(self.__listsList,list), "labelsList must be type list"
        return True
    
    
    @override
    def checkItemsInListTypes(self) -> bool:
        for list in self.__listsList:
            if not isinstance(list, trelloList):
                raise Exception(f"all items in lists list must be instances of list. list #{list} in list is type {type(list)}.")
        return True
    
    
    @override
    def __df__(self):
        returnDf = pd.DataFrame()
        for label in self.__listsList:
            returnDf = pd.concat([returnDf,label.__df__()])
        return returnDf