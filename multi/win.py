import tkinter as tk


class GUI:

    def __init__(self, master):
        self.master = master


root = tk.Tk()
app = GUI(root)
root.mainloop()
