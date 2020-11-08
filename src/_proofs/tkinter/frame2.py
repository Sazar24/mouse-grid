# https://www.daniweb.com/programming/software-development/threads/243146/tkinter-entry-widget-border-color
from tkinter import *
master = Tk()
# nameentryframe = Frame(master, background='BLACK', borderwidth=14, relief=SUNKEN)
nameentryframe = Frame(master, background='BLACK', borderwidth=14)
nameentry = Entry(nameentryframe)
nameentryframe.pack()
nameentry.pack()
master.mainloop()
