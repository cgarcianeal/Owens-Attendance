import csv
from datetime import date

#Getting the data (Name, reason) from the record file into a list (recordList)
today = str(date.today())
record_file_name = "record_" + today + ".csv"
record = open (record_file_name, "r")
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
        names_raw.append(row[0].lower())

    # Loop through the records (rec) and edit the attendance (att)
    # records are in edits [row][column]
    # First locate name in list to get row

    # Info for the attendance csv file
    # column 0 is the names (edits [nameIndex] [0])
    # column 4 is the date of the absense of  (edits [nameIndex] [4])
    # column 5 is the number of absences (edits [nameIndex] [5])
    for row in recordList:
        name = row[0]
        reason = row[1]
        date = row[2]

        print(name)
        if name.lower() in names_raw:
            print(name + "\n" + reason)
            nameIndex = names_raw.index(name) # row = name index
            #Different edits based on the reason
            if reason == "PB" or reason == "NCNS":
                print(attList[nameIndex][5])
                attList[nameIndex][5] = str(float(attList[nameIndex][5]) + 1)
                attList[nameIndex][4] = attList[nameIndex][4] + "\n" + date  + " : " + reason
                print(attList[nameIndex][5])
    #endfor

    outfile_name = 'owens_test_' + today + '.csv'
    writeAtt = open(outfile_name, 'w', newline='')
    writer = csv.writer(writeAtt)
    writer.writerows(attList)

except IOError:
    print("File not found. Please check name and try again.")
