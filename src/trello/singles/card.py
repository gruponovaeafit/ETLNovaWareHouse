#objeto trello card
from overrides import override
from trello.requestTrello import requestTrello
import requests
from datetime import datetime
import pandas as pd


class card(requestTrello):
    def __init__(self,cardId:str):
        self.__cardId:str = cardId
        self.__cardJson:dict = self.requestTrelloObjectJson()
        self.__cardName:str = self.requestTrelloCardName()
        self.__description = self.requestTrelloCardDescription()
        self.__url:str = self.requestTrelloCardUrl()
        self.__startDate:str = self.requestTrelloCardStartDate()
        self.__listId:str = self.requestTrelloCardListId()
        self.__boardId = self.requestTrelloCardBoardId()
        self.__membersId:list = self.requestTrelloCardMembersId()
        self.__labelId:str = self.requestTrelloCardLabelId()
        self.__endDate:str = self.requestTrelloCardEndDate()
        self.__dateLastActivity:str = self.requestTrelloCardDateLastActivity()
        
    
    @override
    def requestTrelloObjectJson(self) -> dict:
        #pedirle a trello el Json de una tarjeta
        requestUrl = f"https://api.trello.com/1/cards/{self.__cardId}"
        headers = {
            "Accept": "application/json"
        }
        query = requestTrello.getTrelloApiCredentials()
        trelloResponse = requests.request(
            "GET",
            requestUrl,
            headers=headers,
            params=query
        )
        if trelloResponse.status_code != 200:
            raise Exception(f"Error requesting trello card json for card id {self.__cardId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
    
    
    def requestTrelloCardName(self) -> str:
        return self.__cardJson["name"]
    
    
    def requestTrelloCardDescription(self) -> str:
        return self.__cardJson["desc"]
        
    
    def requestTrelloCardUrl(self) -> str:
        return self.__cardJson["shortUrl"]
    
    
    def requestTrelloCardStartDate(self) -> str:
        return datetime.strptime(self.__cardJson["start"],'%Y-%m-%dT%H:%M:%S.%fZ')
    
    
    def requestTrelloCardListId(self) -> str:
        return self.__cardJson["idList"]
    
    
    def requestTrelloCardBoardId(self) -> str:
        return self.__cardJson["idBoard"]
    
    
    def requestTrelloCardMembersId(self) -> list:
        return self.__cardJson["idMembers"]
    
    
    def requestTrelloCardLabelId(self) -> str:
        return self.__cardJson["idLabels"][0]
    
    
    def requestTrelloCardEndDate(self) -> datetime:
        if isinstance(self.__cardJson["due"],str):
            return datetime.strptime(self.__cardJson["due"],'%Y-%m-%dT%H:%M:%S.%fZ')
        return None
    
    
    def requestTrelloCardDateLastActivity(self) -> datetime:
        return datetime.strptime(self.__cardJson["dateLastActivity"],'%Y-%m-%dT%H:%M:%S.%fZ')
    
    
    def getCardId(self) -> str:
        return self.__cardId
    
    
    def getCardName(self) -> str:
        return self.__cardName
    

    def getUrl(self) -> str:
        return self.__url
    

    def getStartDate(self) -> str:
        return self.__startDate
    
    
    def getListId(self) -> str:
        return self.__listId
    
    
    def getMembersId(self) -> list:
        return self.__membersId
        
    
    def getLabelId(self) -> str:
        return self.__labelId
    
        
    def getEndDate(self) -> str:
        return self.__endDate
    
    
    def getDateLastAcitivity(self) -> str:
        return self.__dateLastActivity
    
    
    def __df__(self) -> pd.DataFrame:
        #funcion para obtener una representacion de dataframe de
        #una tarjeta
        data = []
        for memberId in self.__membersId:
            row = [self.__cardId, self.__labelId, self.__listId, self.__boardId, memberId, self.__cardName,
                    self.__description, self.__startDate, self.__endDate, self.__url, self.__dateLastActivity]
            data.append(row)
        
        return pd.DataFrame(
            #ids VARCHAR(32)
            #nombre tarea tinyText
            #decripcion text
            #fechaInicio dateTime not null
            #fechaFin dateTime 
            #urlTarea ¿tinytext o text?
            #fechaUltimaActividadTarea dateTime 
            columns = ['idTarea', 'idUrgencia', 'idEstadoTarea', 'idEspacioTrabajo', 'idPersona', 'nombreTarea', 
                       'descripcionTarea', 'fechaInicio', 'fechaFin', 'urlTarea', 'fechaUltimaActividadTarea'],
            data = data
        )
            
            
        