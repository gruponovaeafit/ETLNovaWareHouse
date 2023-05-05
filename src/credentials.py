#credentials handler
import json

def openCredentialsFile(pathToCredentials:str) -> dict:
    with open(pathToCredentials) as file:
        credentials:dict = json.load(file)
    return credentials