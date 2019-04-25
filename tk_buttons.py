# example of how to use the tkinter button widget

from tkinter import *

# **** Functions ****
def change_colour():
    global colour
    
    colour = (colour + 1) % len(colours)
    change_colour_btn.config(bg=colours[colour])

# **** Global Variables ****
colour = 0
colours = ['blue','red','yellow','green','purple', 'orange', 'white']


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Button Example")

# **** Add content to window ****
change_colour_btn = Button(root, text="Click to change colour", bg=colours[colour],  command=change_colour)
change_colour_btn.pack()

# **** Run window loop ****
root.mainloop()