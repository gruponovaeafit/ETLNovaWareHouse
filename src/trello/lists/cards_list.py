from trello.lists.trello_objects_list import trelloObjectsList
from trello.singles.card import Card as trelloCard
from overrides import override
import requests
import pandas as pd

#coregir para obtener tarjetas de unas listas determinadas

class cardsList(trelloObjectsList):
    
    def __init__(self, cardsList:list=False, listsList:list=False):
        if cardsList is not False:
            self.__cardsList = cardsList
        else:
            assert isinstance(listsList, list), "listsList must be a list"
            assert len(listsList) > 0, "listsList must have at least one element"
            self.__listsList:list = listsList
            self.__cardsInListsJson = self.requestTrelloObjectJson()
            self.__cardsList:list = self.setCardsList()
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
                raise Exception(f"Error requesting trello cards list json. Status code: {trelloResponse.status_code}")
            return trelloResponse.json()
        cardsInListJson = []
        for listId in self.__listsList:
            cardsInListJson += requestTrelloJson(listId)
        return cardsInListJson
     
        
    def setCardsList(self, newCardsList:list = False) -> list:
        #retorna lista de cartas ordenadas de mas vieja a mas nueva
        if newCardsList is False:
            cardsList = []
            for card in self.__cardsInListsJson:
                cardsList.append(
                    trelloCard(card["id"])
                )
            return cardsList
        self.__cardsList = newCardsList
            
    
    def getCardsList(self) -> list:
        return self.__cardsList
    
    
    @override
    def checkListType(self):
        assert isinstance(self.__cardsList,list), "cardList must be type list"
        return True
    
    
    @override
    def checkItemsInListTypes(self) -> bool:
        for card in self.__cardsList:
            if not isinstance(card, trelloCard):
                raise Exception(f"all items in card list must be instances of card. card #{card} in list is type {type(card)}.")
        return True
    
    
    @override
    def __df__(self):
        returnDf = pd.DataFrame()
        for card in self.__cardsList:
            returnDf = pd.concat([returnDf,card.__df__()])
        return returnDf
    