from dataclasses import dataclass
import tkinter as tk
from main import WIDTH, HEIGHT
from url import lex

H_STEP:      int = 13
V_STEP:      int = 18
SCROLL_STEP: int = 100


class Browser:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
        self.window.bind("<Up>", self.scrollup)

    def layout(self, text: str) -> list[tuple[int, int, str]]:
        cursor_x = H_STEP
        cursor_y = V_STEP
        display_list = []
        for c in text:
            display_list.append((cursor_x, cursor_y, c))
            cursor_x += H_STEP

            if cursor_x + H_STEP > WIDTH:
                cursor_x = H_STEP
                cursor_y += V_STEP

        return display_list

    def draw(self):
        self.canvas.delete("all")
        for coord_x, coord_y, c in self.display_list:
            self.canvas.create_text(coord_x, coord_y - self.scroll, text=c)

    def load(self, url: str):
        body = url.request()
        text = lex(body)
        self.display_list = self.layout(text)
        self.draw()

    def scrolldown(self, e):
        self.scroll += SCROLL_STEP
        self.draw()

    def scrollup(self, e):
        self.scroll -= SCROLL_STEP
        self.draw()


