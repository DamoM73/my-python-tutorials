# example program for tkinter's listbox widget

from tkinter import *

# **** Functions ****
def display():
    value = options_lb.curselection()
    display_label.config(text=str(value))


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Listbox Example")

# *** Window content ****
Label(root, text="List Box Example").pack()

options_lb = Listbox(root,height=4)
options_lb.insert(1,"Option One")
options_lb.insert(2,"Option Two")
options_lb.insert(3,"Option Three")
options_lb.insert(4,"Option Four")
options_lb.pack()

display_btn = Button(root, text="Display selected", command=display)
display_btn.pack()

display_label = Label(root, text="")
display_label.pack()


# **** Window loop ****
root.mainloop()