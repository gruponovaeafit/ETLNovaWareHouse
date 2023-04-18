from abc import ABC, abstractmethod
import json

class requestTrello(ABC): #definicion de una clase abstracta
    
    def getTrelloApiCredentials() -> dict:
        def openCredentialsFile(filePath):
            with open(filePath) as file:
                credentials = json.load(file)
            return credentials
        
        credentials = openCredentialsFile("C:\\Users\\Admin\\Desktop\\ETL_novaWareHouse\\src\\trello\\credentials.json")
        query = {
            "key":credentials["ApiKey"],
            "token":credentials["ApiToken"],
        }
        return query
    
    
    @abstractmethod
    def requestTrelloObjectJson(self):
        pass
    