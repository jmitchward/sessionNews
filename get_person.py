import requests
import json


def getPerson(personID):
    getRequest = requests.get(
        "https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getPerson&id=" + str(personID))
    convertResponse = json.loads(getRequest.text)
    currentPerson = convertResponse['person']

    return currentPerson

