from tkinter import *

# **** Functions ****
def display():
    response = choice.get()
    display_label.config(text=response+" selected")


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Radio Button Example")


# **** Add content to window ****
Label(root, text="Radio Button Example").pack()

# Create radio buttons
choice = StringVar(value="Option 1")
Radiobutton(root, text="Option 1", variable=choice, value="Option 1", command=display).pack()
Radiobutton(root, text="Option 2", variable=choice, value="Option 2", command=display).pack()
Radiobutton(root, text="Option 3", variable=choice, value="Option 3", command=display).pack()
Radiobutton(root, text="Option 4", variable=choice, value="Option 4", command=display).pack()

display_label = Label(root, text=choice.get()+" selected")
display_label.pack()


# **** Run window loop ****
root.mainloop()