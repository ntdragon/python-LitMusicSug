#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import subprocess

# page input


# tab and header
hd = {"loc": "Suggestions Selection"}
hdr = dict(page="Selection", today="Thursday  April 30, 2020")

#block1 dicts

evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent",  chmass="9:00", date="March 8, 2020")

opening = [
     dict(masstime="\ 4:00", songnum="GC\#382", songtitle="Again We Keep This Solemn Fast"),
     dict(masstime="\ 9:00", songnum="GC\#382", songtitle="Again We Keep This Solemn Fast"),
     dict(masstime="11:30", songnum="GC\#384", songtitle="Forty Days and Forty Nights")
]

parts = [
     dict(songpart="Gloria", songnum="GC\#194", songtitle="Mass of Creation - Gloria"),
     dict(songpart="RP", songnum="GC\#085", songtitle="Psalm 91: Be with Me, Lord"),
     dict(songpart="GA", songnum="GC\#194", songtitle="Mass of Creation - Gospel Acclimation"),
     dict(songpart="HH", songnum="GC\#194", songtitle="Mass of Creation - Holy, Holy, Holy"),
     dict(songpart="MA", songnum="GC\#198", songtitle="Mass of Creation - Memorial Acclamation B"),
     dict(songpart="AM", songnum="GC\#202", songtitle="Mass of Creation - Amen"),
     dict(songpart="LG", songnum="GC\#204", songtitle="Mass of Creation - Lamb of God")
]

offer = [
     dict(masstime="4:00",  songnum="GC\#707", songtitle="Guide My Feet"),
     dict(masstime="9:00", songnum="GC\#707", songtitle="Guide My Feet"),
     dict(masstime="11:30",  songnum="GC\#707", songtitle="Guide My Feet")
]

com = [
     dict(masstime="4:00",  songnum="GC\#642", songtitle="Jesus, Lead the Way"),
     dict(masstime="9:00", songnum="GC\#642", songtitle="Jesus, Lead the Way"),
     dict(masstime="11:30",  songnum="GC\#642", songtitle="Jesus, Lead the Way")
]

commed = [
     dict(masstime="4:00",  songnum="GC\#686", songtitle="Here I Am, Lord"),
     dict(masstime="9:00",  songnum="GC\#686", songtitle="Here I Am, Lord"),
     dict(masstime="11:30", songnum="GC\#686", songtitle="Here I Am, Lord")
]

closing = [
     dict(masstime="4:00",  songnum="GC\#611", songtitle="On Eagle's Wings"),
     dict(masstime="9:00", songnum="GC\#689", songtitle="Out of Darkness"),
     dict(masstime="11:30",  songnum="GC\#574", songtitle="Lead Me, Guide Me")
]



# collect all the dicts and such
input_ = {"evt":evt, "opening":opening, "parts":parts, "offer":offer, "com":com, 
     "commed":commed, "closing":closing,}

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("wknd-print_page1.jtex")


output = template.render(input_)
with open('page.tex', mode='w') as file_object:
     print(output, file=file_object)
subprocess.run(["pdflatex","page.tex"])
#subprocess.run(["lp","page.pdf"])
