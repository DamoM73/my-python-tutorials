from tkinter import *

master = Tk()
variable = StringVar()
w = OptionMenu(master, variable, "one", "two", "three")  
w.config(bg = "GREEN")  # Set background color to green

# Set this to what you want, I'm assuming "green"...
w["menu"].config(bg="GREEN")

w.pack() 

master.mainloop()