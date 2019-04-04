from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter.font as tkFont
import datetime
from datetime import date
from tkinter import filedialog
import csv
import os
import shutil

today = str(date.today())
folder_name = today + "_attendance"

class att_gui:
    def __init__(self, master, names_list):
        def print_selected(event=None):
            value = self.names_box.get() + " " + self.months_box.get() + " " + self.days_box.get() + " : " + self.reason_box.get()
            year = datetime.date.today().year
            date = datetime.datetime(int(year), int(self.months_box.get()), int(self.days_box.get()))

            # Writing data to make a line in csv file
            # Format: "LastName, FirstName",Reason
            record.write("\"" + self.names_box.get() + "\"" + "," +
                         self.reason_box.get() + "," +
                         date.strftime("%m/%d/%y") + "\n"
                         )
            print(value)

        def on_closing():
            if messagebox.askokcancel("Quit", "Are you finished recording names?"):
                record.close()
                root.destroy()

        #Open output file
        file_name = folder_name + "/record_" + today + ".csv"
        #opening records csv file for writing
        record = open (file_name, "w")

        #TODO: Setting the icon

        self.master = master
        master.title("Attendance Recorder")
        self.bigfont = tkFont.Font(family="Helvetica",size=20)
        master.option_add("*Font", self.bigfont)

        #Making fields for the boxes: Names, months, and days
        self.names = names_list
        #Creating frames, one for names and dates
        self.namesFrame = Frame(master)
        self.namesFrame.pack()
        self.datesFrame = Frame(master)
        self.datesFrame.pack(side=BOTTOM)

        #1) Creating a label and combobox for the student names
        self.topLabel = Label(self.namesFrame, text="1) Choose a name", fg='white')
        self.topLabel.pack()

        self.names_box = Combobox(self.namesFrame, values=self.names, width=30)
        self.names_box.set("names")
        self.names_box.pack()

        #2) Creating a label and combobox for the reason
        self.midLabel = Label(self.namesFrame, text="2) Reason", fg='white')
        self.midLabel.pack()

        self.reasons = ["PB", "NCNS"]
        self.reason_box = Combobox(self.namesFrame, values=self.reasons, width=20)
        self.reason_box.set("reason")
        self.reason_box.pack(side=BOTTOM)

        #3) Creating a label and comboboxes for the dates
        #Entry for
        self.botLabel = Label(self.datesFrame, text="3) Enter a date", fg='white')
        self.botLabel.pack()
        self.months_box = Entry(self.datesFrame, bg="white", fg="black", width=10)
        self.months_box.insert(END,"month")
        self.months_box.pack(side=LEFT)
        #Entry for Days
        self.days_box = Entry(self.datesFrame, bg="white", fg="black", width=10)
        self.days_box.insert(END,"day")
        self.days_box.pack(side=LEFT)

        #Making a button to record the names and dates
        self.record_button = Button(self.datesFrame, text="Record name", command=print_selected, fg='white').pack(side=BOTTOM)
        self.master.bind("<Return>", print_selected)
        self.master.bind("<KP_Enter>", print_selected)
        self.master.protocol("WM_DELETE_WINDOW", on_closing)


if __name__ == "__main__":
    #Making the root Tk object
    root = Tk()
    #Setting the default font color to be black
    root.option_add('*foreground', 'black')  # set all tk widgets' foreground to black
    root.option_add('*activeForeground', 'black')  # set all tk widgets' foreground to black
    #Used to make it so that the filedialog and other window show above other windows
    root.lift()
    #Opening main window in the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("550x250+%d+%d" % (screen_width/2-275, screen_height/2-125))

    #This makes a new folder for the attendance of that day
    folder_name = today + "_attendance"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    #Opening a file dialog so the use can select the attendance file to use for the names
    root.filename =  filedialog.askopenfilename(initialdir = "~/Downloads/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    #Using the file to load the names so be used as options on the new recording session
    att = open(root.filename, 'rt')
    attR = csv.reader(att)
    attList = list(attR)
    names_raw = []
    #elimination non-names
    for row in attList:
        if "," in row[0]:
            names_raw.append(row[0])
    att.close()
    #Copying input file to be updated to folder for this day, and renaming to appropriate date
    shutil.move(root.filename, folder_name + "/owens_in_" + today +".csv")

    wind = att_gui(root, names_raw)
    root.mainloop()
