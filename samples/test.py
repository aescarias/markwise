from markwise import *

my_md = MarkDown()

my_md.add_l([
    Header(2, Text("Welcome to Markwise!")),
    Header(4, Text("This is a markdown wrapper.", italic=True)),

    Text("This is a bold text", bold=True),
    Text("This is an italic text", italic=True),

    Text(f"Github: {Link('https://github.com/angelCarias/marquee', Text('A Link'))}"),

    BlockQuote(Text('"Self-doubt is the beginning of defeat"')),

    Line(),

    WidgetList([Mark(Text("Ordered List")), Indent(Mark(Link("https://google.com", Text("Search", bold=True))))]),

    WidgetList([NumberMark(Text("Unordered")),
                NumberMark(Text("Another Unordered")),
                Indent(Mark(BlockQuote(Text("List", italic=True))))]),

    CodeBlock(RawText("greet = lambda name: 'hello' + name"), lang="python")

])

my_md.write("test.md")

md2html(my_md, "test.html")
