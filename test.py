from marquee import *

my_md = MarkDown()
my_md.add_l([Header(2, "Welcome to Marquee!"), Header(4, "This is a markdown wrapper.")])
my_md.write("test.md")
