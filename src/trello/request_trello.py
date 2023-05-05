from credentials import openCredentialsFile
from abc import ABC, abstractmethod

class requestTrello(ABC): #definicion de una clase abstracta
    
    def getTrelloApiCredentials() -> dict:        
        trelloCredentials = openCredentialsFile("C:\\Users\\Admin\\Desktop\\ETLNovaWareHouse\\src\\credentials.json")
        query = {
            "key":trelloCredentials["ApiKey"],
            "token":trelloCredentials["ApiToken"],
        }
        return query
    
    
    @abstractmethod
    def requestTrelloObjectJson(self):
        pass
    