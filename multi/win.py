import tkinter as tk
import time
import datetime

class GUI:

    # gui main window
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
        Win1(self.new, "New window")


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


'''
class Stimer:

    # timer window
    def __init__(self,master):
        self.master = master
        self.master.geometry("100x65+100+100")
        self.master.title("Timer")
        self.frame2 = tk.Frame(master)
        self.frame2.pack()
'''


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x70+10+10")
        self.master.title("Timer")
        self.date1 = tk.Label(self.master, text=f"{datetime.datetime.now():%a, %b %d %Y}", fg="red", font=("helvetica", 12))
        self.date1.pack()
        self.clock = tk.Label(self.master, font=('times', 30, 'bold'), bg='green')
#        self.clock.grid(row=0, column=1)
        self.clock.pack()

    def tick(self):
        time_string = time.strftime('%H:%M:%S')
        self.clock.config(text=time_string)
        self.clock.after(200, self.tick)


root = tk.Tk()
app = GUI(root)

# no static windows
# win1 = tk.Toplevel(root)
# app1 = Win1(win1, "First window")

tm = tk.Toplevel(root)
app2 = Timer(tm)
app2.tick()
root.mainloop()
