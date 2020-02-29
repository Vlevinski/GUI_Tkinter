import tkinter as tk


class Root(tk.Tk):
    def __init__(self, items=None):
        super().__init__()
        if not items:
            self.items = []
        else:
            self.items = items
        self.title("Regular GUI")
        self.label = tk.Label(self, text="Hello World", padx=5, pady=5)
        self.label.pack()


if __name__ == "__main__":
    root = Root()
    root.geometry("600x400")
    root.mainloop()
