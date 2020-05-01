import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')

def quit(event):
    print('Hello, I must be going...')
    sys.exit()

# event gives widget, x/y, etc.
widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)        # bind left mouse clicks
widget.bind('<Double-1>', quit)         # bind double-left clicks
widget.bind('<Button-2>', hello)        # bind left mouse clicks
widget.bind('<Double-2>', quit)         # bind double-left clicks
widget.bind('<Button-3>', hello)        # bind left mouse clicks
widget.bind('<Double-3>', quit)         # bind double-left clicks
widget.mainloop()
