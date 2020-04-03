#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header
hd = {"loc": "Greetings"}
hdr = dict(page="Greeting ", today="Wednesday  March 06, 2019")

#block1 dicts

# block2 dicts
evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive",mstheme="MC", themename="Mass of Creation" )
dayt = dict(today="March 06, 2020", dmax="December 31,2021")
theme = [
    {"num":1 ,"mstid":"MC", "mstname":"Mass of Creation"},
    {"num":0, "mstid":"OM", "mstname":"Order of Mass"},
    {"num":2, "mstid":"MJP", "mstname":"Mass of Joy and Peace"},
    {"num":3, "mstid":"MNW", "mstname":"Mass for a New World"},
    {"num":4, "mstid":"SM", "mstname":"Storrington Mass"},
    {"num":5, "mstid":"BML", "mstname":"Black Mountain Liturgy"},
    {"num":6, "mstid":"MAA", "mstname":"Mass form Age to Age"},
    {"num":7, "mstid":"GM", "mstname":"Glendough Mass"},
    {"num":8, "mstid":"MP", "mstname":"Missa Pacem"},
    {"num":9, "mstid":"UM", "mstname":"Unity Mass"},
    {"num":10, "mstid":"MUSE", "mstname":"Misa Una Sante Fe / One Holy Faith Mass"},
    {"num":11, "mstid":"CM", "mstname":"Cantus Missae"},
    {"num":12, "mstid":"SEM", "mstname":"Service Music"},
    {"num":20, "mstid":"LSS", "mstname":"Song Sheets"}
]

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "theme":theme, "evt":evt, "dayt":dayt }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("page1.jhtml")


output = template.render(input_)

print(output)