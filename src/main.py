from trello.lists import cardsList, listsList, membersList, labelsList
from dao import dao
import pandas as pd


if __name__ == "__main__":
    boardId = "63f02f3229c0bc3d81731587"
    listsListing = listsList.listsList("63f02f3229c0bc3d81731587")
    #members = membersList.membersList(boardId)
    listsIds = list(set(listsListing.__df__()["idEstadoTarea"]))
    cardList = cardsList.cardsList(listsIds)
    
    dbConnection = dao(
        "",
        "",
        "",
        ""
    )
    
    
    
    if dbConnection.insertToDataBase(cardList.__df__(), "Tareas"):
        print("All Done! INSERT Succesfull")
    else:
        print("Something went wrong")
    
    
    