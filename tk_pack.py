# example program for using tkinter's pack geometry manager 

from tkinter import *

# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Pack Example")

# **** Create and pack label ****
label_one = Label(root, text="One", bg="blue", fg="white")
label_one.pack(side=TOP, fill=BOTH)
label_two = Label(root, text="Two", bg="yellow", fg="black")
label_two.pack(side=LEFT, fill=BOTH)
label_three = Label(root, text="Three", bg="red", fg="black")
label_three.pack(side=LEFT, fill=BOTH)
label_four = Label(root, text="Four", bg="green", fg="black")
label_four.pack(side=LEFT, fill=BOTH)
label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.pack(side=BOTTOM, fill=BOTH)


root.mainloop()