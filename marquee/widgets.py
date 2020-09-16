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


class RawText(Widget):
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return self.text


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


class UnorderedList(Widget):
    def __init__(self, widgets):
        self.widgets = widgets

    def __repr__(self):
        return "\n".join("* " + repr(a) for a in self.widgets)


class OrderedList(Widget):
    def __init__(self, widgets):
        self.widgets = widgets

    def __repr__(self):
        return "\n".join(f"{i + 1}. " + repr(a) for i, a in enumerate(self.widgets))


class CodeBlock:
    def __init__(self, text: RawText, lang=None):
        self.highlighters = ["py", "python", "json", "shell"]
        self.text = text
        self.lang = lang

        if self.lang not in self.highlighters:
            self.lang = None

    def __repr__(self):
        return f"""```{self.lang if self.lang else ""}\n{self.text}\n```"""
