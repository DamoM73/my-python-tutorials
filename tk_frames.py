from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Tkinter Frames Example")

# **** Create and pack top label ****
label_one = Label(root, text="One", bg="blue", fg="white")
label_one.pack(fill=BOTH, expand=TRUE)

# **** Create and pack middle frame ****
middle_frame = Frame(root)
middle_frame.pack(fill=BOTH, expand=TRUE)

# **** Create middle labels and pack into middle frame
label_two = Label(middle_frame, text="Two", bg="yellow", fg="black")
label_two.pack(side=LEFT, fill=BOTH, expand=TRUE)
label_three = Label(middle_frame, text="Three", bg="red", fg="black")
label_three.pack(side=LEFT, fill=BOTH, expand=TRUE)
label_four = Label(middle_frame, text="Four", bg="green", fg="black")
label_four.pack(side=LEFT, fill=BOTH, expand=TRUE)

# **** Create and pack bottom label
label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.pack(fill=BOTH, expand=TRUE)

# **** Run window loop ****
root.mainloop()
