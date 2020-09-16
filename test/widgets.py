from .exceptions import HeadingLevelTooHigh


class CodeBlock:
    def __init__(self, text: str, syntax_highlight=None):
        self.highlighters = ["py", "python", "json", "shell"]
        self.text = text
        self.syntax_highlight = syntax_highlight

        if self.syntax_highlight not in self.highlighters:
            self.syntax_highlight = None

    def __repr__(self):
        return f"""```{self.syntax_highlight}\n{self.text}```"""


class Header:
    def __init__(self, level: int, text: str):
        self.level = level if level != 0 else 1
        self.text = text

    def __repr__(self):
        if self.level > 6:
            raise HeadingLevelTooHigh
        return f"{'#' * self.level} {self.text}"
