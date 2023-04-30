from comparator import Comparator
from trello.lists import cards_list#, listsList, membersList, labelsList
from trello.singles.card import Card
from dao import Dao
from datetime import datetime
import pandas as pd

if __name__ == '__main__':
    
    #obtener el id de las listas urgente, medio urgente y demas
    dbListsId = dbConnection.queryToDataBase(
        """SELECT * FROM EstadoTarea"""
    )
    
    
    #lista demas
    
    listDemasId = dbListsId["idEstadoTarea"][dbListsId["nombreEstadoTarea"] == "por realizar demas"] #saco Id de la lista demas
    
    
    
    dbTasksDemasList = dbConnection.queryToDataBase(
        f"""SELECT idTarea, idEstadoTarea, idUrgencia, fechaInicio, fechaUltimaActividadTarea
            FROM Tareas 
            GROUP BY idTarea, idEstadoTarea, idUrgencia, fechaInicio, fechaUltimaActividadTarea
            HAVING idEstadoTarea = \"{listDemasId.values[0]}\";"""
    )   
    
    #creo la lista de cartas
    dbTasksList = []
    for i in range(0, len(dbTasksDemasList)):
        taskId = dbTasksDemasList["idTarea"][i]
        membersInTask = dbConnection.queryToDataBase(f"""SELECT idPersona FROM Tareas WHERE idTarea = \"{taskId}\";""").values
        dbTasksList.append(Card(
            cardId=taskId,
            listId=dbTasksDemasList["idEstadoTarea"][i],
            membersId=membersInTask,
            labelId=dbTasksDemasList["idUrgencia"][i],
            startDate=dbTasksDemasList["fechaInicio"][i],
            endDate=dbTasksDemasList["fechaUltimaActividadTarea"][i]
        ))
    
    dbTasksList = sorted(dbTasksList) #tareas de la base de datos ordenadas segun criterio
    
    trelloCardsList = cards_list.cardsList(listDemasId) #tareas de trello
    trelloCards = trelloCardsList.getCardsList()
    
    
    changes_count = 0
    for i, dbCard in enumerate(dbTasksList):
        if Comparator.compareCards(dbCard, trelloCards[i]) is False:
            changes_count += 1
    print(f"Changes detected: {changes_count}")
            
    






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
    
    
    