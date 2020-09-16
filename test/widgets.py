class Widget:
	pass

class CodeBlock(Widget):
    def __init__(self, text: str, syntax_highlight=None):
        self.highlighters = ["py", "python", "json", "shell"]
        self.text = text
        self.syntax_highlight = syntax_highlight

        if self.syntax_highlight not in self.highlighters:
            self.syntax_highlight = None

    def __repr__(self):
        return f"""```{self.syntax_highlight}\n{self.text}```"""

class TableRow(Widget):
	def __init__(self, elements: list):
		self.elements = elements
		
	def __repr__(self):
		return '| ' + ' | '.join([elem for elem in self.elements]) + ' |'

class TableColumn(Widget):
	def __init__(self, columns: list, alignment: str = "left"):
		self.columns = columns
		self.alignment = alignment

		self.alignments = ["left", "right", "center"]
		
		if self.alignment not in self.alignments:
			self.alignment = "left"
			
	def __repr__(self):
		hline = ":----"

		if self.alignment == "center":
			hline = ":---: |"
		elif self.alignment == "right":
			hline = "----:"
		
		cols = '| ' + ' | '.join([col for col in self.columns]) + ' |'
		lines = '| ' + ' | '.join([hline for _ in self.columns]) + ' |'
		
		return f"{cols}\n{lines}"
