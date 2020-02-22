import tkinter as tk


class GUI:

    # gui main winfow
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400+200+200")
        self.master.resizable(150, 150)
        self.master.title(" Master GUI")
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.quit = tk.Button(self.master, text="Create new", command=self.new_window)
        self.quit.pack()


    def new_window(self):
        self.new = tk.Toplevel(self.master)
        Win1(self.new,"New window")


class Win1:

    # open new window
    def __init__(self, master, text_one):
        self.master = master
        self.master.geometry("300x400")
        self.master.overrideredirect(0)
        self.master.resizable(10, 10)
        self.master.title("New window")
        self.frame1 = tk.Frame(master)
        self.frame1.pack()
        self.quit = tk.Button(self.master, text="x", command=self.close_window)
        self.quit.pack(side=tk.TOP, anchor=tk.E)

    def close_window(self):
        self.master.destroy()


root = tk.Tk()
app = GUI(root)

# no static windows
#win1 = tk.Toplevel(root)
#app1 = Win1(win1, "First window")

root.mainloop()
