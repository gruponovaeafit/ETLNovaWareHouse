from trello.lists.trello_objects_list import trelloObjectsList
from trello.singles.member import member as trelloMember
from overrides import override
import requests
import pandas as pd


class membersList(trelloObjectsList):
    def __init__(self, boardId:str):
        self.__boardId = boardId
        self.__membersListJson:list = self.requestTrelloObjectJson()
        self.__membersList:list = self.setMembersList()
        self.checkListType()
        self.checkItemsInListTypes()
           
           
    @override
    def requestTrelloObjectJson(self) -> list:
        #pedirle a trello el Json de las listas en un tablero
        requestUrl = f"https://api.trello.com/1/boards/{self.__boardId}/members"
        query = trelloObjectsList.getTrelloApiCredentials()
        trelloResponse = requests.request(
            "GET",
            requestUrl,
            params=query
        )
        if trelloResponse.status_code != 200:
            raise Exception(f"Error requesting trello members list json for board id {self.__boardId}. Status code: {trelloResponse.status_code}")
        return trelloResponse.json()
     
    
    def setMembersList(self) -> list:
        #[{"id":###, "fullName":###, "username":###},{"id":###, "fullName":###, "username":###},{"id":###, "fullName":###, "username":###}]
        membersList = []
        for member in self.__membersListJson:
            membersList.append(
                trelloMember(member["id"])
            )
        return membersList
            
    
    @override
    def checkListType(self):
        assert isinstance(self.__membersList,list), "membersList must be type list"
        return True
    
    
    @override
    def checkItemsInListTypes(self) -> bool:
        for member in self.__membersList:
            if not isinstance(member, trelloMember):
                raise Exception(f"all items in members list must be instances of member. member #{member} in list is type {type(member)}.")
        return True
    
    
    @override
    def __df__(self):
        returnDf = pd.DataFrame()
        for member in self.__membersList:
            returnDf = pd.concat([returnDf,member.__df__()])
        return returnDf
    