from tkinter import *

# **** Functions ****
def display():
    selected = "You selected " + option_control.get()
    display_label.config(text=selected)

# **** Create Window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Option Menu Example")

# **** Add Content to Window ****
Label(root, text="Option Menu Example").grid(row=0, column=0, columnspan=2)

Label(root, text="Choose an option").grid(row=1, column=0)

option_list = ('Option 1', 'Option 2', 'Option 3', 'Option 4')
option_control=StringVar()
option_control.set(option_list[0])
choice = OptionMenu(root, option_control, *option_list)
choice.grid(row=1,column=1)

display_btn = Button(root, text="Display selected value", command=display)
display_btn.grid(row=2, column=0, columnspan=2)

display_label = Label(root,text="")
display_label.grid(row=3, column=0, columnspan=2)

# **** Run window loop ****
root.mainloop()