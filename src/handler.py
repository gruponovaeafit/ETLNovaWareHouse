from comparator import compareCardsLists, notifyChanges
from trello.lists.cards_list import cardsList
from trello.singles.card import Card
from dao import Dao
import pandas as pd

def getDbTasksStates(dbCon:Dao) -> pd.DataFrame:
    return dbCon.queryToDataBase(
        """SELECT idEstadoTarea, nombreEstadoTarea FROM EstadoTarea"""
    )

    
def getDbTasksList(dbCon:Dao, taskStateId:str) -> list:
    dbTasks:pd.DataFrame = dbCon.queryToDataBase(
        F"""SELECT idTarea, nombreTarea, idEstadoTarea, idUrgencia
            FROM Tareas
            GROUP BY idTarea, nombreTarea, idEstadoTarea, idUrgencia
            HAVING idEstadoTarea = \"{taskStateId}\";"""
    )
    dbTasksList:list = [
        Card(
            cardId=dbTasks["idTarea"][i],
            cardName=dbTasks["nombreTarea"][i],
            listId=dbTasks["idEstadoTarea"][i], 
            labelId=dbTasks["idEstadoTarea"][i],
        ) for i in range(0, len(dbTasks))
    ]
    return dbTasksList


def handleNewTasks4Db():
    dbCon = Dao("novaWareHouse")
    tasksStates:pd.DataFrame = getDbTasksStates(dbCon)
    for i in range(0, len(tasksStates)):
        print(f"Checking list {tasksStates['nombreEstadoTarea'][i]} for new changes...")
        dbCardsList:list = getDbTasksList(dbCon, tasksStates["idEstadoTarea"][i])
        trelloCardsList:list = cardsList(listsList=[tasksStates["idEstadoTarea"][i]]).getCardsList()
        missingIdsInTaskList:list = compareCardsLists(
            dbCardsList=dbCardsList,
            trelloCardsList=trelloCardsList    
        )
        missingCardsInDb:cardsList = cardsList(cardsList=[
            card for card in trelloCardsList if card.getCardId() in missingIdsInTaskList
        ]) #probablemente hay una forma mas optima de hacer esto sin necesidad de crear una nueva lista solo buscando en la de trello
        print(notifyChanges(missingCardsInDb.getCardsList()))
        userChoice = input("Do you want to insert the changes notified?\n(y/n)")
        if userChoice == "y":
            if dbCon.insertToDataBase(
                df_insert = missingCardsInDb.__df__(),
                dataBaseTableName="Tareas"
            ):
                print("Success!\n")
            else:
                print("Insertion failed\n")    
            print("---------------------------")
        else:
            print("---------------------------")
            continue
        
        
    
    
    


