class MarkDown:
    def __init__(self):
        self.text = ""
        self.widgets = []

    def write(self, filename):
        with open(filename, "w") as f:
            f.write(self.text)
