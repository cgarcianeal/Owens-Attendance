import csv
import sys
import datetime
from datetime import date

more = 'y' # Settingfactor for while loop
today = str(date.today())
year = datetime.date.today().year
default_option = "current"
prev_month = 0
prev_day = 0

file_name = "record_" + today + ".csv"
#opening records csv file for writing
record = open (file_name, "w")

# Recording Loop
while more == 'y':
    first_name = input("What's the students first name? ")
    last_name = input("What's the students last name? ")

    if first_name == "" or last_name =="":
        sys.exit("Please enter a first and last name")

    #Just press Enter to have it be a PB
    reason = input("Reason (Default=PB): ")
    if reason == "":
        reason = "PB"

    #Now getting the date of the absence: year, month, day
    month = input("Month? (Default=" + default_option + "): ")
    if month == "":
        if default_option == "current":
            month = datetime.date.today().month
        else:
            month = prev_month

    day = input("Day? (Default=" + default_option + "): ")
    if day == "":
        if default_option == "current":
            day = datetime.date.today().day
        else:
            day = prev_day

    date = datetime.datetime(int(year), int(month), int(day))

    # Writing data to make a line in csv file
    # Format: "LastName, FirstName",Reason
    record.write("\"" + last_name + ", " + first_name + "\"" + "," +
                reason + "," +
                date.strftime("%m/%d/%y"))

    more = input("More? (default=yes, no = n): ")
    if more == "":
        more = 'y'

    # add new line if there are more entries
    if more == 'y':
        default_option = "previous"
        prev_month = month
        prev_day = day
        print("")
        record.write("\n")
