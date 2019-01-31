import csv
import sys
import datetime

more = 'y' # Settingfactor for while loop
record = open ("record.csv", "w") #opening records csv file for writing. Will erase the old csv everytime

# Recording Loop
while more == 'y':
    first_name = input("What's the students first name? ")
    last_name = input("What's the students last name? ")

    if first_name == "" or last_name =="":
        sys.exit("Please enter a first and last name")

    reason = input("Reason (Default=PB): ")
    #Just press Enter to have it be a PB
    if reason == "":
        reason = "PB"

    #Now getting the date of the absence: year, month, day
    year = input("Year? (Default=currrent): ")
    if year == "":
        year = datetime.date.today().year

    month = input("Month? (Default=current): ")
    if month == "": 
        month = datetime.date.today().month

    day = input("Day? (Default=current): ")
    if day == "":
        day = datetime.date.today().day

    date = datetime.datetime(int(year), int(month), int(day))

    # Writing the name to the csv file. Name must be in quotations to be in one cell
    # Format: "LastName, FirstName",Reason
    record.write("\"" + last_name + ", " + first_name + "\"" + "," + 
                reason + "," +
                date.strftime("%m/%d/%y"))

    more = input("More? (default=yes, no = n): ")

    if more == "":
        more = 'y'
    # add new line if there are more entries
    if more == 'y':
        print("")
        record.write("\n")