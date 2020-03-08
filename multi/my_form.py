import tkinter as tk
from tkinter.messagebox import showinfo

class MyGui(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack()
        button = tk.Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')

class MyWin(MyGui):
    def __init__(self):
        MyGui.__init__(self)
        lbl = tk.Label(self, text="Hello").pack()

root=tk.Tk()
mygui= MyGui(root)
mywin= MyWin()

root.mainloop()
