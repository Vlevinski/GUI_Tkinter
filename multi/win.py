import tkinter as tk
from tkinter import ttk
import time
import datetime as dt


class GUI:


    def __init__(self, master):
        # gui window
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


    def __init__(self, master, text_one):
        # new window
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


    def __init__(self,master):
        # frames window
        self.master = master
        self.master.geometry("100x300")
        self.master.title("Framic")
        self.master.configure(background="LightBlue1")
        self.l1 = self.label("\nFrame1").pack()
        self.l2 = self.label("\nFrame2").pack()

    def label(self, txt):
        return tk.Label(self.master, text=txt, fg="white", bg="LightBlue1",font=("helvetica", 12))


class Buttonic:


    def __init__(self,master):
        # pic buttons
        self.master = master
        self.master.geometry("40x210")
        self.master.title("Framic")
        self.png_btn(photo1)
        self.png_btn(photo2)
        self.png_btn(photo3)
        self.png_btn(photo4)
        self.png_btn(photo5)
        self.png_btn(photo6)

    def btn(self, txt):
        return tk.Button(self.master, text=txt, fg="white", bg="LightBlue1",font=("helvetica", 12))

    def png_btn(self, png_file):
        self.button= ttk.Button(self.master)
        self.button.pack()
        self.button.config(image=png_file)
        return self.button

class Colorite:

    def __init__(self,master):
        # colorite window
        self.master = master
        self.master.geometry("80x300")
        self.master.title("Colorit")
        self.btn()


    def btn(self):
        # btn multicolor
        colors = ["blue","yellow","green","red","violet","pink","brown","grey","orange"]
        for txt in colors:
            tk.Button(self.master, text=txt, bg="white", fg=txt,font=("helvetica", 12)).pack(fill=tk.X)



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

photo1 = tk.PhotoImage(file="ic_group_black_24dp.png")
photo2 = tk.PhotoImage(file="ic_mood_black_24dp.png")
photo3 = tk.PhotoImage(file="ic_plus_one_black_24dp.png")
photo4 = tk.PhotoImage(file="ic_public_black_24dp.png")
photo5 = tk.PhotoImage(file="ic_person_add_black_24dp.png")
photo6 = tk.PhotoImage(file="ic_whatshot_black_24dp.png")

# no static windows
win1 = tk.Toplevel(root)
app1 = Win1(win1, "First window")

win3 = tk.Toplevel(root)
app3 = Framic(win3)

win4 = tk.Toplevel(root)
app4 = Buttonic(win4)

win5 = tk.Toplevel(root)
app5 = Colorite(win5)

tm = tk.Toplevel(root)
app2 = Timer(tm)
app2.tick()

root.mainloop()
