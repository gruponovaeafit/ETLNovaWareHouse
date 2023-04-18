from trello.requestTrello import requestTrello
from abc import ABC, abstractmethod
from overrides import override


class trelloObjectsList(requestTrello, ABC):
    
    @abstractmethod
    def requestTrelloObjectJson(self):
        pass
    
    
    @override
    def getTrelloApiCredentials() -> dict:
        return requestTrello.getTrelloApiCredentials()
    
    
    @abstractmethod
    def checkListType(self):
        pass
    
    
    @abstractmethod
    def checkItemsInListTypes(self):
        pass
    
    
    @abstractmethod
    def __df__(self):
        pass