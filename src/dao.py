#objecto DAO (Database Access Object)
import sqlalchemy as sa
import pandas as pd


class Dao:
    def __init__(self, userName, passwordUser, dbIp, dbName):
        self.__userName = userName
        self.__passwordUser = passwordUser
        self.__dbIp = dbIp
        self.__dbName = dbName
        self.__connectionEngine = self.createConnectionEngine() #crear connexion con base de datos desde el constructor
    
    
    def createConnectionEngine(self) -> sa.engine.base.Engine:
        connectionEngine = sa.create_engine(
            #estructura string de conexion: mysql+pymysql://{user}:{pw}@{db_ip}/{db_name}
            f"mysql+pymysql://{self.__userName}:{self.__passwordUser}@{self.__dbIp}/{self.__dbName}"
        )
        return connectionEngine
    
    
    def queryToDataBase(self, query:str) -> pd.DataFrame:
        df_query = pd.read_sql_query(query, con=self.__connectionEngine) #creo un dataframe con los datos retornados por la base de datos
        return df_query
    
    
    def insertToDataBase(self, df_insert:pd.DataFrame, dataBaseTableName:str) -> bool:
        assert isinstance(df_insert, pd.DataFrame), "df_insert must be a DataFrame"
        #si lo que me retorna la funcion es un numero entero es que los datos fueron ingresados exitosamente
        if isinstance(df_insert.to_sql(dataBaseTableName, con=self.__connectionEngine, if_exists='append', index=False), int):
            return True 
        return False
    