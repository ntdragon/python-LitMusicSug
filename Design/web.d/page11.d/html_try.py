#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input
page = dict(action="single", user="Edward Birdsall")

# tab and header

hd = {"loc": "Calendars"}
hdr = dict(page="Update Calendars", today="Saturday  March 02, 2019")

#block1 dicts

cevt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive" )
dayt = dict(today="March 06, 2019", dmax="December 31,2020")

parts = dict(songnum="654", songtitle="All that is Hidden")

days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

# devt is intended to hold the number of events for the day to be used in the template with an if or for but can't get to work right now
tdy = []
for i in range(0, 35,1):
     tdy.append({"bgtclr":"white","bgeclr":"white", "dnum":0, "devt":-1, "devt1t":"", "devt1c":"",  "devt2t":"", "devt2c":"",  "devt3t":"", "devt3c":"",  "devt4t":"", "devt4c":"", })
 
cals = {"Liturgical", "US Holidays", "Choirs", "Others", "Masses"}

cal = {"month":"March", "year":"2019", "startwk":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Choirs", "calDt":"Other", "calEt":"Masses"}
pref = {  "startDay":1,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "red"}
dts = [25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 ]

for i in range(0, 4):
          tdy[i]["bgtclr"] = colorsm["priormonth"]
          tdy[i]["bgeclr"] = colorsm["priormonth"]


for i in range(0,35,1):
     tdy[i]["dnum"] = dts[i]


tdy[4]["bgtclr"] = colorsm["thisbefore"]
tdy[4]["beeclr"] = colorsm["thisbefore"]
tdy[5]["bgtclr"] = colorsm["today"]
tdy[5]["beeclr"] = colorsm["today"]

tdy[1]["devt"] = 1
tdy[1]["dev1t"] =  "Noon Mass"
tdy[1]["dev1c"] =pref["calEclr"]
tdy[2]["devt"] = 2
tdy[2]["dev1t"] =  "08:15AM Mass"
tdy[2]["dev1c"] =pref["calEclr"]
tdy[2]["dev2t"] =  "Choir"
tdy[2]["dev2c"] =pref["calCclr"]
tdy[4]["devt"] = 1
tdy[4]["dev1t"] =  "Noon Mass"
tdy[4]["dev1c"] =pref["calEclr"]
tdy[5]["devt"] = 2
tdy[5]["dev1t"] =  "Ordinary 5"
tdy[5]["dev1c"] =pref["calAclr"]
tdy[5]["dev2t"] =  "5:00PM Mass"
tdy[5]["dev2c"] =pref["calEclr"]
tdy[6]["devt"] = 3
tdy[6]["dev1t"] =  "Ordinary 5"
tdy[6]["dev1c"] = pref["calAclr"]
tdy[6]["dev2t"] =  "10:00AM Mass"
tdy[6]["dev2c"] =pref["calEclr"]
tdy[6]["dev3t"] =  "5:00PM Mass"
tdy[6]["dev3c"] =pref["calEclr"]

tdy[8]["devt"] = 1
tdy[8]["dev1t"] =  "Noon Mass"
tdy[8]["dev1c"] =pref["calEclr"]
tdy[9]["devt"] = 3
tdy[9]["dev1t"] =  "Ash Wednesday"
tdy[9]["dev1c"] =pref["calAclr"]
tdy[9]["dev2t"] =  "08:15AM Mass"
tdy[9]["dev2c"] =pref["calEclr"]
tdy[9]["dev3t"] =  "5:00PM Mass"
tdy[9]["dev3c"] =pref["calEclr"]
tdy[11]["devt"] = 1
tdy[11]["dev1t"] =  "Noon Mass"
tdy[11]["dev1c"] =pref["calEclr"]
tdy[12]["devt"] = 2
tdy[12]["dev1t"] =  "First Sunday Lent"
tdy[12]["dev1c"] =pref["calAclr"]
tdy[12]["dev2t"] =  "5:00PM Mass"
tdy[12]["dev2c"] =pref["calEclr"]
tdy[13]["devt"] = 4
tdy[13]["dev1t"] =  "DST begins"
tdy[13]["dev1c"] = pref["calBclr"]
tdy[13]["dev2t"] =  "First Sunday Lent"
tdy[13]["dev2c"] = pref["calAclr"]
tdy[13]["dev3t"] =  "10:00AM Mass"
tdy[13]["dev3c"] =pref["calEclr"]
tdy[13]["dev4t"] =  "5:00PM Mass"
tdy[13]["dev4c"] =pref["calEclr"]

tdy[15]["devt"] = 1
tdy[15]["dev1t"] =  "Noon Mass"
tdy[15]["dev1c"] =pref["calEclr"]
tdy[16]["devt"] = 2
tdy[16]["dev1t"] =  "08:15AM Mass"
tdy[16]["dev1c"] =pref["calEclr"]
tdy[16]["dev2t"] =  "Choir"
tdy[16]["dev2c"] =pref["calCclr"]
tdy[18]["devt"] = 1
tdy[18]["dev1t"] =  "Noon Mass"
tdy[18]["dev1c"] =pref["calEclr"]
tdy[19]["devt"] = 2
tdy[19]["dev1t"] =  "Second Sunday Lent"
tdy[19]["dev1c"] =pref["calAclr"]
tdy[19]["dev2t"] =  "5:00PM Mass"
tdy[19]["dev2c"] =pref["calEclr"]
tdy[20]["devt"] = 3
tdy[20]["dev1t"] =  "Second Sunday Lent"
tdy[20]["dev1c"] = pref["calAclr"]
tdy[20]["dev2t"] =  "10:00AM Mass"
tdy[20]["dev2c"] =pref["calEclr"]
tdy[20]["dev3t"] =  "5:00PM Mass"
tdy[20]["dev3c"] =pref["calEclr"]

tdy[22]["devt"] = 1
tdy[22]["dev1t"] =  "Noon Mass"
tdy[22]["dev1c"] =pref["calEclr"]
tdy[23]["devt"] = 2
tdy[23]["dev1t"] =  "08:15AM Mass"
tdy[23]["dev1c"] =pref["calEclr"]
tdy[23]["dev2t"] =  "Choir"
tdy[23]["dev2c"] =pref["calCclr"]
tdy[25]["devt"] = 1
tdy[25]["dev1t"] =  "Noon Mass"
tdy[25]["dev1c"] =pref["calEclr"]
tdy[26]["devt"] = 2
tdy[26]["dev1t"] =  "Third Sunday Lent"
tdy[26]["dev1c"] =pref["calAclr"]
tdy[26]["dev2t"] =  "5:00PM Mass"
tdy[26]["dev2c"] =pref["calEclr"]
tdy[27]["devt"] = 3
tdy[27]["dev1t"] =  "Third Sunday Lent"
tdy[27]["dev1c"] = pref["calAclr"]
tdy[27]["dev2t"] =  "10:00AM Mass"
tdy[27]["dev2c"] =pref["calEclr"]
tdy[27]["dev3t"] =  "5:00PM Mass"
tdy[27]["dev3c"] =pref["calEclr"]

tdy[29]["devt"] = 1
tdy[29]["dev1t"] =  "Noon Mass"
tdy[29]["dev1c"] =pref["calEclr"]
tdy[30]["devt"] = 2
tdy[30]["dev1t"] =  "08:15AM Mass"
tdy[30]["dev1c"] =pref["calEclr"]
tdy[30]["dev2t"] =  "Choir"
tdy[30]["dev2c"] =pref["calCclr"]
tdy[32]["devt"] = 1
tdy[32]["dev1t"] =  "Noon Mass"
tdy[32]["dev1c"] =pref["calEclr"]
tdy[33]["devt"] = 2
tdy[33]["dev1t"] =  "Fourth Sunday Lent"
tdy[33]["dev1c"] =pref["calAclr"]
tdy[33]["dev2t"] =  "5:00PM Mass"
tdy[33]["dev2c"] =pref["calEclr"]
tdy[34]["devt"] = 3
tdy[34]["dev1t"] =  "Fourth Sunday Lent"
tdy[34]["dev1c"] = pref["calAclr"]
tdy[34]["dev2t"] =  "10:00AM Mass"
tdy[34]["dev2c"] =pref["calEclr"]
tdy[34]["dev3t"] =  "5:00PM Mass"
tdy[34]["dev3c"] =pref["calEclr"]





# block2 dicts
# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "cevt":cevt, "dayt":dayt,"parts":parts, "tdy":tdy, "cal":cal, "pref":pref, "dts":dts, "days":days, "colorsm":colorsm, "cals":cals  }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page11.jhtml")


output = template.render(input_)

print(output)