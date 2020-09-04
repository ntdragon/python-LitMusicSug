#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header

hd = {"loc": "Add Suggestion"}
hdr = dict(page="Add Suggestion to database", today="Wednesday  March 06, 2019")

#block1 dicts

parts = dict(searchString="Alabaré/Alabaré, We Sing the Praises of Our God")

ksongbooks = [
     {"num":0, "sbc":"GC", "sbi":"GC1",  "sbn":"Gather Comprehensive", "snum":"542"},
    {"num":1, "sbc":"G3", "sbi":"GC3",  "sbn":"Gather Comprehensive 3", "snum":" "},
    {"num":2, "sbc":"SS", "sbi":"MDS1",  "sbn":"Music Director Song Book", "snum":" "},
    {"num":3, "sbc":"SS", "sbi":"LPS1",  "sbn":"Local Parish Song Book", "snum":" "},     
]
# block2 dicts
# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "ksongbooks":ksongbooks, "parts":parts  }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page7.jhtml")


output = template.render(input_)

print(output)