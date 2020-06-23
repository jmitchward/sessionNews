import requests
import json


class getBill:
    def __init__(self, billID):
        getRequest = requests.get("https://api.legiscan.com/?key=37171dfe48f4ed320021de67197e3217&op=getBill&id=" + str(billID))
        convertResponse = json.loads(getRequest.text)
        self.currentBill = convertResponse['bill']

    def getTitle(self):
        return self.currentBill['title']

    def getHistory(self):
        historyList = list()
        for each in self.currentBill['history']:
            historyList.append((each['date'], each['chamber'], each['action']))
            return historyList

    def getSponsors(self):
        sponsorList = list()
        for each in self.currentBill['sponsors']:
            sponsorList.append((each['people_id'], each['party'], each['first_name'] + ' ' + each['last_name']))
        return sponsorList

    def getVotes(self):
        voteList = list()
        for each in self.currentBill['votes']:
            voteList.append((each['roll_call_id'],each['date'],each['yea'],each['nay'],each['nv'],each['absent'],each['total'],
                             each['passed'],each['chamber']))
        return voteList

    def getDocID(self):
        for each in self.currentBill['texts']:
            return each['doc_id']


