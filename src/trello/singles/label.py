from trello.request_trello import requestTrello
from overrides import override
import requests
import pandas as pd

class Label(requestTrello):
    def __init__(self, labelId:str):
        self.__labelId = labelId
        self.__labelJson = self.requestTrelloObjectJson()
        self.__name:str = self.requestTrelloLabelName()
        self.__description:str = self.setLabelDescription()  
    
    
    @override
    def requestTrelloObjectJson(self):
        requestUrl = f"https://api.trello.com/1/labels/{self.__labelId}"
        query = requestTrello.getTrelloApiCredentials()
        trelloResponse = requests.request(
            "GET",
            requestUrl,
            params=query
        )
        if trelloResponse.status_code != 200:
            raise Exception(f"Error requesting trello label json for label id {self.__labelId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
    
    
    def requestTrelloLabelName(self) -> str:
        return self.__labelJson["name"].lower()
    
    
    def setLabelDescription(self) -> str:
        if self.__name == "¡urgente!":
            return "tareas que deban de ser completadas como maximo 5 dias despues de su fecha de creacion."
        elif self.__name == "medio urgente":
            return "tareas que deban de ser completadas como minimio 6 dias despues de su fecha de creacion, y como maximo 17 dias despues de su fecha de creacion."
        #descripcion de urgencia leve
        return "tareas que deben de ser completadas como minimo 18 dias despues de su fecha de creacion" 
    
    
    def __df__(self):
        return pd.DataFrame(
            columns = ['idUrgencia','tipoUrgencia','descripcionUrgencia'],
            data = [[self.__labelId, self.__name, self.__description]],
            dtype =str
        )