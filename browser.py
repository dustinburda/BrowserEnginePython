from dataclasses import dataclass
import tkinter as tk
import tkinter.font
from main import WIDTH, HEIGHT
from url import lex
from elements import Tag, Text

H_STEP:      int = 13
V_STEP:      int = 18
N_STEP:      int = 24
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


    def layout(self, tokens: list[str]) -> list[tuple[int, int, str]]:
        # TODO: refactor this
        display_list = []
        cursor_x = H_STEP
        cursor_y = V_STEP
        weight = "normal"
        style = "roman"
        size = 16

        for tok in tokens:
            if isinstance(tok, Text):
                for word in tok.text.split():
                    font = tkinter.font.Font(size=size, weight=weight, slant=style)
                    w = font.measure(word)

                    if word == "\n":
                        cursor_x = H_STEP
                        cursor_y += font.metrics("linespace") * 1.25
                        continue

                    if cursor_x + w + H_STEP > WIDTH:
                        cursor_x = H_STEP
                        cursor_y += font.metrics("linespace") * 1.25

                    display_list.append((cursor_x, cursor_y, word, font))
                    cursor_x += w + font.measure(" ")
            elif tok.tag == "i":
                style="italic"
            elif tok.tag == "/i":
                style="roman"
            elif tok.tag == "b":
                weight="bold"
            elif tok.tag == "/b":
                weight="normal"


        self.max = cursor_y
        return display_list

    def draw(self):
        self.canvas.delete("all")
        for coord_x, coord_y, word, font in self.display_list:
            if coord_y > self.scroll + HEIGHT:
                continue
            if coord_y + V_STEP < self.scroll:
                continue
            self.canvas.create_text(coord_x, coord_y - self.scroll, text=word, anchor="nw", font=font)#, font=self.bi_times)

    def load(self, url: str):
        body = url.request()
        tokens = lex(body)
        self.display_list = self.layout(tokens)
        self.draw()

    def scrolldown(self, e):
        self.scroll += min(SCROLL_STEP, self.max - self.scroll)
        #self.scroll += SCROLL_STEP
        # print("Max: ", self.max, "Scroll: ", self.scroll)
        self.draw()

    def scrollup(self, e):
        self.scroll -= min(SCROLL_STEP, self.scroll)
        # self.scroll -= SCROLL_STEP
        print("Min: ", self.min, "Scroll: ", self.scroll)
        print(self.scroll)
        self.draw()