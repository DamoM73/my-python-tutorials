# example program for using tkinter's  spinbox widget
from tkinter import *


# **** Functions ****
def display():
    selection = choice_sb.get()
    display_label.config(text=str(selection))


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Spin Box Example")


# **** Add window content ****
Label(root, text="Spin Box Example").pack()

choice_sb = Spinbox(root, from_=0, to=5, command=display)
choice_sb.pack()

display_label = Label(root)
display_label.pack()


# **** Run window loop ****
root.mainloop()
