#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input


# tab and header
hd = {"loc": "Suggestions Selection"}
hdr = dict(page="Selection", today="Thursday  April 30, 2020")

#block1 dicts

evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent",  chmass="9:00", date="March 8, 2020")

opening = {
     { "masstime":"4:00", "songnum":"GC#382", "songtitle":"Again We Keep This Solemn Fast"},
     { "masstime":"9:00", "songnum":"GC#382", "songtitle":"Again We Keep This Solemn Fast"},
     {"masstime":"11:30", "songnum":"GC#3384", "songtitle":"Forty Days and Forty Nights"}
}

parts = {
     {"songpart":"Gloria", "songnum":"GC#194", "songtitle":"Mass of Creation - Gloria"},
     { "songpart":"RP", "songnum":"GC#085", "songtitle":"Psalm 91: Be with Me, Lord"},
     { "songpart":"GA", "songnum":"GC#194", "songtitle":"Mass of Creation - Gospel Acclimation"},
     { "songpart":"HH", "songnum":"GC#194", "songtitle":"Mass of Creation - Holy, Holy, Holy"},
     { "songpart":"MA", "songnum":"GC#198", "songtitle":"Mass of Creation - Memorial Acclamation B"},
     {"songpart":"AM", "songnum":"GC#202", "songtitle":"Mass of Creation - Amen"},
     {"songpart":"LG", "songnum":"GC#204", "songtitle":"Mass of Creation - Lamb of God"}
}

offer = {
     {"masstime":"4:00",  "songnum":"GC#707", "songtitle":"Guide My Feet"},
     {"masstime":"9:00", "songnum":"GC#707", "songtitle":"Guide My Feet"},
     {"masstime":"11:30",  "songnum":"GC#707", "songtitle":"Guide My Feet"}
]

com = {
     {"masstime":"4:00",  "songnum":"GC#642", "songtitle":"Jesus, Lead the Way"},
     {"masstime":"9:00", "songnum":"GC#642", "songtitle":"Jesus, Lead the Way"},
     {"masstime":"11:30",  "songnum":"GC#642", "songtitle":"Jesus, Lead the Way"}
}

commed = {
     {"masstime":"4:00",  "songnum":"GC#686", "songtitle":"Here I Am, Lord"},
     {"masstime":"9:00",  "songnum":"GC#686", "songtitle":"Here I Am, Lord"},
     {"masstime":"11:30", "songnum":"GC#686", "songtitle":"Here I Am, Lord"}
}

closing = {
     {"masstime":"4:00",  "songnum":"GC\#611", "songtitle":"On Eagle's Wings"},
     {"masstime":"9:00", "songnum":"GC\#689", "songtitle":"Out of Darkness"},
     {"masstime":"11:30",  "songnum":"GC\#574", "songtitle":"Lead Me, Guide Me"}
}



# collect all the dicts and such
input_ = {"evt":evt, "opening":opening, "parts":parts, "offer":offer, "com":com, 
     "commed":commed, "closing":closing,}

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("wknd-print_page.jhtml")


output = template.render(input_)

print(output)