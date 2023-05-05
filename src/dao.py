#objecto DAO (Database Access Object)
from credentials import openCredentialsFile
import sqlalchemy as sa
import pandas as pd


class Dao:
    def __init__(self, dbName, userName=False, passwordUser=False, dbIp=False):
        self.__dbName = dbName
        #si no me dan los atributos necesarios para generar la card le pido a trello la card
        if any(attribute is False for attribute in [userName, passwordUser, dbIp]):
            self.__dbCredentials = openCredentialsFile("C:\\Users\\Admin\\Desktop\\ETLNovaWareHouse\\src\\credentials.json")
            self.__userName = self.getDbUserName()
            self.__passwordUser = self.getpassWord4User()
            self.__dbIp = self.getDbIp()
            self.__connectionEngine = self.createConnectionEngine() #crear connexion con base de datos desde el constructor
        else:
            self.__userName = userName
            self.__passwordUser = passwordUser
            self.__dbIp = dbIp
    
    
    def getDbUserName(self) -> str:
        return self.__dbCredentials["dbUserName"]
    
    
    def getpassWord4User(self) -> str:
        return self.__dbCredentials["dbPassword"]
    
    
    def getDbIp(self) -> str:
        return self.__dbCredentials["dbIp"]
    
        
    def createConnectionEngine(self) -> str:
        connectionEngine = sa.create_engine(
            #estructura string de conexion: mysql+pymysql://{user}:{pw}@{db_ip}/{db_name}
            f"mysql+pymysql://{self.__userName}:{self.__passwordUser}@{self.__dbIp}/{self.__dbName}"
        )
        return connectionEngine
    
    
    def queryToDataBase(self, query:str) -> pd.DataFrame:
        df_query:pd.DataFrame = pd.read_sql_query(query, con=self.__connectionEngine) #creo un dataframe con los datos retornados por la base de datos
        return df_query
    
    
    def insertToDataBase(self, df_insert:pd.DataFrame, dataBaseTableName:str) -> bool:
        assert isinstance(df_insert, pd.DataFrame), "df_insert must be a DataFrame"
        assert len(df_insert) > 0, "cannot insert an empty DataFrame"
        #si lo que me retorna la funcion es un numero entero es que los datos fueron ingresados exitosamente
        if isinstance(df_insert.to_sql(dataBaseTableName, con=self.__connectionEngine, if_exists='append', index=False), int):
            return True 
        return False
    