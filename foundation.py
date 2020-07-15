import get_sessions


class construct:
    def __init__(self):
        self.rollcallID = list()
        self.billDict = dict()
        self.senateDict = dict()
        self.houseDict = dict()
        self.sponsorsID = list()
        self.senateJoint = list()
        self.houseJoint = list()
        self.houseRes = list()
        self.senateRes = list()
        self.houseBill = list()
        self.senateBill = list()
        self.houseCon = list()
        self.senateCon = list()
        self.currentSelection = list()
        self.chamber = ""
        self.chamberBills = ""

        #    print("Welcome. Here are the 5 most recent sessions currently available.")
        #
        #    sessionList = get_sessions.getSessions()
        #    print("Session ID ", " Session Name")
        #    for each in sessionList[:5]:
        #        print(each)

        #    sessionSelect = input("Select a session: ")
