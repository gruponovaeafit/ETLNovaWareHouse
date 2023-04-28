#from trello.lists import cardsList, listsList, membersList, labelsList
from trello.singles.card import Card
from dao import dao
from datetime import datetime
import pandas as pd

if __name__ == '__main__':
    c1 = Card(cardId='6434ec5be502e715cf661265', 
                listId='63f02f3229c0bc3d8173158f',
                membersId=['63f2ca4d791e17971239f926','63f2a578bb97677b68d2f8c7','5e4572c48caf2277dbfb0274','63fcd0afcce26c636b6bc425'],
                labelId='63f0355e416bd7f1dd8a88fc',
                endDate=datetime.strptime('2023-04-21 19:00:00','%Y-%m-%d %H:%M:%S'))
    c2 = Card(cardId='6434ec5be502e715cf661265', 
              listId='63f02f3229c0bc3d8173158f',
              membersId=['63f2ca4d791e17971239f926','63f2a578bb97677b68d2f8c7','5e4572c48caf2277dbfb0274','63fcd0afcce26c636b6bc425'],
              labelId='63f0355e416bd7f1dd8a88fc',
              endDate=datetime.strptime('2023-04-21 19:00:00','%Y-%m-%d %H:%M:%S'))
    print(c1.__dict__ == c2.__dict__)
    






# if __name__ == "__main__":
#     boardId = "63f02f3229c0bc3d81731587"
#     listsListing = listsList.listsList("63f02f3229c0bc3d81731587")
#     #members = membersList.membersList(boardId)
#     listsIds = list(set(listsListing.__df__()["idEstadoTarea"]))
#     cardList = cardsList.cardsList(listsIds)
    
#     dbConnection = dao(
#         "",
#         "",
#         "",
#         ""
#     )
    
    
    
#     if dbConnection.insertToDataBase(cardList.__df__(), "Tareas"):
#         print("All Done! INSERT Succesfull")
#     else:
#         print("Something went wrong")
    
    
    