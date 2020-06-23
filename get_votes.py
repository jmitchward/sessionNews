import requests
import json


def getVotes(rollID):
    getRequest = requests.get(
        "https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getRollcalll&id=" + rollID)
    convertResponse = json.loads(getRequest.text)
    currentRoll = convertResponse['roll_call']

    voteList = list()

    for each in currentRoll['votes']:
        voteList.append((each['people_id'], each['vote_text']))
        return voteList
