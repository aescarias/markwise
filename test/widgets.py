class HeadingLevelTooHigh(Exception):
    def __str__(self):
        return "Heading level must be lower or equal to 6."

class Header:
    def __init__(self, level: int, text: str):
        self.level = level
        self.text = text

    def __repr__(self):
        if self.level > 6:
            raise HeadingLevelTooHigh
        return f"{'#' * self.level} {self.text}"
