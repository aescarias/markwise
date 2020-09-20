from markdown import markdown as mdconv
from .obj import MarkDown

class Conversion:
    def md2html(md: MarkDown, file=None):
        ht = mdconv(md.text)
        
        if file is not None:
            with open(file, "w") as f:
                f.write(ht)
        return ht
    
    def md2html_f(md, file=None):
        with open(md, "r") as f:
            ht = mdconv(f)
            
            if file is not None:
                with open(file, "w") as f:
                    f.write(ht)
       return ht
