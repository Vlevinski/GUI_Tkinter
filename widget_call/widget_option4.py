from tkinter import *
root= Tk()
options = {'text': 'Hello GUI world!'}
layout = {'side': 'top'}
Label(root, **options).pack()
mainloop()
