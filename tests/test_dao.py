from src.dao import dao
import pytest
import pandas as pd

def test_createConnectionEngine():
    databaseObject = dao("root", "root01", "192.168.1.53", "novaWareHouse")
    print(databaseObject)
    