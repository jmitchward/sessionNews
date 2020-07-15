import requests
import json
import get_person


def getVotes(rollID):
    getRequest = requests.get(
        "https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getRollcall&id=" + str(rollID))
    convertResponse = json.loads(getRequest.text)
    currentRoll = convertResponse['roll_call']

    voteList = list()

    for each in currentRoll['votes']:
        eachPerson = get_person.getPerson(each['people_id'])
        voteList.append((eachPerson['role'], eachPerson['name'], each['vote_text']))
    return voteList
