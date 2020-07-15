import get_session
import get_bill
import get_votes
import get_person
import foundation
import logging
import time
import sys


class main(foundation.construct):
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s)')
        super(main, self).__init__()
        print("Welcome. Here are the bills for the most recent session in Kentucky.")
        self.currentSession = get_session.getSession("KY")

        self.billSort()

    def billSort(self):
        for each in self.currentSession:
            if 'sj' in each[1][:2].lower():
                # Senate Joint Resolution
                self.senateJoint.append(each)
            elif 'hj' in each[1][:2].lower():
                self.houseJoint.append(each)
            elif 'sr' in each[1][:2].lower():
                # Senate Resolution
                self.senateRes.append(each)
            elif 'hr' in each[1][:2].lower():
                # House Resolution
                self.houseRes.append(each)
            elif 'hb' in each[1][:2].lower():
                # House Bill
                self.houseBill.append(each)
            elif 'sb' in each[1][:2].lower():
                # Senate Bill
                self.senateBill.append(each)
            elif 'hc' in each[1][:2].lower():
                # House Concurrent Resolution
                self.houseCon.append(each)
            elif 'sc' in each[1][:2].lower():
                # Senate Concurrent Resolution
                self.senateCon.append(each)

        self.houseDict['joint'] = self.houseJoint
        self.houseDict['resolutions'] = self.houseRes
        self.houseDict['bills'] = self.houseBill
        self.houseDict['concurrent'] = self.houseCon

        self.senateDict['joint'] = self.senateJoint
        self.senateDict['resolutions'] = self.senateRes
        self.senateDict['bills'] = self.senateBill
        self.senateDict['concurrent'] = self.senateCon

        self.billDict['house'] = self.houseDict
        self.billDict['senate'] = self.senateDict

        self.chamberSelect()

    def chamberSelect(self):
        self.chamber = input("House or Senate? ")
        if self.chamber.lower() == "exit":
            sys.exit("Thank you.")
        self.chamberBills = input('Bills, Joint, Resolutions, Concurrent?')
        try:
            self.currentSelection = self.billDict[self.chamber.lower()][self.chamberBills.lower()]
        except ValueError:
            print("Please enter a valid format.")
            self.chamberSelect()
        except KeyError:
            print("Please enter a valid format.")
            self.chamberSelect()
        self.billSelect()

    def billSelect(self):
        for each in self.currentSelection:
            print(each[1], "|", each[2])
        billSelect = input("Select a bill or enter back: ")
        if billSelect.lower() == 'back':
            self.chamberSelect()
        for bills in self.currentSelection:
            if bills[1].lower() == billSelect.lower():
                thisBill = bills[0]
        try:
            nextBill = get_bill.getBill(thisBill)
        except UnboundLocalError:
            print("Invalid Bill ID.")
            time.sleep(2)
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
            print("Name:", each[0], each[1])
            print("Vote:", each[2])

    def billDetail(self, currentBill):
        print("What would you like to know about the bill? ")
        print("1. Path")
        print("2. Sponsors")
        print("3. Votes")
        print("4. Document ID")
        print("5. Go Back")

        billDetail = input("Select: ")

        try:
            if int(billDetail) == 1:
                list_a = currentBill.getHistory()
                print("Last action for this bill: ")
                for each in list_a:
                    print(each)
                self.billDetail(currentBill)

            elif int(billDetail) == 2:
                list_b = currentBill.getSponsors()
                print("Sponsors: ")
                for each in list_b:
                    self.sponsorsID = each[0]
                    print(each)
                moreDetail = input("Would you like to know more about a sponsor?")
                if moreDetail.lower() == 'yes':
                    if len(list_b) == 1:
                        self.sponsorSelect(each[0])
                    else:
                        getSponsor = input("Please enter the Sponsor ID: ")
                        self.sponsorSelect(getSponsor)
                self.billDetail(currentBill)

            elif int(billDetail) == 3:
                list_c = currentBill.getVotes()
                if not list_c:
                    print("Votes on this bill: ")
                    print("This bill was not voted on.")
                else:
                    print("Votes on this bill: ")
                    for each in list_c:
                        print("Vote ID: ", each[0])
                        print("Date: ", each[1], " Chamber: ", each[8])
                        print("Yay Votes: ", each[2], " Nay Votes: ", each[3])
                        print("No Vote: ", each[4], " Absent: ", each[5])
                        print("Total Votes: ", each[6])
                        if int(each[7]) == 1:
                            print("This bill passed.")
                        else:
                            print("This bill did not pass.")
                    moreDetail = input("Would you like to know more about a vote?")
                    if moreDetail.lower() == "yes":
                        getVote = input("Please enter the Vote ID: ")
                        self.voteSelect(getVote)
                self.billDetail(currentBill)

            elif int(billDetail) == 4:
                list_d = currentBill.getDocID()
                print("Document ID: ")
                print(list_d)
                self.billDetail(currentBill)
            else:
                self.billSelect()

        except ValueError:
            print("Please enter the number selection.")
            self.billDetail(currentBill)


main()
