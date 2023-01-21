#! /usr/bin/python3
"""
Liturgical Calendar Generation module
------------------------------
This module and the additional modules in the set are to generate a Liturgical calendar in support of the Liturgical 
Music Suggestion program for Roman Catholic Music Directors, Liturgy Directors and musicians.

On Github I found a python2 program that was written by Martin Raynal, 2015-2016 who was inspired by and based on 
ROMCAL 6.2 ROMCAL is Copyright (C) 1993-2003 Kenneth G. Bath (kbath@harris.com).  See http://www.romcal.net/ for
 additional credits and information.  It was set up based on the Gregorian calendar year.

So these modules are similar but are desinged to feed a database with the information and the Liturgical Day not only
 contains basic information on the litrgical event to be celebrated but also contains the readings and psalm for the
 event.  The reason for this is to supply the user with all this for planning purposes.

One major change is that I am not seeting up a bunch of codes that needs to be translated back and forth.  For example;
instead of setting up a code for colors for an event I will just use the color saving a lot of code in the process.

It will will then be used to feed a calendar database.
"""


def generate_liturgical_calendar(lc,year,diocese,parish)
""" Generate a liturgical calendar for (c)calendar (l)liturgical year for a given diocese and parish.
     The diocese file holds key for liturgical options and diocesan/parish celebrations
     The array holds the following information:
          date, title of celebration
     
     """

# set up list for year with dates in year
# set up fixed celebrations
# read in celebrations with dates - Roman Catholic Church
# read in local celebrations - Diocese (Continent)
# read in local celebrations - parish
# 
