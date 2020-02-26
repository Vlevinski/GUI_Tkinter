import tkinter as tk
from tkinter import ttk
import datetime as dt
import time


class GUI:

    def __init__(self, master):
        # gui window
        self.master = master
        self.master.geometry("600x400+200+200")
        self.master.resizable(150, 150)
        self.master.title(" Master GUI")

        self.lPane = tk.Frame(self.master, bg="white")
        self.rPane = tk.Frame(self.master, bg="grey")

        self.lPane.grid(row=0, column=0, sticky="nsew")
        self.rPane.grid(row=0, column=1, sticky="nsew")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        self.quit = tk.Button(self.lPane, text="Create", command=self.new_window)
        self.quit.pack()
        self.label = tk.Label(self.rPane, text="Console")
        self.label.pack()

    def new_window(self):
        self.new = tk.Toplevel(self.master)
        Win1(self.new)


class Win1:

    def __init__(self, master):
        self.master = master
        self.master.geometry("800x400")
        self.master.overrideredirect(0)
        self.master.resizable(10, 10)
        self.master.title("New window")
        self.frame1 = tk.Frame(master)
        self.frame1.pack()
#        self.quit = tk.Button(self.master, text="x", command=self.close_window)
#        self.quit.pack(side=tk.TOP, anchor=tk.E)

    def close_window(self):
        self.master.destroy()


class Tables:

    def __init__(self, master):
        self.master = master
        self.master.geometry("980x300")
        self.master.overrideredirect(0)
        self.master.resizable(10, 10)
        self.master.title("Table")
        self.frame1 = tk.Frame(master)
        self.frame1.pack()
#        self.quit = tk.Button(self.master, text="x", command=self.close_window)
#        self.quit.pack(side=tk.TOP, anchor=tk.E)
        self.label = tk.Label(self.master, text="Contry rainfall", font=("Arial", 30)).pack()

        # create Treeview with 5 columns
        self.cols = ('Position', "City name", "Area", "Population", "Annual Rainfall")
        self.listBox = ttk.Treeview(self.master, columns=self.cols, show='headings')

        # set column headings
        for col in self.cols:
            self.listBox.heading(col, text=col)
        self.listBox.pack()

        tk.Button(self.master, text="Show scores", width=10, command=self.show).pack()

    def close_window(self):
        self.master.destroy()

    def show(self):

        tempList = [
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4],
            ["Darwin", 112, 120900, 1714.7],
            ["Hobart", 1357, 205556, 619.5],
            ["Sydney", 2058, 4336374, 1214.8],
            ["Melbourne", 1566, 3806092, 646.9],
            ["Perth", 5386, 1554769, 869.4]
        ]
        tempList.sort(key=lambda e: e[0], reverse=False)

        for i, (name, area, population, annual) in enumerate(tempList, start=1):
            self.listBox.insert("", "end", values=(i, name, area, population, annual))


class Framic:
    def __init__(self, master):
        # frames window
        self.master = master
        self.master.geometry("100x220")
        self.master.title("Framic")
        self.master.configure(background="LightBlue1")
        self.l1 = self.label("USD").pack()
        self.l2 = self.label("EUR").pack()
        self.l3 = self.label("RUB").pack()
        self.l4 = self.label("ROL").pack()
        self.l5 = self.label("GBR").pack()
        self.l6 = self.label("MDL").pack()

    def label(self, txt):
        return tk.Button(self.master, text=txt, fg="white", bg="LightBlue1", font=("helvetica", 12))


class Buttonic:

    def __init__(self, master):
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
        return tk.Button(self.master, text=txt, fg="white", bg="LightBlue1", font=("helvetica", 12))

    def png_btn(self, png_file):
        self.button = ttk.Button(self.master)
        self.button.pack()
        self.button.config(image=png_file)
        return self.button


class Colorite:

    def __init__(self, master):
        # colorite window
        self.master = master
        self.master.geometry("80x300")
        self.master.title("Colorit")
        self.btn()

    def btn(self):
        # btn multicolor
        colors = ["blue", "yellow", "green", "red", "violet", "pink", "brown", "grey", "orange"]
        for txt in colors:
            tk.Button(self.master, text=txt, bg="white", fg=txt, font=("helvetica", 12)).pack(fill=tk.X)


class Timer:

    def __init__(self, master):
        self.master = master
        self.master.geometry("200x120+10+10")
        self.master.title("Timer")
        self.date1 = tk.Label(self.master, text=f"{dt.datetime.now():%a, %b %d, %Y \n}", fg="black",
                              font=("helvetica", 12))
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
app1 = Win1(win1)
image = tk.PhotoImage(file='plot.png')
label = tk.Label(win1, image=image)
label.pack()

win7 = tk.Toplevel(root)
app7 = Win1(win7)
image7 = tk.PhotoImage(file='plot1.png')
label = tk.Label(win7, image=image7)
label.pack()

tm = tk.Toplevel(root)
app2 = Timer(tm)
app2.tick()

win3 = tk.Toplevel(root)
app3 = Framic(win3)

win4 = tk.Toplevel(root)
app4 = Buttonic(win4)

win5 = tk.Toplevel(root)
app5 = Colorite(win5)

win6 = tk.Toplevel(root)
app6 = Tables(win6)

root.mainloop()
