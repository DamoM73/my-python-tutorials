from tkinter import *

# **** Functions ****
def display_check():
    check_value = check_state.get()
    value_label.config(text=str(check_value))


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Check Button")

# **** Window content ****
Label(root, text="Check Box Example").pack()

check_state = IntVar()
check_ck = Checkbutton(root, text="Click this check button", variable=check_state)
check_ck.pack()

display_btn = Button(root, text="Display value", command=display_check)
display_btn.pack()

value_label = Label(root)
value_label.pack()

# **** Window Loop ****
root.mainloop()