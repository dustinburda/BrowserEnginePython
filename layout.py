H_STEP:      int = 13
V_STEP:      int = 18

from elements import Text, Tag
import tkinter
from main import WIDTH, HEIGHT

class Layout:
    def __init__(self, tokens):
        self.display_list = []
        self.cursor_x = H_STEP
        self.cursor_y = V_STEP
        self.weight = "normal"
        self.style = "roman"
        self.size = 16

        for tok in tokens:
            self.token(tok)

        self.max_scroll = self.cursor_y

    def token(self, tok: str):
        if isinstance(tok, Text):
            for word in tok.text.split():
                self.word(word)
        elif tok.tag == "i":
            self.style = "italic"
        elif tok.tag == "/i":
            self.style = "roman"
        elif tok.tag == "b":
            self.weight = "bold"
        elif tok.tag == "/b":
            self.weight = "normal"
        elif tok.tag == "small":
            self.size -= 2
        elif tok.tag == "/small":
            self.size += 2
        elif tok.tag == "big":
            self.size += 4
        elif tok.tag == "/big":
            self.size -= 4

    def word(self, word: str):
        font = tkinter.font.Font(size=self.size, weight=self.weight, slant=self.style)
        w = font.measure(word)

        if word == "\n":
            self.cursor_x = H_STEP
            self.cursor_y += font.metrics("linespace") * 1.25
            return

        if self.cursor_x + w + H_STEP > WIDTH:
            self.cursor_x = H_STEP
            self.cursor_y += font.metrics("linespace") * 1.25

        self.display_list.append((self.cursor_x, self.cursor_y, word, font))
        self.cursor_x += w + font.measure(" ")