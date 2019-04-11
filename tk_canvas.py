from tkinter import *

# **** Create window ****
root = Tk()
root.geometry("450x225")
root.title("Tkinter Canvas Example")

# **** Create window content ****
shape_canvas = Canvas(root, bg="light blue", width=225, height=225)
image_canvas = Canvas(root, bg="violet", width=225, height=225)

# **** Draw shapes ****
shape_canvas.create_line(112,0,112,225, fill="black", width=2)
shape_canvas.create_line(0,112,225,112, fill="black", width=2)
shape_canvas.create_arc(5,5,107,107, start=30, extent=300, fill="yellow")
shape_canvas.create_oval(118,5,220,107, fill="blue")
shape_canvas.create_rectangle(5,118,107,220, fill="red")
shape_canvas.create_polygon(170,118,220,220,118,220, fill="green")

# **** Draw image ****
photo = PhotoImage(file="dog.png")
image_canvas.create_image(0,0, anchor=NW, image=photo)
image_canvas.create_text(112,10, text="Cute!", fill="yellow")


# **** Show canvas ****
shape_canvas.grid(row=0, column=0)
image_canvas.grid(row=0, column=1)

# **** Run window loop ****
root.mainloop()