import tkinter as tk
from tkinter.messagebox import showinfo

class MyGui(tk.Tk):
    def __init__(self, parent=None):
        tk.Tk.__init__(self, parent)
        self.geometry= "500x300"
        self.title = "Main"

        # data
        self.txt1 = "Welcome Back !\n"
        self.txt2 = "To keep connected with us please login \n with your personal info"

        # frames
        frm1 = tk.Frame(self, bg="blue")
        frm2 = tk.Frame(self, bg="white")
        topl = tk.Frame(frm1, bg="brown1")
        botl = tk.Frame(frm1, bg="brown1")

        # frames packs
        frm1.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        frm2.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        topl.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        botl.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)

        # left
        lbl1 = tk.Label(topl, text=self.txt1, font=('helvetica', 15, 'bold'), fg="white", bg="brown1").pack(side=tk.BOTTOM)
        lbl2 = tk.Label(botl, text=self.txt2, fg="white", bg="brown1").pack()

        # buttons
        btn1 = tk.Button(botl, text="SIGN IN", fg="brown1", bg="white", command=lambda: self.reply()).pack(expand=tk.YES)
        btn2 = tk.Button(frm2, text="SIGN UP", command=lambda: self.reply()).pack(expand=tk.YES)


    def reply(self):
        showinfo(title='popup', message='Button pressed!')

class MyWin(MyGui):
    def __init__(self):
        MyGui.__init__(self)
        lbl = tk.Label(self, text="Hello").pack()


mygui= MyGui().mainloop()
