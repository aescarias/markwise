from marquee import *

my_md = MarkDown()

my_md.add_l([
    Header(2, Text("Welcome to Marquee!")),
    Header(4, Text("This is a markdown wrapper.", italic=True)),

    Text("This is a bold text", bold=True),
    Text("This is an italic text", italic=True),

    Text(f"Github: {Link('https://github.com/angelCarias/marquee', Text('A Link'))}"),

    BlockQuote(Text('"Self-doubt is the beginning of defeat"')),

    OrderedList([Text("Ordered List"), Link("https://google.com", Text("Search", bold=True))]),

    UnorderedList([Text("Unordered"), BlockQuote(Text("List", italic=True))]),

])

my_md.write("test.md")
