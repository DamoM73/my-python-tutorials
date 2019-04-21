# example program for using tkinter's scale widget

from tkinter import *

# **** Functions ****
def display():
    selection = "Value = " + str(value.get())
    display_label.config(text=selection)



# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Scale Example")

# **** Create window content ****
Label(root,text="Scale Example")

value = DoubleVar()
input_sc = Scale(root, variable=value)
input_sc.pack()

display_btn = Button(root, text="Display slider value", command=display)
display_btn.pack()

display_label = Label(root, text="")
display_label.pack()

# **** Run window loop ****
root.mainloop()