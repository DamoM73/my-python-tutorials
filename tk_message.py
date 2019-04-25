# example program for using tkinter's message widget

from tkinter import *

# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Message Example")

# **** Add window content ****
example_message = Message(root, text="Mesages are just like lables, except their text can go over several lines.", bg="light blue", width=150)
example_message.pack()

# **** Run window loop ****
root.mainloop()