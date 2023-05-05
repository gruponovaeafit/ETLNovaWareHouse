from trello.singles.card import Card


def compareCardsLists(dbCardsList:list, trelloCardsList:list) -> list:
    assert isinstance(dbCardsList, list) and isinstance(trelloCardsList, list), "Both atributes must be lists"
    idsDbCardsList = [card1.getCardId() for card1 in dbCardsList]
    idsTrelloCardsList = [card2.getCardId() for card2 in trelloCardsList]
    missingCardsIdsInDb:list = list(set(idsTrelloCardsList) - set(idsDbCardsList)) #lista de Ids de cards por añadir a la base de datos 
    return missingCardsIdsInDb


def notifyChanges(missingCardsIdsInDb:list) -> str:
    if len(missingCardsIdsInDb) == 0:
        return "No changes to resolve\n"
    message = "Here is the list of changes to resolve.\nAdd(+)\n"
    card:Card
    for i,card in enumerate(missingCardsIdsInDb):
        message += f"{card.__df__()}\n"
    return message
    
        
        


    
