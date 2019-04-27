'''example program for using tkinter's radio button widget'''
from tkinter import *


# **** Functions ****
def display():
    response = radio_control.get()
    display_label.config(text=response)


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Radio Button Example")


# **** Add content to window ****
Label(root, text="Radio Button Example").pack()

radio_control = StringVar(value="Option 1")
Radiobutton(root, text="Option 1", variable=radio_control, value="Option 1", command=display).pack()
Radiobutton(root, text="Option 2", variable=radio_control, value="Option 2", command=display).pack()
Radiobutton(root, text="Option 3", variable=radio_control, value="Option 3", command=display).pack()
Radiobutton(root, text="Option 4", variable=radio_control, value="Option 4", command=display).pack()

display_label = Label(root)
display_label.pack()


# **** Run window loop ****
root.mainloop()