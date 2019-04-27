# example program on how to use tkitner frames in classes

import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Window Name")
        #self.geometry("1000x600")

        self.frame_one = tk.Frame(self, bg="blue", width=1000, height=300)
        self.frame_two = tk.Frame(self, bg="pink", width=500, height=300)
        self.frame_one.pack()
        self.frame_two.pack()


# ---- MAIN PROGRAM ----
main = Main()
main.mainloop()