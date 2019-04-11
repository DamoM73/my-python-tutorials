from tkinter import *

# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Label Frame Example")

# **** Add window content ****
example_label_frame = LabelFrame(root, text="A collection of labels", padx=5, pady=5)
example_label_frame.pack()

example_label_1 = Label(example_label_frame, text="This is the example label")
example_label_1.grid(row=0, column=0, sticky=W)

example_label_2 = Label(example_label_frame, text="This is another example label")
example_label_2.grid(row=1, column=0, sticky=W)


# **** Run window loop ****
root.mainloop()