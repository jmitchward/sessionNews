import requests
import json


def getSession(sessionID):
    getRequest = requests.get("https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getMasterList&state=" + sessionID)
    convertResponse = json.loads(getRequest.text)
    currentSession = convertResponse['masterlist']

    sessionName = currentSession['session']['session_name']
    print("Bill List retrieved for", sessionName)

    currentSession.pop('session')
    billList = list()

    for each in currentSession:
        billList.append((currentSession[each]['bill_id'], currentSession[each]['number'], currentSession[each]['title']))

    return billList





