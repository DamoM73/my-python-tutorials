'''example program in how to use the tkinter checkbutton widget'''
from tkinter import *


# **** Functions ****
def display():
    check_value = check_control.get()
    value_label.config(text=str(check_value))


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Check Button Example")


# **** Add window content ****
Label(root, text="Check Box Example").pack()

check_control = IntVar()
Checkbutton(root, text="Click this check button", variable=check_control, command=display).pack()

value_label = Label(root)
value_label.pack()


# **** Window Loop ****
root.mainloop()