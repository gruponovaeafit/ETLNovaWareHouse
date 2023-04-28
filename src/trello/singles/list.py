#objeto trello list
from overrides import override
from trello.request_trello import requestTrello
import requests
import pandas as pd


class List(requestTrello):
    def __init__(self, listId:str):
        self.__listId = listId
        self.__listJson = self.requestTrelloObjectJson()
        self.__name = self.requestTrelloListName()
        self.__state = self.setListState()
        
        
    @override
    def requestTrelloObjectJson(self) -> dict:
        #pedirle a trello el Json de una tarjeta
        requestUrl = f"https://api.trello.com/1/lists/{self.__listId}"
        query = requestTrello.getTrelloApiCredentials()
        trelloResponse = requests.request(
            "GET",
            requestUrl,
            params=query
        )
        if trelloResponse.status_code != 200:
            raise Exception(f"Error requesting trello list json for list id {self.__listId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
    
    
    def requestTrelloListName(self) -> str:
        return self.__listJson["name"].lower()
    
    
    def setListState(self) -> str:
        if (self.__name == "urgentes") or (self.__name == "medio urgentes") or (self.__name == "demas"):
            return f"por realizar {self.__name}"
        return self.__name
    
    
    def getId(self) -> str:
        return self.__listId
    
    
    def __df__(self) -> pd.DataFrame:
        return pd.DataFrame(
            columns = ['idEstadoTarea','nombreEstadoTarea'],
            data = [[self.__listId, self.__state]],
            dtype =str
        )