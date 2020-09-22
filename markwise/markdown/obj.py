from .md2html import md2html


class MarkDown:
    def __init__(self):
        self.widgets = []
        self.text = ""

    def write(self, filename):
        self.update()
        with open(filename, "w") as f:
            f.write(self.text)

    def update(self):
        self.text = "\n\n".join([repr(a) for a in self.widgets])

    def add_l(self, l):
        self.widgets += l
        self.update()
        return self

    def add(self, o):
        self.widgets.append(o)
        self.update()
        return self

    def to_html(self, file=None):
        return md2html(self, file)
