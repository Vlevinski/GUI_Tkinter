import tkinter as tk
import time

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

class Timer:

    # timer window
    def __init__(self,master):
        self.master = master
        self.master.geometry("100x65+100+100")
        self.master.title("Timer")
        self.frame2 = tk.Frame(master)
        self.frame2.pack()

root = tk.Tk()
app = GUI(root)

# no static windows
#win1 = tk.Toplevel(root)
#app1 = Win1(win1, "First window")

# timer
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

win1 = tk.Toplevel(root)
app1 = Win1(win1, "First window")
win1.geometry("100x70+0+0")
time1 = ''
clock = tk.Label(win1, font=('times', 20, 'bold'), bg='green')
clock.pack(side=tk.TOP, anchor=tk.E)

tick()
root.mainloop()
