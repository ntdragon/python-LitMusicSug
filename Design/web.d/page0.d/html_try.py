#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import calendar
import datetime

#=========================================================================================================
#Begining of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
#=========================================================================================================
#=================================
# desired inputs for final version what, when, which event calendars, preferences
#=================================
inputs = {"date":"March 2, 2019", "startDay":6,}
#========================================================
# some kludges for testing and until I get it all working
#========================================================
#cyear = int(cal.get("year"))
cyear = 2019
cmonth = 3
cday = 2
cals= [
      dict(num=0, app="FALSE", name="Liturgical", color="yellowgreen"),
      dict(num=1, app="FALSE", name="US Holidays", color="lightsteelblue"),
      dict(num=2, app="TRUE", name="Choirs", color="cyan"),
      dict(num=3, app="TRUE", name="Other",color="magenta"),
      dict(num=4, app="TRUE", name="Masses", color="red")
]

eventCal = [
           dict(num=0, cal="Liturgical", eDate=datetime.date(2019, 2, 23), title="Ordinary 8th Vigil"),
           dict(num=1, cal="Liturgical", eDate=datetime.date(2019, 2, 24), title="Ordinary 8th Sunday"),
           dict(num=2, cal="Liturgical", eDate=datetime.date(2019, 3, 2), title="Ordinary 9th Vigil"),
           dict(num=3, cal="Liturgical", eDate=datetime.date(2019, 3, 3), title="Ordinary 9th Sunday"),
           dict(num=4, cal="Liturgical", eDate=datetime.date(2019, 3, 6), title="Ash Wednesday"),
           dict(num=5, cal="Liturgical", eDate=datetime.date(2019, 3, 9), title="Lent 1 Vigil"),
           dict(num=6, cal="Liturgical", eDate=datetime.date(2019, 3, 10), title="Lent 1st Sunday"),
           dict(num=7, cal="Liturgical", eDate=datetime.date(2019, 3, 16), title="Lent 2nd Vigil"),
           dict(num=8, cal="Liturgical", eDate=datetime.date(2019, 3, 17), title="Lent 2nd Sunday"),
           dict(num=9, cal="Liturgical", eDate=datetime.date(2019, 3, 23), title="Lent 3rd Vigil"),
           dict(num=10, cal="Liturgical", eDate=datetime.date(2019, 3, 24), title="Lent 3rd Sunday"),
           dict(num=11, cal="Liturgical", eDate=datetime.date(2019, 3, 30), title="Lent 4th Vigil"),
           dict(num=12, cal="Liturgical", eDate=datetime.date(2019, 3, 31), title="Lent 4th Sunday"),
           dict(num=13, cal="Liturgical", eDate=datetime.date(2019, 4, 6), title="Lent 5th Vigil"),
           dict(num=14, cal="US Holidays", eDate=datetime.date(2019, 3, 9), title="DST begins"),
           dict(num=15, cal="Masses", eDate=datetime.date(2019, 2, 26), title="Noon Mass"),
           dict(num=16, cal="Masses", eDate=datetime.date(2019, 2, 27), title="08:15 Mass"),
           dict(num=17, cal="Masses", eDate=datetime.date(2019, 3, 1), title="Noon Mass"),
           dict(num=18, cal="Masses", eDate=datetime.date(2019, 3, 2), title="4PM Mass"),
           dict(num=19, cal="Masses", eDate=datetime.date(2019, 3, 3), title="9AM Mass"),
           dict(num=20, cal="Masses", eDate=datetime.date(2019, 3, 3), title="11:30AM Mass"),
           dict(num=21, cal="Masses", eDate=datetime.date(2019, 3, 5), title="Noon Mass"),
           dict(num=22, cal="Masses", eDate=datetime.date(2019, 3, 6), title="08:15 Mass"),
           dict(num=23, cal="Masses", eDate=datetime.date(2019, 3, 6), title="5PM Mass"),
           dict(num=24, cal="Masses", eDate=datetime.date(2019, 3, 8), title="Noon Mass"),
           dict(num=25, cal="Masses", eDate=datetime.date(2019, 3, 9), title="4PM Mass"),
           dict(num=26, cal="Masses", eDate=datetime.date(2019, 3, 10), title="9AM Mass"),
           dict(num=27, cal="Masses", eDate=datetime.date(2019, 3, 10), title="11:30AM Mass"),
           dict(num=28, cal="Masses", eDate=datetime.date(2019, 3, 12), title="Noon Mass"),
           dict(num=29, cal="Masses", eDate=datetime.date(2019, 3, 13), title="08:15AM Mass"),
           dict(num=30, cal="Masses", eDate=datetime.date(2019, 3, 15), title="Noon Mass"),
           dict(num=31, cal="Masses", eDate=datetime.date(2019, 3, 16), title="4PM Mass"),
           dict(num=32, cal="Masses", eDate=datetime.date(2019, 3, 17), title="9AM Mass"),
           dict(num=33, cal="Masses", eDate=datetime.date(2019, 3, 17), title="11:30AM Mass"),
           dict(num=34, cal="Masses", eDate=datetime.date(2019, 3, 19), title="Noon Mass"),
           dict(num=35, cal="Masses", eDate=datetime.date(2019, 3, 20), title="08:15AM Mass"),
           dict(num=36, cal="Masses", eDate=datetime.date(2019, 3, 22), title="Noon Mass"),
           dict(num=37, cal="Masses", eDate=datetime.date(2019, 3, 23), title="4PM Mass"),
           dict(num=38, cal="Masses", eDate=datetime.date(2019, 3, 24), title="9AM Mass"),
           dict(num=39, cal="Masses", eDate=datetime.date(2019, 3, 24), title="11:30AM Mass"),
           dict(num=40, cal="Masses", eDate=datetime.date(2019, 3, 26), title="Noon Mass"),
           dict(num=41, cal="Masses", eDate=datetime.date(2019, 3, 27), title="08:15AM Mass"),
           dict(num=42, cal="Masses", eDate=datetime.date(2019, 3, 29), title="Noon Mass"),
           dict(num=43, cal="Masses", eDate=datetime.date(2019, 3, 30), title="4PM Mass"),
           dict(num=44, cal="Masses", eDate=datetime.date(2019, 3, 31), title="9AM Mass"),
           dict(num=45, cal="Masses", eDate=datetime.date(2019, 3, 31), title="11:30AM Mass"),
           dict(num=46, cal="Masses", eDate=datetime.date(2019, 4, 2), title="Noon Mass"),
           dict(num=47, cal="Masses", eDate=datetime.date(2019, 4, 3), title="08:15AM Mass"),
           dict(num=48, cal="Masses", eDate=datetime.date(2019, 4, 5), title="Noon Mass"),
           dict(num=49, cal="Masses", eDate=datetime.date(2019, 4, 6), title="4PM Mass"),
           dict(num=50, cal="Choirs", eDate=datetime.date(2019, 2, 27), title="Choir"),
           dict(num=51, cal="Choirs", eDate=datetime.date(2019, 3, 13), title="Choir"),
           dict(num=52, cal="Choirs", eDate=datetime.date(2019, 3, 20), title="Choir"),
           dict(num=53, cal="Choirs", eDate=datetime.date(2019, 3, 27), title="Choir"),
           dict(num=54, cal="Choirs", eDate=datetime.date(2019, 4, 3), title="Choir"),
           dict(num=10, cal="Other", eDate=datetime.date(2019, 2, 25), title="Staff Meeting"),
]
#===================================
# Working code towards final version
#===================================
# page input
#page = dict(action="single", user="Edward Birdsall")

