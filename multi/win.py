import tkinter as tk


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400")
        self.master.title(" Master")
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label_one = tk.Label(text="Click to open new window", bg="#B0C4DE")
        self.label_one.pack()


class Win1:

    def __init__(self, master, text_one):
        self.master = master
        self.master.geometry("300x400")
        self.master.title("Window")
        self.frame1 = tk.Frame(master)
        self.frame1.pack()
        self.label_two = tk.Label(master, text=text_one, bg="#FFC0CB")
        self.label_two.pack()


root = tk.Tk()
app = GUI(root)

win1 = tk.Toplevel(root)
app1 = Win1(win1,"First window")

win2 = tk.Toplevel(root)
app2 = Win1(win2,"Second window")

win3 = tk.Toplevel(root)
app3 = Win1(win3,"Third window")

root.mainloop()
