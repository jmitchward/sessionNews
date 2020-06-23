import requests
import json


def getSessions():
    getRequest = requests.get("https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getSessionList&id=KY")
    convertResponse = json.loads(getRequest.text)
    sessions = convertResponse['sessions']

    sessionList = list()

    for each in sessions:
        sessionList.append((each['session_id'], each['name']))

    return sessionList
