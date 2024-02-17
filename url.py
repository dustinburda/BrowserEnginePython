from dataclasses import dataclass

@dataclass
class URL:
    scheme: str
    host: str
    path: str

    @staticmethod
    def new_url(url: str):
        return URL(scheme="Hello", host="my name is", path="Dustin Burda")