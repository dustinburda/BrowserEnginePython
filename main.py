import tkinter as tk
from url import *

WIDTH: int = 800
HEIGHT: int = 600

if __name__ == "__main__":
    window = tk.Tk()
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    canvas.create_rectangle(10, 20, 400, 300)    
    tk.mainloop()

    print("Yada yada, this is rebase-branch")

    print("Hello this is I")

    print(4)
