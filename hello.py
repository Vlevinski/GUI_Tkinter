import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x100+200+100")
    label = tk.Label(text="Hello").pack()
    root.mainloop()
