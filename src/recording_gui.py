from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font as tkFont

class main_window:
    def __init__(self, master):
        self.master = master
        master.title("Attendance Recorder")
        self.bigfont = tkFont.Font(family="Helvetica",size=20)
        master.option_add("*Font", self.bigfont)

        #Making fields for the boxes: Names, months, and days
        self.names = ["fads", "fasdfa"]
        #Creating frames, one for names and dates
        self.namesFrame = Frame(master)
        self.namesFrame.pack()
        self.datesFrame = Frame(master)
        self.datesFrame.pack(side=BOTTOM)

        #Creating labels for instructions when app opens
        self.topLabel = Label(self.namesFrame, text="1) Choose a name")
        self.topLabel.pack()
        self.botLabel = Label(self.datesFrame, text="2) Enter a date")
        self.botLabel.pack()

        #Making a Combobox for names names
        self.names_box = Combobox(self.namesFrame, values=self.names, width=30)
        self.names_box.set("names")
        self.names_box.pack(side=LEFT)
        #Entry for Months
        self.months_box = Entry(self.datesFrame, bg="white", fg="black", width=10)
        self.months_box.insert(END,"month")
        self.months_box.pack(side=LEFT)
        #Entry for Days
        self.days_box = Entry(self.datesFrame, bg="white", fg="black", width=10)
        self.days_box.insert(END,"day")
        self.days_box.pack(side=LEFT)

        #Making a button to record the names and dates
        self.record_button = Button(self.datesFrame, text="Record name", command=self.print_selected).pack(side=BOTTOM)
        self.master.bind("<Return>", self.print_selected)

        self.master.geometry("540x200")

    def print_selected(event=None):
        value = names_box.get() + " " + months_box.get() + " " + days_box.get()
        print(value)



if __name__ == "__main__":
    root = Tk()
    wind = main_window(root)
    root.mainloop()
