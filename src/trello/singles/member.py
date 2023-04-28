from trello.request_trello import requestTrello
from overrides import override
import requests
import pandas as pd


class Member(requestTrello):
    def __init__(self, memberId:str):
        self.__memberId:str = memberId
        self.__memberJson:dict = self.requestTrelloObjectJson()
        self.__fullName:str = self.requestTrelloMemberFullName()
        self.__userName:str =  self.requestTrelloMemberUserName()
        
    
    @override
    def requestTrelloObjectJson(self):
        requestUrl = f"https://api.trello.com/1/members/{self.__memberId}"
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
            raise Exception(f"Error requesting trello member json for member id {self.__memberId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
    
    
    def requestTrelloMemberFullName(self) -> str:
        return self.__memberJson["fullName"]
    
    
    def requestTrelloMemberUserName(self) -> str:
        return self.__memberJson["username"]
    
    
    def getFullName(self) -> str:
        return self.__fullName
    
    
    def getUserName(self) -> str:
        return self.__userName
    
    
    def __df__(self) -> pd.DataFrame:
        #funcion para obtener una representacion de dataframe de un miembro
        return pd.DataFrame(
            columns = ['idPersona', 'nombrePersona', 'usuarioTrelloPersona'],
            data = [[self.__memberId, self.__fullName, self.__userName]],
            dtype=str
            )