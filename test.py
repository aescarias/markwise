from marquee import *

my_md = MarkDown()

my_md.add_l([
    Header(2, Text("Welcome to Marquee!")),
    Header(4, Text("This is a markdown wrapper.", italic=True))])

my_md.add_l([
    Text("This is a bold text", bold=True),
    Text("This is an italic text", italic=True)])

my_md.add(Text(f"Github: {Link('https://github.com/angelCarias/marquee', Text('A Link'))}"))

my_md.add(BlockQuote(Text('"Self-doubt is the beginning of defeat"')))

my_md.write("test.md")
