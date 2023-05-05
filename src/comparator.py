
@classmethod
def compareCardsLists(cls, dbCardsList:list, trelloCardsList:list) -> list:
    idsDbCardsList = [card1.getCardId() for card1 in dbCardsList]
    idsTrelloCardsList = [card2.getCardId() for card2 in trelloCardsList]
    missingIdsInDb:list = list(set(idsTrelloCardsList) - set(idsDbCardsList)) #lista de Ids de cards por añadir a la base de datos 
    return missingIdsInDb
    
        
        


    
