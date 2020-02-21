import tkinter as tk
class Root(tk.Tk):
    def __init__(self, items = None):
        super().__init__()
        self.title("Regular GUI")
        self.geometry("600x400")


def main():
    # define two frames
    left = tk.Frame(root,bg="white")
    right = tk.Frame(root,bg="grey")

    left.grid(row=0,column=0,sticky="nsew")
    right.grid(row=0,column=1,sticky="nsew")

    # use grid 2x1 (col x row)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # show labels
    label = tk.Label(left, text = "Hello World")
    label.pack()
    label = tk.Label(right, text = "Console Output")
    label.pack()


if __name__ == "__main__":
    root = Root()
    main()
    root.mainloop()
