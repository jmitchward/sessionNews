import get_sessions
import get_session
import get_bill
import get_votes
import get_person


class main:
    def __init__(self):
        self.rollcallID = list()
        self.sponsorsID = list()
        #    print("Welcome. Here are the 5 most recent sessions currently available.")
        #
        #    sessionList = get_sessions.getSessions()
        #    print("Session ID ", " Session Name")
        #    for each in sessionList[:5]:
        #        print(each)

        #    sessionSelect = input("Select a session: ")

        print("Welcome. Here are the bills for the most recent session in Kentucky.")
        self.currentSession = get_session.getSession("KY")

        self.billSelect()

    def billSelect(self):
        print("Bill Number", "|", " Bill Title")
        for each in self.currentSession:
            print(each[1], "|", each[2])
        billSelect = input("Select a bill: ")
        for bills in self.currentSession:
            if bills[1].lower() == billSelect.lower():
                thisBill = bills[0]
        try:
            nextBill = get_bill.getBill(thisBill)
        except UnboundLocalError:
            print("Invalid Bill ID.")
            self.billSelect()
        print("Bill Description")
        print(nextBill.getTitle())
        self.billDetail(nextBill)

    def sponsorSelect(self, sponsorID):
        print("Bill Sponsor:")
        sponsorInfo = get_person.getPerson(sponsorID)
        if sponsorInfo is None:
            newID = input("Please enter a valid Sponsor ID: ")
            self.sponsorSelect(newID)
        else:
            print(sponsorInfo['role'], sponsorInfo['name'])
            print("District: ", sponsorInfo['district'])
            print("Party: ", sponsorInfo['party'])

    def voteSelect(self, voteID):
        print("Roll Call for this vote")
        voteInfo = get_votes.getVotes(voteID)
        for each in voteInfo:
            print("Person ID: ", each[0])
            print(each[1])

    def billDetail(self, currentBill):
        print("What would you like to know about the bill? ")
        billDetail = input("""1. Path
2. Sponsors
3. Votes
4. Document ID
5. Go Back
Select: """)
        try:
            if int(billDetail) == 1:
                list_a = currentBill.getHistory()
                print("Last action for this bill: ")
                for each in list_a:
                    print(each)
                self.billDetail(currentBill)

            elif int(billDetail) == 2:
                list_a = currentBill.getSponsors()
                print("Sponsors: ")
                for each in list_a:
                    self.sponsorsID = each[0]
                    print(each)
                moreDetail = input("Would you like to know more about a sponsor?")
                if moreDetail.lower() == 'yes':
                    if len(list_a) == 1:
                        self.sponsorSelect(list_a[0])
                    else:
                        getSponsor = input("Please enter the Sponsor ID: ")
                        self.sponsorSelect(getSponsor)
                self.billDetail(currentBill)

            elif int(billDetail) == 3:
                list_a = currentBill.getVotes()
                if not list_a:
                    print("Votes on this bill: ")
                    print("This bill was not voted on.")
                else:
                    print("Votes on this bill: ")
                    for each in list_a:
                        print("Vote ID: ",  each[0])
                        print("Date: ", each[1], " Chamber: ", each[8])
                        print("Yay Votes: ", each[2], " Nay Votes: ", each[3])
                        print("No Vote: ", each[4], " Absent: ", each[5])
                        print("Total Votes: ", each[6])
                        if int(each[7]) == 1:
                            print("This bill passed.")
                        else:
                            print("This bill did not pass.")
                    moreDetail = input("Would you like to know more about a vote? ")
                    if moreDetail.lower == "yes":
                        getVote = input("Please enter the Vote ID: ")
                        self.voteSelect(getVote)
                self.billDetail(currentBill)

            elif int(billDetail) == 4:
                list_a = currentBill.getDocID()
                print("Document ID: ")
                print(list_a)
                self.billDetail(currentBill)
            else:
                self.billSelect()

        except ValueError:
            print("Please enter the number selection.")
            self.billDetail(currentBill)


main()
