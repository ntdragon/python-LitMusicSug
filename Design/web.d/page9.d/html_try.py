#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header

hd = {"loc": "Transfer Numbers"}
hdr = dict(page="Thansfer Song information to new songbook", today="Wednesday  March 06, 2019")

#block1 dicts

bks = dict(book1="Gather Comprehensive", book2="Gather Comprehensive2"  )


# block2 dicts
sbk = [
     {"num":1, "stitle":"Morning Praise Opening Dialog", "snum":1, "nsnum":1 },
     {"num":2, "stitle":"Morning Praise Morning Hymn", "snum":2, "nsnum":2 },
     {"num":3, "stitle":"Evensong Light Proclamation", "snum":9, "nsnum":9 },
     {"num":4, "stitle":"Evensong Evening Hymn", "snum":10, "nsnum":10 },
     {"num":5, "stitle":"Psalm 1: Happy Are They", "snum":18, "nsnum":18 },
     {"num":6, "stitle":"Psalm 4: Let Your Face Shine upon Us", "snum":19, "nsnum":19 },
     {"num":7, "stitle":"Canticle of Simeon/Luke 2:29-32", "snum":144, "nsnum":144 },
     {"num":8, "stitle":"Canticle of Mary/Luke 1:46-55", "snum":145, "nsnum":145 },
     {"num":9, "stitle":"Magnificat/Luke 1:46-55", "snum":146, "nsnum":146 },
     {"num":10, "stitle":"Holy Is Your Name/Luke 1:46-55", "snum":147, "nsnum":147 },
     {"num":11, "stitle":"Isaiah 12:2-3,4,6", "snum":148, "nsnum":148 },
     {"num":12, "stitle":"Revelation 19:1-7", "snum":149, "nsnum":149 },
     {"num":13, "stitle":"Song of the Three Children / Daniel 3:52-56", "snum":150, "nsnum":150 },
     {"num":14, "stitle":"Song of the Three Children / Daniel 3:52-57", "snum":151, "nsnum":151 },
     {"num":15, "stitle":"Song of the Three Children / Daniel 3:57-88", "snum":152, "nsnum":152 },
     {"num":16, "stitle":"Order of Mass", "snum":153, "nsnum":153 },
     {"num":17, "stitle":"Blessing and Sprinkling of Holy Water", "snum":154, "nsnum":154 },
     {"num":18, "stitle":"May We Be One", "snum":316, "nsnum":316 },
     {"num":19, "stitle":"O Come, O Come, Emmanuel", "snum":317, "nsnum":317 },
     {"num":20, "stitle":"People, Look East", "snum":318, "nsnum":318 },
     {"num":21, "stitle":"Walk in the Reign", "snum":319, "nsnum":319 }
]
# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "bks":bks,"sbk":sbk  }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page9.jhtml")


output = template.render(input_)

print(output)