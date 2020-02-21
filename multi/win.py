import tkinter as tk


window = tk.Tk()
window.geometry("300x400")

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()

'''
label = tk.Label(text="    Python rocks!   ", bg= "#B0C4DE", fg="black",     width=10,    height=2)
label.pack()
button = tk.Button(
    text="Click me!",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
)
button.pack()
'''

window.mainloop()
