class Widget:
    pass


class Text(Widget):
    def __init__(self, text: str, bold=False, italic=False):
        self.text = text
        self.bold = bold
        self.italic = italic

    def __repr__(self):
        a = (self.italic * 1 + self.bold * 2) * '*'
        return f"{a}{self.text}{a}"


class Header(Widget):
    def __init__(self, size: int, text: Widget):
        self.size = size
        self.text = text

    def __repr__(self):
        return f"{self.size * '#'} {self.text}"


class Link(Widget):
    def __init__(self, link: str, text: Widget):
        self.link = link
        self.text = text

    def __repr__(self):
        return f"[{self.text}]({self.link})"


class BlockQuote(Widget):
    def __init__(self, text: Widget):
        self.text = text

    def __repr__(self):
        return f"> {self.text}"
