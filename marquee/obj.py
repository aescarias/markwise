class MarkDown:
    def __init__(self):
        self.widgets = []

    def write(self, filename):
        text = "\n\n".join([repr(a) for a in self.widgets])
        with open(filename, "w") as f:
            f.write(text)

    def add_l(self, l):
        self.widgets += l
        return self

    def add(self, o):
        self.widgets.append(o)
        return self
