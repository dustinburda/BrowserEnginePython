import socket
from dataclasses import dataclass
from elements import Text, Tag

@dataclass
class URL:
    scheme: str
    host: str
    path: str

    @staticmethod
    def new_url(url: str):
        scheme, url = url.split("://", 1)

        if "/" not in url:
            url = url + "/"

        host, url = url.split("/", 1)
        path = "/" + url

        return URL(scheme=scheme, host=host, path=path)

    def request(self) -> str:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        s.connect((self.host, 80))

        s.send(f"GET {self.path} HTTP/1.0\r\nHost: {self.host}\r\n\r\n".encode("utf8"))


        response = s.makefile("r", encoding="utf8", newline="\r\n")

        statusline = response.readline()
        version, status, explanation = statusline.split(" ", 2)

        response_headers = {}
        while True:
            line = response.readline()
            if line == "\r\n":
                break
            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value.strip()

        body = response.read()
        s.close()

        return body


def lex(body: str):
    in_tag = False
    out = []
    buffer = ""
    for c in body:
        if c == "<":
            in_tag = True
            if buffer:
                out.append(Text(buffer))
            buffer = ""
        elif c == ">":
            in_tag = False
            out.append(Tag(buffer))
            buffer = ""
        else:
            buffer += c
    if not in_tag and buffer:
        out.append(Tag(buffer))
    return out









