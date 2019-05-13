'''example program for tkinter toplevel'''
from tkinter import *

def say_hello():
    # **** Create hello window ****
    hello = Tk()
    hello.geometry("300x200")
    hello.title("Hello window")

    # add hello window content
    Label(hello, text="Hello").pack(fill=BOTH, expand=YES)

def say_goodbye():
    # **** Create hello window ****
    goodbye = Tk()
    goodbye.geometry("300x200")
    goodbye.title("Goodbye window")

    # add goodbye window content
    Label(goodbye, text="Goodbye").pack(fill=BOTH, expand=YES)


def goodbye():
    pass

# **** Create root window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Toplevel Example")

# **** add root window content ****
Button(root, text="Hello window", command=say_hello).pack()
Button(root, text="Goodbye window", command=say_goodbye).pack()

# **** run window loop ****
root.mainloop()