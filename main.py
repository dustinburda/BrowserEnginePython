import tkinter as tk

WIDTH: int = 1920
HEIGHT: int = 1080

if __name__ == "__main__":
    window = tk.Tk()
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    canvas.create_rectangle(10, 20, 400, 300)
    canvas.create_text(40, 50, text="Hello World! My first tkinter window!", fill="black")

    tk.mainloop()
    print(3)