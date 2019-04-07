import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Window Name")
        self.geometry("1000x600")



# ---- MAIN PROGRAM ----
main = Main()
main.mainloop()