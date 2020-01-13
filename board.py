import tkinter as tk
class Root(tk.Tk):
    def __init__(self, items = None):
        super().__init__()
        if not items:
            self.items = []
        else:
            self.items = items
        self.title("Scripts GUI")
        self.geometry("300x400")
        item1 = tk.Label(self, text=" -- add items --", bg="lightgrey", fg="white", pady=10)
        self.items.append(item1)
        for item in self.items:
            item.pack(side=tk.TOP, fill=tk.X)
        self.item_create = tk.Text(self, height=3, bg="white", fg="black")
        self.item_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.item_create.focus_set()
        self.bind("<Return>", self.add_item)
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]
    def add_item(self, event=None):
        item_text = self.item_create.get(1.0,tk.END).strip()
        if len(item_text) > 0:
            new_item = tk.Label(self, text=item_text, pady=10)
            _, item_style_choice = divmod(len(self.items), 2)
            my_scheme_choice = self.colour_schemes[item_style_choice]
            new_item.configure(bg=my_scheme_choice["bg"])
            new_item.configure(fg=my_scheme_choice["fg"])
            new_item.pack(side=tk.TOP, fill=tk.X)
            self.items.append(new_item)
            self.item_create.delete(1.0, tk.END)
#            self.label.pack()
if __name__ == "__main__":
    root = Root()
    root.mainloop()
