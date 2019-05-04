'''example program for tkinter's messagebox'''
from tkinter import *
from tkinter import messagebox


# **** Functions ****
def hello():
   messagebox.showinfo("Say Hello", "Hello World")


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Message Box Example ")


# **** Add content to window ****
Button(root, text = "Say Hello", command = hello).pack()


# **** Run window loop ****
root.mainloop()
