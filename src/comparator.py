from trello.singles import card
from trello.lists import cards_list

class Comparator:
    @classmethod
    def compareCards(card1:card, card2:card) -> bool:
        return card1.__dict__ == card2.__dict__
    
    
    @classmethod
    def compareCardsLists():
        pass
    
