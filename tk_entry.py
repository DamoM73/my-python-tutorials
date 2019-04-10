from tkinter import *

# **** Functions ****
def read_entry():
    user_input = entry_box.get()
    entry_box.delete(0, END)
    display_label.config(text=user_input)


# **** Create window ****
root=Tk()
root.geometry("300x200")
root.title("Tkinter Entry")


# **** Display window content ****
Label(root, text="Entry Widget").grid(row=0,column=0,columnspan=3)

Label(root,text="Enter message:").grid(row=1,column=0)

entry_box = Entry(root)
entry_box.grid(row=1, column=1)

display_btn = Button(root, text="", command=read_entry)
display_btn.grid(row=1, column=2)

display_label = Label(root, text="Nothing")
display_label.grid(row=2,column=0, columnspan=3)


# **** Window loop ****
root.mainloop()