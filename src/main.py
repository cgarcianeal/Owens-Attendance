import csv
import os
import sys
import pathlib
from datetime import date

class dis_action:
    def __init__(self, name, date, offense):
        self.name = name
        self.date = date
        self.offense = offense

    def __lt__(self, other):
        return self.offense < other.offense

    def print_formated(self):
        return self.name + " " + self.date

def needs_memo(name, date, days_used):
    if days_used == 3:
        print(name + " needs 3 PB memo")
        disciplinary_action_list.append(dis_action(name, date, "3 PB"))
    elif days_used == 4:
        print(name + " needs 4 PB need")
        disciplinary_action_list.append(dis_action(name, date, "4 PB"))
    else:
        print(name + " wrong memo")

def needs_writeup(name, date, days_used, reason):
    if reason == "1st NCNS":
        print(name + " 1st ncns writeup")
        disciplinary_action_list.append(dis_action(name, date, "1st NCNS"))
    elif reason == "2nd NCNS":
        print(name + " 2nd ncns writeup")
        disciplinary_action_list.append(dis_action(name, date, "2nd NCNS"))

    if days_used >= 5:
        print(name + " " + str(int(days_used)) + " PB writeup")
        disciplinary_action_list.append(dis_action(name, date, str(int(days_used)) + " PB"))

def needs_termination(name, date, days_used, reason):
    if days_used >= 6:
        print(name + " terminated for > 6 PB")
        disciplinary_action_list.append(dis_action(name, date, "Terminate: 6 PB"))
    else:
        print(name + " terminated for 2 ncns")
        disciplinary_action_list.append(dis_action(name, date, "Terminate: 2 NCNS"))

#Getting the data (Name, reason) from the record file into a list (recordList)
today = str(date.today())

#Setting directory name for output
folder_name = today + "_attendance"

try:
    record_file_name = folder_name + "/record_" + today + ".csv"
    #record_file_name = "record_2019-04-03.csv"
    record = open (record_file_name, "r")

    recR = csv.reader(record)
    recordList = list(recR)

except IOError:
    print(record_file_name + " not found. Please check name and try again.")
    sys.exit(1)

#Attendance files to be updated
fname = folder_name + "/owens_in_" + today +".csv"

try:
    att = open(fname, 'rt')
    attR = csv.reader(att)
    attList = list(attR)
    names_raw = []
    disciplinary_action_list = []

    #Going through the csv to get a list of names to use for easy searching
    name_count = 0
    for row in attList:
        name_count+=1
        if "," in row[0]:
            names_raw.append(row[0])
        elif name_count > 2:
            print(row)
            print("Comma not detected seperating first and last name for \"" + row[0] + "\". Please the name has the" +
                  " proper format: \"lastname, firstname\"")
            sys.exit(1)

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
                prev_days_used = float(attList[nameIndex][6])
                updated_days_used = float(attList[nameIndex][6]) + 1
                attList[nameIndex][6] = str(updated_days_used)
                attList[nameIndex][5] = attList[nameIndex][5] + "\n" + date  + " : " + reason
                att_notes = attList[nameIndex][5]
                print("Updated num: " + attList[nameIndex][6])

                #need memo for 1 pb left or 0 pb left
                if updated_days_used == 3 or updated_days_used == 4:
                    #need_memo
                    needs_memo(name, date, updated_days_used)

                if reason == "PB":
                    if updated_days_used >= 6:
                        #need_termination
                        needs_termination(name, date, updated_days_used, reason)
                    if updated_days_used >= 5:
                        #need_writeup
                        needs_writeup(name, date, updated_days_used, reason)

                if reason == "NCNS":
                    if att_notes.count("NCNS") == 1:
                        needs_writeup(name, date, updated_days_used, "1st NCNS")
                    elif att_notes.count("NCNS") >= 2:
                        needs_writeup(name, date, updated_days_used, "2nd NCNS")
                        needs_termination(name, date, updated_days_used, "2nd NCNS")

    #endfor

    #Outputting updated attendance file to be reuploaded to canvas
    outfile_name = folder_name + '/owens_out_' + today + '.csv'
    writeAtt = open(outfile_name, 'w', newline='')
    writer = csv.writer(writeAtt)
    writer.writerows(attList)
    writeAtt.close()
    print("\nUpdated output to " + outfile_name)

    #Outputting the summary text file of all memos/write ups/terminations
    summary_outfile_name = folder_name + '/owens_summary_' + today + '.txt'
    summary_outfile = open(summary_outfile_name, 'w', newline='')
    summary_outfile.write("Attendance done through: " + today +  "\n")

    disciplinary_action_list.sort()
    last_offense = ""
    for elem in disciplinary_action_list:
        if elem.offense != last_offense:
            #print("\n" + elem.offense + "\n")
            summary_outfile.write("\n" + elem.offense + "\n\n")
            last_offense = elem.offense
        #print(elem.print_formated())
        summary_outfile.write(elem.print_formated() + "\n")


except IOError:
    print("File not found. Please check name and try again.")
    sys.exit()
