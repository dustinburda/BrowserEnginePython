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

    print("Yada yada, this is  main branch")

    print("Hello this is I")

    print("Merge conflicts..............!")

    print(4)
