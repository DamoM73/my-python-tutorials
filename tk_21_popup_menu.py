'''example program for creating popup menus in tkinter'''
from tkinter import *


# **** Functions ****
def hello():
    message.config(text="Hello")

def goodbye():
    message.config(text="Goodbye")

def popup(event):
    popup_menu.post(event.x_root, event.y_root)


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Popup Menu Example")

# **** Add content to window ****
message = Label(root, text="", bg="white")
message.pack(fill=BOTH, expand=YES)

# create popup menu
popup_menu = Menu(root, tearoff=0)
popup_menu.add_command(label="Hello", command=hello)
popup_menu.add_command(label="Goodbye", command=goodbye)

# bind popup to label
message.bind("<Button-3>", popup)


# **** Run window loop ****
root.mainloop()