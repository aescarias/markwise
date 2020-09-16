class Bold:
    def __init__(self, text: str):
        self.text = text
        
    def __repr__(self):
        return f"**{self.text}**"

class Italic:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return f"*{self.text}*"

class Strikeout:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return f"~~{self.text}~~"

