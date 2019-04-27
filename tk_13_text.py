'''example program for using tkinter's text widget'''
from tkinter import *


# **** Functions ****
def display():
    user_input = text_box.get(1.0,END)
    text_box.delete(1.0,END)
    display_message.config(text=user_input)


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Text Box Example")


# **** Add window content ****
Label(root, text="Enter message below:").pack()

text_box = Text(root, width=30, height=4)
text_box.pack()

Button(root, text="Display", command=display).pack()

display_message = Message(root)
display_message.pack(fill=BOTH, expand=YES)


# **** Run window loop ****
root.mainloop()