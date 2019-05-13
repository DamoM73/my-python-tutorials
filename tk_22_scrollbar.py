'''example program for using scrollbars'''
from tkinter import *


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Scrollbar Example")


# **** add content to window ****
scrollbar = Scrollbar(root)
scrollbar.pack(side =RIGHT, fill=Y)

my_list = Listbox(root, yscrollcommand = scrollbar.set)

for line in range(100):
    my_list.insert(END, "This is line "+str(line))

my_list.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=my_list.yview)


# **** run window loop ****
root.mainloop()