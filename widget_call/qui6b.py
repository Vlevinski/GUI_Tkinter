from sys import exit
from tkinter import *
from widget_call.gui6 import Hello

parent = Frame(None)
parent.pack()
Hello(parent).pack(side=RIGHT)
# get Tk widget classes
# get the subframe class
# make a container widget
# attach Hello instead of running it
Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
