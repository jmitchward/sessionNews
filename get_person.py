import requests
import json


def getPerson(personID):
    getRequest = requests.get(
        "https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getPerson&id=" + personID)
    convertResponse = json.loads(getRequest.text)
    currentPerson = convertResponse['person']

    for each in currentPerson:
        return each['role'], each['name'], each['district'], each['party']
