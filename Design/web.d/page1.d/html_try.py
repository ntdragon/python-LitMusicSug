#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header
hd = {"loc": "Greetings"}
hdr = dict(page="Greeting ", today="Wednesday  March 06, 2019")

#block1 dicts

# block2 dicts
# Event Information
cevt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive",mstheme="MC", themename="Mass of Creation" )
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
events = [
    {"num":1 ,"evtid":"A1", "evtname":"First Sunday in Advent"},
    {"num":2 ,"evtid":"A2", "evtname":"Second Sunday in Advent"},
    {"num":3 ,"evtid":"A3", "evtname":"Third Sunday in Advent"},
    {"num":4 ,"evtid":"A4", "evtname":"Fourth Sunday in Advent"},
    {"num":5 ,"evtid":"O1", "evtname":"First Sunday in Ordinary Time"},
    {"num":6 ,"evtid":"O2", "evtname":"Second Sunday in Ordinary Time"},
    {"num":7 ,"evtid":"O3", "evtname":"Third Sunday in Ordinary Time"},
    {"num":8 ,"evtid":"O4", "evtname":"Fourth Sunday in  Ordinary Time"},
    {"num":9 ,"evtid":"O5", "evtname":"Fifth Sunday in  Ordinary Time"},
    {"num":10 ,"evtid":"O6", "evtname":"Sixth Sunday in  Ordinary Time"},
    {"num":11 ,"evtid":"O7", "evtname":"Seventh Sunday in  Ordinary Time"},
    {"num":12 ,"evtid":"O8", "evtname":"Eighth Sunday in  Ordinary Time"},
    {"num":13 ,"evtid":"O9", "evtname":"Ninth Sunday in  Ordinary Time"},
    {"num":14 ,"evtid":"O10", "evtname":"Tenth Sunday in  Ordinary Time"},
    {"num":15 ,"evtid":"O11", "evtname":"Eleventh Sunday in  Ordinary Time"},
    {"num":16 ,"evtid":"O12", "evtname":"Twelth Sunday in  Ordinary Time"},
    {"num":17 ,"evtid":"O13", "evtname":"Thirteenth Sunday in  Ordinary Time"},
    {"num":18 ,"evtid":"O14", "evtname":"Fourteenth Sunday in  Ordinary Time"},
    {"num":19 ,"evtid":"O15", "evtname":"Fifteenth Sunday in  Ordinary Time"},
    {"num":20 ,"evtid":"O16", "evtname":"Sixteenth Sunday in  Ordinary Time"},
    {"num":21 ,"evtid":"O17", "evtname":"Seventeenth Sunday in  Ordinary Time"},
    {"num":22 ,"evtid":"O18", "evtname":"Eighteenth Sunday in  Ordinary Time"},
    {"num":23 ,"evtid":"O19", "evtname":"Nineteenthth Sunday in  Ordinary Time"},
    {"num":24 ,"evtid":"O20", "evtname":"Twentieth Sunday in  Ordinary Time"},
    {"num":25 ,"evtid":"O21", "evtname":"Twenty First Sunday in  Ordinary Time"},
    {"num":26 ,"evtid":"O22", "evtname":"Twenty Second Sunday in  Ordinary Time"},
    {"num":27 ,"evtid":"O23", "evtname":"Twenty Third Sunday in  Ordinary Time"},
    {"num":28 ,"evtid":"O24", "evtname":"Twenty Fourtth Sunday in  Ordinary Time"},
    {"num":29 ,"evtid":"O25", "evtname":"Twenty Fifth Sunday in  Ordinary Time"},
    {"num":30 ,"evtid":"O26", "evtname":"Twenty Sixth Sunday in  Ordinary Time"},
    {"num":31 ,"evtid":"O27", "evtname":"Twenty Seventh Sunday in  Ordinary Time"},
    {"num":32 ,"evtid":"O28", "evtname":"Twenty Eighth Sunday in  Ordinary Time"},
    {"num":33 ,"evtid":"O29", "evtname":"Twenty Ninth Sunday in  Ordinary Time"},
    {"num":34 ,"evtid":"O30", "evtname":"Thirtieth Sunday in  Ordinary Time"},
    {"num":35 ,"evtid":"O31", "evtname":"Thirty First Sunday in  Ordinary Time"},
    {"num":36 ,"evtid":"O32", "evtname":"Thirty Second Sunday in  Ordinary Time"},
    {"num":37 ,"evtid":"O33", "evtname":"Thirty Third Sunday in  Ordinary Time"},
    {"num":38 ,"evtid":"O34", "evtname":"Thirty Fourth Sunday in  Ordinary Time"},
    {"num":39 ,"evtid":"L1", "evtname":"First Sunday in  Lent"},
    {"num":40 ,"evtid":"L2", "evtname":"Second Sunday in  Lent"},
    {"num":41 ,"evtid":"L3", "evtname":"Third Sunday in  Lent"},
    {"num":42 ,"evtid":"L4", "evtname":"Fourth Sunday iin Lent"},
    {"num":43 ,"evtid":"L5", "evtname":"Palm Sunday"},
    {"num":44 ,"evtid":"E2", "evtname":"Second Sunday in  Easter Time"},
    {"num":45 ,"evtid":"E3", "evtname":"Third Sunday in  Easter Time"},
    {"num":46 ,"evtid":"E4", "evtname":"Fourth Sunday in  Easter Time"},
    {"num":47 ,"evtid":"E5", "evtname":"Fifth Sunday in  Easter Time"},
    {"num":48 ,"evtid":"E6", "evtname":"Sixth Sunday in  Easter Time"},
    {"num":49 ,"evtid":"E7", "evtname":"Seventh Sunday in  Easter Time"},
    {"num":50 ,"evtid":"D1", "evtname":"Christmas"},
    {"num":51 ,"evtid":"D2", "evtname":"Easter"},
    {"num":52 ,"evtid":"H1", "evtname":"Holy Family"},
    {"num":53 ,"evtid":"H2", "evtname":"Baptism of the Lord"},
    {"num":54 ,"evtid":"H3", "evtname":"Ash Wednesday"},
    {"num":55 ,"evtid":"H4", "evtname":"Pentecost"},
    {"num":56 ,"evtid":"MW1", "evtname":"Wedding"},
    {"num":57 ,"evtid":"MF1", "evtname":"Funeral"},
    {"num":99 ,"evtid":"N00", "evtname":"Other"}
]
# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "theme":theme, "events":events, "cevt":cevt, "dayt":dayt }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page1.jhtml")


output = template.render(input_)

print(output)