#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# document input

#header information
parish = dict(name="St. Roch Church")
wknd = dict(date="11/20/2016", title="Our Lord Jesus Christ, King of the Universe", ltyr="C", choir="Sun  9:00 AM")

#Mass Songs information
#Mass 1
mass[1]["day"] = "Sat"
mass[1]["time"] = "4:00 PM"
mass[1]["OS"]["num"] = "GC\#443"
mass[1]["OS"]["title"] = "Alleluia, Give Thanks"
mass[1]["Gloria"]["num"] = "(Sheet Music)"
mass[1]["Gloria"]["title"] = "Mass of Creation"
mass[1]["RS"]["num"] = "GC\#121"
mass[1]["RS"]["title"] = " I Was Glad (vss. 1-3 only) (Theresa W.)"
mass[1]["GA"]["num"] = "GC\#258"
mass[1]["GA"]["title"] = "Celtic Alleluia"
mass[1]["GA"]["verse1"] = " ``Blessed is he who comes in the name of the Lord!"
mass[1]["GA"]["verse2"] = "Blessed is the kingdom of our father David that is come!'' "
mass[1]["Of"]["num"] = "GC\#635"
mass[1]["Of"]["title"] = "The King of Love My Shepherd Is"
mass[1]["Holy"]["num"] = "(Sheet Music)"
mass[1]["Holy"]["title"] = "Mass of Creation"
mass[1]["acc"] = "B"
mass[1]["MA"]["num"] = "(Sheet Music)"
mass[1]["MA"]["title"] = "Mass of Creation"
mass[1]["Amen"]["num"] = "(Sheet Music)"
mass[1]["Amen"]["title"] = "Mass of Creation"
mass[1]["LG"]["num"] = "(Sheet Music)"
mass[1]["LG"]["title"] = "Mass of Creation"
mass[1]["CS"][1]["num"] = "GC\#593"
mass[1]["CS"][1]["title"] = "We Remember "
mass[1]["CS"][2]["num"] = "GC\#593"
mass[1]["CS"][2]["title"] = "We Remember "
mass[1]["CM"]["num"] = " GC\#418"
mass[1]["CM"]["title"] = " Jesus the Lord "
mass[1]["ES"]["num"] = "GC\#485"
mass[1]["ES"]["title"] = "Crown Him With Many Crowns"

#Mass2
mass[2]["day"] = "Sun"
mass[2]["time"] = "9:00 AM"
mass[2]["OS"]["num"] = "GC\#443"
mass[2]["OS"]["title"] = "Alleluia, Give Thanks"
mass[2]["Gloria"]["num"] = "(Sheet Music)"
mass[2]["Gloria"]["title"] = "Mass of Creation"
mass[2]["RS"]["num"] = "GC\#121"
mass[2]["RS"]["title"] = " I Was Glad (vss. 1-3 only) (Theresa W.)"
mass[2]["GA"]["num"] = "GC\#258"
mass[2]["GA"]["title"] = "Celtic Alleluia"
mass[2]["GA"]["verse1"] = " ``Blessed is he who comes in the name of the Lord!"
mass[2]["GA"]["verse2"] = "Blessed is the kingdom of our father David that is come!'' "
mass[1]["Of"]["num"] = "GC\#635"
mass[1]["Of"]["title"] = "The King of Love My Shepherd Is"
mass[2]["Holy"]["num"] = "(Sheet Music)"
mass[2]["Holy"]["title"] = "Mass of Creation"
mass[2]["acc"] = "B"
mass[2]["MA"]["num"] = "(Sheet Music)"
mass[2]["MA"]["title"] = "Mass of Creation"
mass[2]["Amen"]["num"] = "(Sheet Music)"
mass[2]["Amen"]["title"] = "Mass of Creation"
mass[2]["LG"]["num"] = "(Sheet Music)"
mass[2]["LG"]["title"] = "Mass of Creation"
mass[2]["CS"][1]["num"] = "GC\#593"
mass[2]["CS"][1]["title"] = "We Remember "
mass[2]["CS"][2]["num"] = "GC\#593"
mass[2]["CS"][2]["title"] = "We Remember "
mass[2]["CM"]["num"] = " GC\#418"
mass[2]["CM"]["title"] = " Jesus the Lord "
mass[2]["ES"]["num"] = "GC\#794"
mass[2]["ES"]["title"] = "Ye Watchers and Ye Holy Ones "

#Mass3
mass[3]["day"] = "Sun"
mass[3]["time"] = "11:30 AM"
mass[3]["OS"]["num"] = "GC\#487"
mass[3]["OS"]["title"] = "Rejoice, the Lord is King"
mass[3]["Gloria"]["num"] = "(Sheet Music)"
mass[3]["Gloria"]["title"] = "Mass of Creation"
mass[3]["RS"]["num"] = "GC\#121"
mass[3]["RS"]["title"] = " I Was Glad (vss. 1-3 only) (Theresa W.)"
mass[3]["GA"]["num"] = "GC\#258"
mass[3]["GA"]["title"] = "Celtic Alleluia"
mass[3]["GA"]["verse1"] = " ``Blessed is he who comes in the name of the Lord!"
mass[3]["GA"]["verse2"] = "Blessed is the kingdom of our father David that is come!'' "
mass[1]["Of"]["num"] = "GC\#635"
mass[1]["Of"]["title"] = "The King of Love My Shepherd Is"
mass[3]["Holy"]["num"] = "(Sheet Music)"
mass[3]["Holy"]["title"] = "Mass of Creation"
mass[3]["acc"] = "B"
mass[3]["MA"]["num"] = "(Sheet Music)"
mass[3]["MA"]["title"] = "Mass of Creation"
mass[3]["Amen"]["num"] = "(Sheet Music)"
mass[3]["Amen"]["title"] = "Mass of Creation"
mass[3]["LG"]["num"] = "(Sheet Music)"
mass[3]["LG"]["title"] = "Mass of Creation"
mass[3]["CS"][1]["num"] = "GC\#593"
mass[3]["CS"][1]["title"] = "We Remember "
mass[3]["CS"][2]["num"] = "GC\#593"
mass[3]["CS"][2]["title"] = "We Remember "
mass[3]["CM"]["num"] = " GC\#418"
mass[3]["CM"]["title"] = " Jesus the Lord "
mass[3]["ES"]["num"] = "GC\#547"
mass[3]["ES"]["title"] = "Sing of the Lord's Goodness"


# collect all the dicts and such
input_ = {"parish":parish, "wknd":wknd, "mass":mass }

env = Environment(loader = FileSystemLoader("."))
template=env.get_template("Weekend_Music.jtex")


output = template.render(input_)

print(output)