from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font as tkFont

def print_selected(event=None):
    value = names_box.get() + " " + months_box.get() + " " + days_box.get()
    print(value)

root = Tk()
root.title("Attendance Recorder")
bigfont = tkFont.Font(family="Helvetica",size=20)
root.option_add("*Font", bigfont)

#Making fields for the boxes: Names, months, and days
names = ["student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three", "student one", "student two", "student three"]

#Creating frames, one for names and dates
namesFrame = Frame(root)
namesFrame.pack()
datesFrame = Frame(root)
datesFrame.pack(side=BOTTOM)

#Creating labels for instructions when app opens
topLabel = Label(namesFrame, text="1) Choose a name")
topLabel.pack()
botLabel = Label(datesFrame, text="2) Enter a date")
botLabel.pack()

#Making a Combobox for names names
names_box = Combobox(namesFrame, values=names, width=30)
names_box.set("names")
names_box.pack(side=LEFT)
#Entry for Months
months_box = Entry(datesFrame, bg="white", fg="black", width=10)
months_box.insert(END,"month")
months_box.pack(side=LEFT)
#Entry for Days
days_box = Entry(datesFrame, bg="white", fg="black", width=10)
days_box.insert(END,"day")
days_box.pack(side=LEFT)

#Making a button to record the names and dates
button = Button(datesFrame, text="Record name", command=print_selected).pack(side=BOTTOM)
root.bind("<Return>", print_selected)

root.geometry("540x200")
root.mainloop()
