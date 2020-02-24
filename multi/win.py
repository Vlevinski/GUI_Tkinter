import tkinter as tk
from tkinter import ttk

root = tk.Tk()

photo1 = tk.PhotoImage(file="ic_group_black_24dp.png")
photo2 = tk.PhotoImage(file="ic_mood_black_24dp.png")
photo3 = tk.PhotoImage(file="ic_plus_one_black_24dp.png")
photo4 = tk.PhotoImage(file="ic_public_black_24dp.png")
photo5 = tk.PhotoImage(file="ic_person_add_black_24dp.png")
photo6 = tk.PhotoImage(file="ic_whatshot_black_24dp.png")


def btn(ptn):
    button = ttk.Button(root)
    button.grid()
    button.config(image=ptn, compound=tk.RIGHT)
    return button


btn(photo1)
btn(photo2)
btn(photo3)
btn(photo4)
btn(photo5)
btn(photo6)

root.mainloop()
