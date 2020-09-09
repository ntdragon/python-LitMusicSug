#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header

hd = {"loc": "Songbook Listing - Alphabetic"}
hdr = dict(page="Alphabetic SOngbook Index", today="Wednesday  March 06, 2019")

#block1 dicts

cevt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive" )
dayt = dict(today="March 06, 2019", dmax="December 31,2020")

parts = dict(songnum="654", songtitle="All that is Hidden")

# block2 dicts
# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "cevt":cevt, "dayt":dayt,"parts":parts  }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page15.jhtml")


output = template.render(input_)

print(output)