import tkinter as tk


class Root(tk.Tk):
    def __init__(self, items=None):
        super().__init__()
        self.title("GUI")
        self.geometry("300x400")
        self.label = tk.Label(self, text="Desktop", fg="white", padx=5, pady=5)
        self.label.pack()



if __name__ == "__main__":
    root = Root()
    root.mainloop()
