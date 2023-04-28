from trello.lists.trello_objects_list import trelloObjectsList
from trello.singles.card import Card as trelloCard
from overrides import override
import requests
import pandas as pd

#coregir para obtener tarjetas de unas listas determinadas

class cardsList(trelloObjectsList):
    def __init__(self, listsList:list):
        self.__listsList:list = listsList
        self.__cardsInListsJson = self.requestTrelloObjectJson()
        self.__cardList:list = self.setCardsList()
        self.checkListType()
        self.checkItemsInListTypes()
      
            
    @override
    def requestTrelloObjectJson(self) -> list:
        #pedirle a trello el Json de las tarjetas en una lista
        def requestTrelloJson(listId:str):
            requestUrl = f"https://api.trello.com/1/lists/{listId}/cards"
            headers = {
                "Accept": "application/json"
            }
            query = trelloObjectsList.getTrelloApiCredentials()
            trelloResponse = requests.request(
                "GET",
                requestUrl,
                headers=headers,
                params=query
            )
            if trelloResponse.status_code != 200:
                raise Exception(f"Error requesting trello cards list json for board id {self.__boardId}. Status code: {trelloResponse.status_code}")
            return trelloResponse.json()
        cardsInListJson = []
        for listId in self.__listsList:
            cardsInListJson += requestTrelloJson(listId)
        return cardsInListJson
     
        
    def setCardsList(self) -> list:
        cardsList = []
        for card in self.__cardsInListsJson:
            cardsList.append(
                trelloCard(card["id"])
            )
        return cardsList
            
    
    @override
    def checkListType(self):
        assert isinstance(self.__cardList,list), "cardList must be type list"
        return True
    
    
    @override
    def checkItemsInListTypes(self) -> bool:
        for card in self.__cardList:
            if not isinstance(card, trelloCard):
                raise Exception(f"all items in card list must be instances of card. card #{card} in list is type {type(card)}.")
        return True
    
    
    @override
    def __df__(self):
        returnDf = pd.DataFrame()
        for card in self.__cardList:
            returnDf = pd.concat([returnDf,card.__df__()])
        return returnDf
    