import socket
from dataclasses import dataclass

@dataclass
class URL:
    scheme: str
    host: str
    path: str

    @classmethod
    def new_url(url: str):
        scheme, url = url.split("://", 1)

        if "/" not in url:
            url = url + "/"

        host, url = url.split("/", 1)
        path = "/" + url

        return URL(scheme=scheme, host=host, path=path)

    def request(self):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
        s.connect((self.host, 80))

        s.send(f"GET {self.path} HTTP/1.0\r\nHost: {self.host}\r\n\r\n".encode("utf8"))







