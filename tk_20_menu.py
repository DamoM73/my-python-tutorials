'''example program for creating menus in tkinter'''
from tkinter import *


# **** Functions ****
def hello():
    message.config(text="Hello")

def goodbye():
    message.config(text="Goodbye")

def white():
    message.config(bg="white")

def yellow():
    message.config(bg="yellow")


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Menu Example")


# **** Add content to window ****
message = Label(root, bg="white")
message.pack(fill=BOTH, expand=YES)

# create menu
menubar = Menu(root)

# create text menu
text_menu = Menu(menubar, tearoff=0)
text_menu.add_command(label="Hello", command=hello)
text_menu.add_command(label="Goodbye", command=goodbye)
menubar.add_cascade(label="Text", menu=text_menu)

# create background menu
bg_menu = Menu(menubar, tearoff=0)
bg_menu.add_command(label="White", command=white)
bg_menu.add_command(label="Yellow", command=yellow)
menubar.add_cascade(label="Background", menu=bg_menu)

# dsiplay menu
root.config(menu=menubar)


# **** Run window loop ****
root.mainloop()