#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input


# tab and header
hd = {"loc": "Suggestions Selection"}
hdr = dict(page="Selection", today="Thursday  April 30, 2020")

#block1 dicts

evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent",  chmass="9:00", date="March 8, 2020")

songs = {
     {"nm":"2", "masstime":"4:00 & 9:00", "songpart":"Opening", "songnum":"GC#382", "songtitle":"Again We Keep This Solemn Fast"},
     {"nm":"1","masstime":"11:30", "songpart":"Opening", "songnum":"GC#3384", "songtitle":"Forty Days and Forty Nights"}
     {"nm":"3", "masstime":"all", "songpart":"Gloria", "songnum":"GC#194", "songtitle":"Mass of Creation - Gloria"},
     {"nm":"3", "masstime":"all", "songpart":"RPsalm", "songnum":"GC#085", "songtitle":"Psalm 91: Be with Me, Lord"},
     {"nm":"3", "masstime":"all", "songpart":"Gacc", "songnum":"GC#194", "songtitle":"Mass of Creation - Gospel Acclimation"},
     {"nm":"3", "masstime":"all", "songpart":"Offer", "songnum":"GC#707", "songtitle":"Guide My Feet"},
     {"nm":"3", "masstime":"all", "songpart":"Holy", "songnum":"GC#194", "songtitle":"Mass of Creation - Holy, Holy, Holy"},
     {"nm":"3", "masstime":"all", "songpart":"MA", "songnum":"GC#198", "songtitle":"Mass of Creation - Memorial Acclamation B"},
     {"nm":"3", "masstime":"all", "songpart":"A", "songnum":"GC#202", "songtitle":"Mass of Creation - Amen"},
     {"nm":"3", "masstime":"all", "songpart":"LoG", "songnum":"GC#204", "songtitle":"Mass of Creation - Lamb of God"},
     {"nm":"3", "masstime":"all", "songpart":"Comm", "songnum":"GC#642", "songtitle":"Jesus, Lead the Way"},
     {"nm":"3", "masstime":"all", "songpart":"CommMed", "songnum":"GC#686", "songtitle":"Here I Am, Lord"},
     {"nm":"1", "masstime":"all", "songpart":"Closing", "songnum":"GC#611", "songtitle":"On Eagle's Wings"},
     {"nm":"1", "masstime":"all", "songpart":"Closing", "songnum":"GC#689", "songtitle":"Out of Darkness"},
     {"nm":"1", "masstime":"all", "songpart":"Closing", "songnum":"GC#574", "songtitle":"Lead Me, Guide Me"}
}


# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "evt":evt, "kpsalms":kpsalms,   "ksongs":ksongs, "parts":parts}

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("print_page.jhtml")


output = template.render(input_)

print(output)