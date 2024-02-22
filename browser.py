from dataclasses import dataclass
import tkinter as tk
from main import WIDTH, HEIGHT
from url import lex

H_STEP: int = 13
V_STEP: int = 18


@dataclass
class Browser:
    window: 'tk-window'
    canvas: 'tk-canvas'
    display_list: list[tuple[int, int, str]]
    scroll: int

    @staticmethod
    def new_browser():
        window = tk.Tk()
        canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
        canvas.pack()
        return Browser(window=window, canvas=canvas, display_list = [], scroll=0)

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
        for coord_x, coord_y, c in self.display_list:
            self.canvas.create_text(coord_x, coord_y, text=c)

    def load(self, url: str):
        body = url.request()
        text = lex(body)
        self.display_list = self.layout(text)
        self.draw()


