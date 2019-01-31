import csv
from datetime import date

# Initializing the date of edits
today = str(date.today())

#Getting the data (Name, reason) from the record file into a list (recordList)
record = open ("record.csv", "r")
recR = csv.reader(record)
recordList = list(recR)

#Opening the attendance file for editing
fname = input("What is the name of the attendance file?\n")
try:
    att = open(fname, 'rt')
    attR = csv.reader(att)
    attList = list(attR)
    names_raw = []

    for row in attList:
        names_raw.append(row[0])

    # Loop through the records (rec) and edit the attendance (att)
    # records are in edits [row][column]
    # First locate name in list to get row
    # column 0 is the names (edits [nameIndex] [0])
    # column 5 is the attendance of PBs (edits [nameIndex] [5])
    for row in recordList:
        name = row[0]
        reason = row[1]
        if name in names_raw:
            print(name + "\n" + reason)
            nameIndex = names_raw.index(name) # row = name index
            #Different edits based on the reason
            if reason == "PB" or reason == "NCNS":
                print(attList[nameIndex][5])
                attList[nameIndex][5] = str(float(attList[nameIndex][5]) + 1)
                print(attList[nameIndex][5])

    writeAtt = open('owens_test_out.csv', 'w', newline='')
    writer = csv.writer(writeAtt)
    writer.writerows(attList)

except IOError:
    print("File not found. Please check name and try again.")