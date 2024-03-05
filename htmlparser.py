from dataclasses import dataclass


class Text:
    def __init__(self, text, parent):
        self.text = text
        self.parent = parent
        self.children = [] # textnodes never have children

class Element:
    def __init__(self, tag, parent):
        self.tag = tag
        self.parent = parent
        self.children = []

class HTMLParser:
    def __init__(self, body):
        self.body = body
        self.unfinished = []