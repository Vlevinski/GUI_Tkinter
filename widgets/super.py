import tkinter as tk


class Application(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Button(self, text='Super!', command=root.destroy).pack()


root = tk.Tk()
Application(root).pack()
root.mainloop()
