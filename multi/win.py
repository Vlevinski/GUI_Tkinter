import tkinter as tk
import time
import datetime as dt


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


class Framic:

    # timer window
    def __init__(self,master):
        self.master = master
        self.master.geometry("100x300")
        self.master.title("Framic")
        self.master.configure(background="LightBlue1")
        self.l1 = self.label("\nFrame1").pack()
        self.l2 = self.label("\nFrame2").pack()

    def label(self, txt):
        return tk.Label(self.master, text=txt, fg="white", bg="LightBlue1",font=("helvetica", 12))


class Buttonic:

    # timer window
    def __init__(self,master):
        self.master = master
        self.master.geometry("100x300")
        self.master.title("Framic")
        self.master.configure(background="LightBlue1")

        self.btn1 = self.btn("btn1")
        self.btn1.pack()

        self.btn2 = self.png_btn("ic_group_black_24dp.png")
        self.btn2.pack()

        self.btn3 = self.btn("btn3")
        self.btn3.pack()

    def btn(self, txt):
        return tk.Button(self.master, text=txt, fg="white", bg="LightBlue1",font=("helvetica", 12))

    def png_btn(self, png_file):
        self.photo = tk.PhotoImage(file=png_file, master=self.master)
        self.button= tk.Button(self.master)
        self.button.config(image=self.photo)
        return self.button



class Timer:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x120+10+10")
        self.master.title("Timer")
        self.date1 = tk.Label(self.master, text=f"{dt.datetime.now():%a, %b %d, %Y \n}", fg="black", font=("helvetica", 12))
        self.date1.pack()
        self.clock = tk.Label(self.master, font=('times', 30, 'bold'), bg='green', fg="white")
        self.clock.pack()

    def tick(self):
        time_string = time.strftime('%H:%M:%S')
        self.clock.config(text=time_string)
        self.clock.after(200, self.tick)


root = tk.Tk()
app = GUI(root)

# no static windows
win1 = tk.Toplevel(root)
app1 = Win1(win1, "First window")

win3 = tk.Toplevel(root)
app3 = Framic(win3)

win4 = tk.Toplevel(root)
app4 = Buttonic(win4)

tm = tk.Toplevel(root)
app2 = Timer(tm)
app2.tick()

root.mainloop()
