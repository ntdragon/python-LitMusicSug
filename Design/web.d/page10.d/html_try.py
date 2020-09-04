#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header

hd = {"loc": "Add Songbook"}
hdr = dict(page="Add Songbook to database", today="Saturday  March 06, 2021")

#block1 dicts
ksongbooks = [
     {"num":0, "sbc":"GC", "sbi":"GC1",  "sbn":"Gather Comprehensive 1"},
    {"num":1, "sbc":"G3", "sbi":"GC3",  "sbn":"Gather Comprehensive 3"},
    {"num":2, "sbc":"SS", "sbi":"MDS1",  "sbn":"Music Director Song Book"},
    {"num":3, "sbc":"SS", "sbi":"LPS1",  "sbn":"Local Parish Song Book"},     
]
usongbooks = [
     {"num":0, "sbc":"BB", "sbi":"BByyyy",  "sbn":"Breaking Bread (for year yyyy)"},
     {"num":1, "sbc":"BFW", "sbi":"BFW",  "sbn":"By Flowing Waters"},
     {"num":2, "sbc":"CBW", "sbi":"CBW3",  "sbn":"Catholic Book of Worship III "},
     {"num":3, "sbc":"CCS", "sbi":"CCS",  "sbn":"Cantor/Congregation Series"},
     {"num":4, "sbc":"CH", "sbi":"CH",  "sbn":"The Collegeville Hymnal"},
     {"num":5, "sbc":"CPC2", "sbi":"CPC2",  "sbn":" Choral Praise Comprehensive, Second Edition"},
     {"num":6, "sbc":"CPD", "sbi":"CPD2",  "sbn":"Cantos del Pueblo de Dios, second edition"},
     {"num":7, "sbc":"FYC", "sbi":"FYC2",  "sbn":"Flor y Canto, Segunda Edición "},
     {"num":8, "sbc":"GC2", "sbi":"GC2",  "sbn":"Gather Comprehensive, Second Edition"},
     {"num":9, "sbc":"GP", "sbi":"GP2",  "sbn":" Glory \& Praise, Second Edition"},
     {"num":10, "sbc":"GPS", "sbi":"GPS3",  "sbn":"Glory and Praise, third edition"},
     {"num":11, "sbc":"HG", "sbi":"HG",  "sbn":"Hymns for the Gospels"},
     {"num":12, "sbc":"IH", "sbi":"IH",  "sbn":"Introit Hymns for the Church Year "},
     {"num":13, "sbc":"JS2", "sbi":"JS2",  "sbn":" Journeysongs, Second Edition"},
     {"num":14, "sbc":"LMGM", "sbi":"LMGM",  "sbn":"Lead Me, Guide Me "},
     {"num":15, "sbc":"LMGM2", "sbi":"LMGM2",  "sbn":"Lead Me, Guide Me second edition"},
     {"num":16, "sbc":"LP", "sbi":"LP",  "sbn":"A Lectionary Psalter: John Schiavone"},
     {"num":17, "sbc":"LPGC", "sbi":"LPGC",  "sbn":" Lectionary Psalms: Grail/Gelineau"},
     {"num":18, "sbc":"LPMG", "sbi":"LPMG",  "sbn":"Lectionary Psalms: Michel Guimont"},
     {"num":19, "sbc":"MI", "sbi":"MIyyyy",  "sbn":"Music Issue (for year yyyy)"},
     {"num":20, "sbc":"NTY", "sbi":"NTY",  "sbn":"Never Too Young"},
     {"num":21, "sbc":"OIF", "sbi":"OIF",  "sbn":" One in Faith"},
     {"num":22, "sbc":"OFUV", "sbi":"OFUV",  "sbn":"One Faith, Una Voz"},
     {"num":23, "sbc":"PC", "sbi":"PC",  "sbn":"Psalms for the Cantor"},
     {"num":24, "sbc":"PCY", "sbi":"PCY",  "sbn":"Psalms for the Church Year"},
     {"num":25, "sbc":"PFS", "sbi":"PFS",  "sbn":" Psalms for Feasts and Seasons (1990, The Liturgical Press)"},
     {"num":26, "sbc":"PJ", "sbi":"PJ",  "sbn":"Psalms for the Journey (1991, The Liturgical Press)"},
     {"num":27, "sbc":"PMB", "sbi":"PMB",  "sbn":"Peoples Mass Book (2003, WLP)"},
     {"num":28, "sbc":"PRM", "sbi":"PRM",  "sbn":"Psalms and Ritual Music (various years, WLP) "},
     {"num":29, "sbc":"PSL", "sbi":"PSL",  "sbn":"Psallité (2005,2006,2007, The Liturgical Press)"},
     {"num":30, "sbc":"PST", "sbi":"PST",  "sbn":"Psaltery (1990, GIA)"},
     {"num":31, "sbc":"RA", "sbi":"RA",  "sbn":"Respond & Acclaim (annual psalmody resource, OCP)"},
     {"num":32, "sbc":"RS", "sbi":"RS",  "sbn":"RitualSong (1996, GIA) "},
     {"num":33, "sbc":"RUAS", "sbi":"RUAS",  "sbn":"Rise Up and Sing, Second Edition (children’s hymnal; 2000, OCP)"},
     {"num":34, "sbc":"RYA", "sbi":"RYA",  "sbn":"Responde y Aclama (Spanish annual psalmody resource, OCP)"},
     {"num":35, "sbc":"SI", "sbi":"SI",  "sbn":"Songs of Israel (1971, 1983, GIA)"},
     {"num":36, "sbc":"SMM", "sbi":"SMM",  "sbn":"Service Music for the Mass (1987-89, WLP) "},
     {"num":37, "sbc":"SO", "sbi":"SO",  "sbn":"Sing Out! (1994, WLP) "},
     {"num":38, "sbc":"SP", "sbi":"SP",  "sbn":"Singing the Psalms (1995, 1996, 1997, 1999, OCP)"},
     {"num":39, "sbc":"SPS", "sbi":"SPS",  "sbn":"Spirit and Song OCP, 2013"},
     {"num":40, "sbc":"SS", "sbi":"SS",  "sbn":"Sacred Song (seasonal resource, The Liturgical Press) "},
     {"num":41, "sbc":"SS1", "sbi":"SS1",  "sbn":"Spirit & Song 1 (1999, OCP)"},
     {"num":42, "sbc":"SS2", "sbi":"SS2",  "sbn":"Spirit & Song 2 (2005, OCP)"},
     {"num":43, "sbc":"WC", "sbi":"WC",  "sbn":"We Celebrate  (2011, WLP)"},
     {"num":44, "sbc":"WS", "sbi":"WS",  "sbn":" Word and Song (annual resource, WLP)"},
     {"num":45, "sbc":"WOR", "sbi":"WOR",  "sbn":"Worship, Third Edition (1986, GIA) "},
     {"num":46, "sbc":"WOR4", "sbi":"WOR4",  "sbn":"Worship, Fourth Edition (GIA, 2011)"},
     {"num":47, "sbc":"XXXX", "sbi":"XXXX",  "sbn":"None of the Above"}
]



# block2 dicts
# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "ksongbooks":ksongbooks, "usongbooks":usongbooks }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page10.jhtml")


output = template.render(input_)

print(output)