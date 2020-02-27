import tkinter as tk
from tkinter import ttk
import datetime as dt
import time
from multi.gui import GUI,Win1,Tables,Framic, Buttonic, Colorite, Timer


root = tk.Tk()
app = GUI(root)

# no static windows
win1 = tk.Toplevel(root)
app1 = Win1(win1)
image = tk.PhotoImage(file='img/plot.png')
label = tk.Label(win1, image=image)
label.pack()

win7 = tk.Toplevel(root)
app7 = Win1(win7)
image7 = tk.PhotoImage(file='img/plot1.png')
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
