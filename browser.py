from dataclasses import dataclass
import tkinter as tk
import tkinter.font
from main import WIDTH, HEIGHT
from url import lex
from elements import Tag, Text
from layout import Layout, H_STEP, V_STEP

N_STEP: int = 24
SCROLL_STEP: int = 100


class Browser:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.scroll = 0
        self.min = 0
        self.max = 0
        self.window.bind("<Down>", self.scrolldown)
        self.window.bind("<Up>", self.scrollup)

    def draw(self):
        self.canvas.delete("all")
        for coord_x, coord_y, word, font in self.display_list:
            if coord_y > self.scroll + HEIGHT:
                continue
            if coord_y + V_STEP < self.scroll:
                continue
            self.canvas.create_text(coord_x, coord_y - self.scroll, text=word, anchor="nw",
                                    font=font)  # , font=self.bi_times)

    def load(self, url: str):
        body = url.request()
        tokens = lex(body)

        layout = Layout(tokens)
        self.display_list = layout.display_list
        self.max = layout.max_scroll

        self.draw()

    def scrolldown(self, e):
        self.scroll += min(SCROLL_STEP, self.max - self.scroll)
        # self.scroll += SCROLL_STEP
        # print("Max: ", self.max, "Scroll: ", self.scroll)
        self.draw()

    def scrollup(self, e):
        self.scroll -= min(SCROLL_STEP, self.scroll)
        # self.scroll -= SCROLL_STEP
        print("Min: ", self.min, "Scroll: ", self.scroll)
        print(self.scroll)
        self.draw()
