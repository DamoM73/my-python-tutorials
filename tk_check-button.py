from tkinter import *

# **** Functions ****
def display():
    check_value = check_state.get()
    value_label.config(text=str(check_value))


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Check Button Example")

# **** Window content ****
Label(root, text="Check Box Example").pack()

check_state = IntVar()
check_ck = Checkbutton(root, text="Click this check button", variable=check_state, command=display)
check_ck.pack()

value_label = Label(root)
value_label.pack()

# **** Window Loop ****
root.mainloop()