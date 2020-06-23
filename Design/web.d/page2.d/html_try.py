#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header
hd = {"loc": "Input NPM Suggestions"}
hdr = dict(page="Input NPM Suggestions", today="Wednesday  March 06, 2019")

#block1 dicts

# block2 dicts
evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive" )
dayt = dict(today="March 06, 2019", dmax="December 31,2020")

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "evt":evt, "dayt":dayt }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page2.jhtml")


output = template.render(input_)

print(output)