from tkinter import *
from widget_call.gui7 import HelloPackage
# or get from gui7c--__getattr__ added

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()
part = HelloPackage(frm)
part.pack(side=RIGHT)
frm.mainloop()
