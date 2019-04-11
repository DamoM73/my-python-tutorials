from tkinter import *

# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Create Window")

# **** Add window content ****
example_label = Label(root, text="This is the example label", bg="light blue")
example_label.pack()

# **** Run window loop ****
root.mainloop()