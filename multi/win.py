import tkinter as tk


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400")
        self.master.title(" Master")
        self.frame = tk.Frame(master)
        self.frame.pack()


root = tk.Tk()
app = GUI(root)
root.mainloop()
