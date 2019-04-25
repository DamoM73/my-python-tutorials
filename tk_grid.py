# example program for using tkinter's grid geometery manager

from tkinter import *

# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Grid Example")

# **** Create and pack label ****
label_one = Label(root, text="One", bg="blue", fg="white")
label_one.grid(row=0, column=0, columnspan=3)

label_two = Label(root, text="Two", bg="yellow", fg="black")
label_two.grid(row=1, column=0)
label_three = Label(root, text="Three", bg="red", fg="black")
label_three.grid(row=1, column=1)
label_four = Label(root, text="Four", bg="green", fg="black")
label_four.grid(row=1, column=2)

label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.grid(row=2, column=0, columnspan=3)


root.mainloop()