# tab and header

hd = {"loc": "Main"}
hdr = dict(page="Main", today="Saturday  March 02, 2022")
#hdr["today"] = datetime.datetime.now().strftime("%A %B %d, %Y")
hdr["today"] = "Saturday March 02, 2019"  #for testing

#block1 dicts
cal = {"month":"March", "year":"2019", "startwk":5, "calrows":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Choirs", "calDt":"Other", "calEt":"Masses"}
pref = {  "startDay":0,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "red"}
pref["startDay"] = inputs["startDay"]


#cevt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive" )
#dayt = dict(today="March 06, 2019", dmax="December 31,2020")

colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }


if (inputs["startDay"] == 6):  # Week starts on Sunday
     cal["startwk"] = int(datetime.date(cyear, cmonth, cday).strftime("%U"))
else:                        #Week starts on Monday
     cal["startwk"] = int(datetime.date(cyear, cmonth, cday).strftime("%W"))

glcal = calendar.Calendar(inputs["startDay"])
days = [calendar.day_name[i] for i in glcal.iterweekdays()]
dts = []
dmt = []
for i in glcal.itermonthdates(cyear, cmonth):
     dts.append( i.day )
     dmt.append( i.month )

numdays = len(dts)
cal["calrows"] = numdays//7

#days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

tdy = []
for i in range(0, 42,1):
     tdy.append({"bgtclr":"white","bgeclr":"white", "mnum":0, "dnum":0, "devt":-1, "dev1t":"", "dev1c":"gray85", "dev1e":"",  "dev2t":"", "dev2c":"gray85", "dev2e":"", "dev3t":"", "dev3c":"gray85", "dev3e":"", "dev4t":"", "dev4c":"grey85", "dev4e":"", })
 
for i in range(0, numdays, 1):
     tdy[i]["mnum"] = dmt[i]
     tdy[i]["dnum"] = dts[i]
     if (dmt[i] < cmonth):
          tdy[i]["bgtclr"] = colorsm["priormonth"]
          tdy[i]["bgeclr"] = colorsm["priormonth"]
     elif (dmt[i] > cmonth ):
          tdy[i]["bgtclr"] = colorsm["nextmonth"]
          tdy[i]["bgeclr"] = colorsm["nextmonth"]
     else:
          if (dts[i] < cday):
               tdy[i]["bgtclr"] = colorsm["thisbefore"]
               tdy[i]["beeclr"] = colorsm["thisbefore"]
          elif (dts[i] == cday):
               tdy[i]["bgtclr"] = colorsm["today"]
               tdy[i]["beeclr"] = colorsm["today"]
          else:
               tdy[i]["bgtclr"] = colorsm["thismonth"]
               tdy[i]["beeclr"] = colorsm["thismonth"]

for i in range(0, 42, 1):
     for ii in range(0,len(eventCal),1):
          if ((tdy[i]["mnum"] == eventCal[ii]["eDate"].month) and (tdy[i]["dnum"] == eventCal[ii]["eDate"].day)):
               if (tdy[i]["devt"]<1):
                    tdy[i]["devt"] = 1
               else:
                    tdy[i]["devt"] = tdy[i]["devt"] + 1
               if (tdy[i]["devt"] == 1):
                    tdy[i]["dev1t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev1c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev1e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 2):
                    tdy[i]["dev2t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev2c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev2e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 3):
                    tdy[i]["dev3t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev3c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev3e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 4):
                    tdy[i]["dev4t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev4c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev4e"] = "Show "+ eventCal[ii]["title"]
               else:
                    tdy[i]["devt"] = 4


# block2 dicts
# block3 dicts

# collect all the dicts and such

input_ = {"hd":hd, "hdr":hdr, "tdy":tdy, "cal":cal, "pref":pref,  "days":days, "colorsm":colorsm  }

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page0.jhtml")


output = template.render(input_)

print(output)
