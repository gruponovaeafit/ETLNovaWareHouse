from trello.lists.trelloObjectsList import trelloObjectsList
from trello.singles.label import label as trelloLabel
from overrides import override
import requests
import pandas as pd

class labelsList(trelloObjectsList):
    def __init__(self, boardId:str):
        self.__boardId = boardId
        self.__labelsListJson = self.requestTrelloObjectJson()
        self.__labelsList = self.setLabelsList()
        self.checkListType()
        self.checkItemsInListTypes()
    
    
    @override
    def requestTrelloObjectJson(self) -> list:
        #pedirle a trello el Json de las listas en un tablero
        requestUrl = f"https://api.trello.com/1/boards/{self.__boardId}/labels"
        query = trelloObjectsList.getTrelloApiCredentials()
        trelloResponse = requests.request(
            "GET",
            requestUrl,
            params=query
        )
        if trelloResponse.status_code != 200:
            raise Exception(f"Error requesting trello members list json for board id {self.__boardId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
    
    
    def setLabelsList(self):
        labelsList = []
        for label in self.__labelsListJson:
            if "peso" not in label["name"].lower(): #no guardar proyectos como tareas
                labelsList.append(
                    trelloLabel(label["id"])
                )
        return labelsList
    
    
    @override
    def checkListType(self):
        assert isinstance(self.__labelsList,list), "labelsList must be type list"
        return True
    
    
    @override
    def checkItemsInListTypes(self) -> bool:
        for label in self.__labelsList:
            if not isinstance(label, trelloLabel):
                raise Exception(f"all items in labels list must be instances of label. label #{label} in list is type {type(label)}.")
        return True
    
    
    @override
    def __df__(self):
        returnDf = pd.DataFrame()
        for label in self.__labelsList:
            returnDf = pd.concat([returnDf,label.__df__()])
        return returnDf

