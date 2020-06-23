import get_sessions
import get_session
import get_bill
import get_votes
import get_person


class main:
    def __init__(self):
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
        print("Bill ID ", " Bill Title")
        for each in self.currentSession:
            print(each)

        billSelect = input("Select a bill: ")
        nextBill = get_bill.getBill(billSelect)
        print(nextBill.getTitle())
        self.billDetail(nextBill)

    def billDetail(self, currentBill):
        print("What would you like to know about the bill? ")
        billDetail = input("""1. History
2. Sponsors
3. Votes
4. Document ID
5. Go Back""")
        try:
            if int(billDetail) == 1:
                list_a = currentBill.getHistory()
                print("History: ")
                for each in list_a:
                    print(each)
                self.billDetail(currentBill)
            elif int(billDetail) == 2:
                list_a = currentBill.getSponsors()
                print("Sponsors: ")
                for each in list_a:
                    print(each)
                self.billDetail(currentBill)
            elif int(billDetail) == 3:
                list_a = currentBill.getVotes()
                print("Votes: ")
                for each in list_a:
                    print(each)
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