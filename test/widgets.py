from exceptions import HeadingLevelTooHigh

class Header:
    def __init__(self, level: int, text: str):
        self.level = level if level != 0 else 1
        self.text = text

    def __repr__(self):
        if self.level > 6:
            raise HeadingLevelTooHigh
        return f"{'#' * self.level} {self.text}"
