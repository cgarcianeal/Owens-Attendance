import csv
import sys
from datetime import date

def needs_memo(name, date, days_used):
    if days_used == 3:
        print(name + " needs 3 PB memo")
        disciplinary_action_list.append(name + " needs 3 PB memo")
    elif days_used == 4:
        print(name + " needs 4 pb need")
        disciplinary_action_list.append(name + " needs 4 pb need")
    else:
        print(name + " wrong memo")
        disciplinary_action_list.append(name + " wrong memo")

def needs_writeup(name, date, days_used, reason):
    if reason == "1st NCNS":
        print(name + " 1st ncns writeup")
        disciplinary_action_list.append(name + " 1st ncns writeup")
    elif reason == "2nd NCNS":
        print(name + " 2nd ncns writeup")
        disciplinary_action_list.append(name + " 2nd ncns writeup")
    elif days_used >= 5:
        print(name + " " + str(int(days_used)) + " PB writeup")
        disciplinary_action_list.append(name + " " + str(int(days_used)) + " PB writeup")

def needs_termination(name, date, days_used, reason):
    if days_used >= 6:
        print(name + " terminated for > 6 PB")
        disciplinary_action_list.append(name + " terminated for > 6 PB")
    else:
        print(name + " terminated for 2 ncns")
        disciplinary_action_list.append(name + " terminated for 2 ncns")



#Getting the data (Name, reason) from the record file into a list (recordList)
today = str(date.today())
try:
    record_file_name = "record_" + today + ".csv"
    record = open (record_file_name, "r")

    recR = csv.reader(record)
    recordList = list(recR)

except IOError:
    print(record_file_name + " not found. Please check name and try again.")
    sys.exit()

#Opening the attendance file for editing
#fname = input("What is the name of the attendance file?\n")
#for testing file always owens_test.csv
fname = "owens_test.csv"
try:
    att = open(fname, 'rt')
    attR = csv.reader(att)
    attList = list(attR)
    names_raw = []
    disciplinary_action_list = []

    for row in attList:
        if "," in row[0]:
            names_raw.append(row[0])

    # Loop through the records (rec) and edit the attendance (att)
    # records are in edits [row][column]
    # First locate name in list to get row

    # Info for the attendance csv file
    # column 0 is the names (edits [nameIndex] [0])
    # column 5 is the date of the absense of  (edits [nameIndex] [4])
    # column 6 is the number of absences (edits [nameIndex] [5])
    for row in recordList:
        name = row[0]
        reason = row[1]
        date = row[2]

        print("\nLooking at: " + name)
        if name in names_raw:
            print("Found in file", name, reason, date, sep=" : ")
            nameIndex = names_raw.index(name) + 2 # row = name index + 2 (adjusting for header offset)

            #Different edits based on the reason
            if reason == "PB" or reason == "NCNS":
                print("Previous num: " + attList[nameIndex][6])
                if attList[nameIndex][6] == "":
                    attList[nameIndex][6] = "0"
                attList[nameIndex][6] = str(float(attList[nameIndex][6]) + 1)
                attList[nameIndex][5] = attList[nameIndex][5] + "\n" + date  + " : " + reason
                updated_days_used = float(attList[nameIndex][6])
                att_notes = attList[nameIndex][5]
                print("Updated num: " + attList[nameIndex][6])

                #need memo for 1 pb left or 0 pb left
                if updated_days_used == 3 or updated_days_used == 4:
                    #need_memo
                    needs_memo(name, date, updated_days_used)

                if reason == "PB":
                    if updated_days_used >= 5:
                        #need_writeup
                        needs_writeup(name, date, updated_days_used, reason)
                        if updated_days_used >= 6:
                            #need_termination
                            needs_termination(name, date, updated_days_used, reason)

                if reason == "NCNS":
                    if att_notes.count("NCNS") == 1:
                        needs_writeup(name, date, updated_days_used, "1st NCNS")
                    elif att_notes.count("NCNS") >= 2:
                        needs_writeup(name, date, updated_days_used, "2nd NCNS")
                        needs_termination(name, date, updated_days_used, "2nd NCNS")

    #endfor

    outfile_name = 'owens_test_' + today + '.csv'
    writeAtt = open(outfile_name, 'w', newline='')
    writer = csv.writer(writeAtt)
    writer.writerows(attList)

    print("\nResults output to " + outfile_name)

    for elem in disciplinary_action_list:
        print(elem)


except IOError:
    print("File not found. Please check name and try again.")
    sys.exit()
