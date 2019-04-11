from tkinter import *

# **** Functions ****
def display():
    selection = "You have choosen " + choice_sb.get()
    display_label.config(text=selection)

# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Spin Box Example")

# **** Add window content ****
Label(root, text="Spin Box Example")

choice_sb = Spinbox(root, from_=0, to=5, command=display)
choice_sb.pack()

display_label = Label(root, text="")
display_label.pack()


# **** Run window loop ****
root.mainloop()