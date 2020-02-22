import tkinter as tk


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400")
        self.master.title(" Master")
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label_one = tk.Label(text="Click to open new window")
        self.label_one.pack()


class Win1:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400")
        self.master.title("Window")


root = tk.Tk()
app = GUI(root)
root.mainloop()
