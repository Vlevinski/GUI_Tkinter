import tkinter as tk


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400+200+200")
        self.master.resizable(150, 150)
        self.master.title(" Master")
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label_one = tk.Label(text="Main window", bg="#B0C4DE")
        self.label_one.pack()


class Win1:

    def __init__(self, master, text_one):
        self.master = master
        self.master.geometry("300x400")
        self.master.overrideredirect(0)
        self.master.resizable(10, 10)
        self.master.title("Window")
        self.frame1 = tk.Frame(master)
        self.frame1.pack()
        self.label_two = tk.Label(master, text=text_one, bg="#FFC0CB")
        self.label_two.pack()
        #        tk.Label(master, text="Press <ESC> to exit").pack()
        #        master.bind("<Escape>", exit)
        self.quit = tk.Button(self.master, text="Quit", command=self.close_window)
        self.quit.pack()

    def close_window(self):
        self.master.destroy()


root = tk.Tk()
app = GUI(root)

win1 = tk.Toplevel(root)
app1 = Win1(win1, "First window")


win2 = tk.Toplevel(root)
app2 = Win1(win2, "Second window")

win3 = tk.Toplevel(root)
app3 = Win1(win3, "Third window")


root.mainloop()
