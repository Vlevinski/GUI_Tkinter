import tkinter as tk

root=tk.Tk()
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
lbl1 = tk.Label(topl, text= txt1, font=('helvetica', 15, 'bold'), fg="white", bg="brown1").pack(side=tk.BOTTOM)
lbl2 = tk.Label(botl, text= txt2, fg="white", bg="brown1").pack()

# right
lbl9 = tk.Label(frm2, text= "Hello \nworld").pack(fill=tk.BOTH, expand=tk.YES)


root.mainloop()
