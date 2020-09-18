from markdown import markdown as mdconv
from .obj import MarkDown


def md2html(md: MarkDown, file=None):
    ht = mdconv(md.text)
    if file is not None:
        with open(file, "w") as f:
            f.write(ht)

    return ht
