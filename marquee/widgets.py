class Widget:
    def __init__(self):
        pass


class Header:
    def __init__(self, size: int, text: str):
        self.size = size
        self.text = text

    def __repr__(self):
        return f"{self.size * '#'} {self.text}"
