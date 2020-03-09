import tkinter as tk


def pressed():
    print(" You pressed the button !")


root = tk.Tk()
root.title("Main")
root.geometry("500x300")

txt1 = "Welcome Back !\n"
txt2 = "To keep connected with us please login \n with your personal info"

# frames
frm1 = tk.Frame(root, bg="blue")
frm2 = tk.Frame(root, bg="white")
topl = tk.Frame(frm1, bg="brown1")
botl = tk.Frame(frm1, bg="brown1")

# frames packs
frm1.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
frm2.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
topl.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
botl.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)

# left
lbl1 = tk.Label(topl, text=txt1, font=('helvetica', 15, 'bold'), fg="white", bg="brown1").pack(side=tk.BOTTOM)
lbl2 = tk.Label(botl, text=txt2, fg="white", bg="brown1").pack()

# buttons
btn1 = tk.Button(botl, text="SIGN IN", fg="brown1", bg="white", command=lambda: pressed()).pack(expand=tk.YES)
btn2 = tk.Button(frm2, text="SIGN UP", command=lambda: pressed()).pack(expand=tk.YES)

root.mainloop()
