import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Window Name")
        #self.geometry("1000x600")

        self.blue = tk.Label(self,text="BLUE", bg="blue", fg="white", width=20)
        self.blue.grid(column=0, row=0)

        self.red = tk.Label(self, text="RED", bg="red", width=20)
        self.red.grid(column=1, row=0)
        
        self.yellow = tk.Label(self, text="YELLOW", bg="yellow", width=20)
        self.yellow.grid(column=2, row=0)

        self.green = tk.Label(self, text="GREEN", bg="green", width=20)
        self.green.grid(column=0, columnspan=2, row=1)

        self.purple = tk.Label(self, text="PURPLE", bg="purple", width=20)
        self.purple.grid(column=2,row=1)

        self.organe = tk.Label(self, text="ORANGE", bg="orange", width=20)
        self.organe.grid(column=1,row=2)

# ---- MAIN PROGRAM ----
main = Main()
main.mainloop()