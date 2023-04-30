from trello.singles.card import Card
from trello.lists import cards_list

class Comparator:
    @classmethod
    def compareCards(cls, card1:Card, card2:Card) -> bool:
        dictCard1, dictCard2 = card1.__dict__, card2.__dict__
        #si alguna de las dos cartas tiene menos llaves las comparo con las llaves en comun
        if len(dictCard1.keys()) != len(dictCard2.keys()):
            #en caso de que la carta 1 tenga mas llaves que la carta 2 comparo por medio de las llaves de la carta 2
            if len(dictCard1.keys()) > len(dictCard2.keys()):
                dictCard1 = {key : dictCard1[key] for key in dictCard2.keys()}
            #en caso contrario comparo con las llaves de la carta 1
            else:
                dictCard2 = {key : dictCard2[key] for key in dictCard1.keys()}
        else:
            return dictCard1 == dictCard2
        
    
    @classmethod
    def compareCardsLists(cls, cardsList1:list, cardsList2:list) -> int:
        #retorna el numero de cambios detectados entre las dos listas
        changesCounter:int = 0
        for card1, card2 in zip(cardsList1, cardsList2):
            if cls.compareCards(card1, card2) is False:
                changesCounter += 1
            return changesCounter

    
