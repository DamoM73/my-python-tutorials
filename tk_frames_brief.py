from tkinter import *

root = Tk()
#root.geometry("300x200")
root.title("Tkinter Frames")

# **** Create and pack top label ****
Label(root, text="One", bg="blue", fg="white").pack(fill=BOTH, expand=TRUE)

# **** Create and pack middle frame ****
middle_frame = Frame(root).pack(fill=BOTH, expand=TRUE)

# **** Create middle labels and pack into middle frame
Label(middle_frame, text="Two", bg="yellow", fg="black").pack(side=LEFT, fill=BOTH, expand=TRUE)
Label(middle_frame, text="Three", bg="red", fg="black").pack(side=LEFT, fill=BOTH, expand=TRUE)
Label(middle_frame, text="Four", bg="green", fg="black").pack(side=LEFT, fill=BOTH, expand=TRUE)

# **** Create and pack bottom label
label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.pack(fill=BOTH, expand=TRUE)

# **** Run window loop ****
root.mainloop()