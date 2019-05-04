'''example program for using tkinter's scale widget'''
from tkinter import *

# **** Functions ****
def display():
    selection = value.get()
    display_label.config(text=str(selection))


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Scale Example")


# **** Add window content ****
Label(root,text="Scale Example").pack()

value = DoubleVar()
Scale(root, variable=value).pack()

Button(root, text="Display slider value", command=display).pack()

display_label = Label(root)
display_label.pack()


# **** Run window loop ****
root.mainloop()
