#! /usr/bin/python3
"""
Liturgical Event module
------------------------------
This module is designed to populate a Liturgical Day with the exception of the exact date for a given year.
So some days this module populates may not be used in a particular liturgical year.  It reads from files that contain
all the liturgical celebrations for both the whole Roman Catholic Church and also the local diocese and parish where
the parish is located.  So three inputs there.  It also inputs from file the readings for the event given the reading
cycle for the day.

"""

Colors =["NONE", "GREEN", "WHITE", "RED", "PURPLE", "ROSE","BLACK", "GOLD","BLUE"]
EventRank = ["WEEKDAY","COMMEMORATION","OPTIONAL_MEMORIAL", "MEMORIAL","FEAST","SUNDAY","LORD","ASHWED",""HOLYWEEK,
     "TRIDUUM","SOLEMNITY"]
Seasons = ["ORDINARY","ADVENT","CHRISTMAS","LENT","EASTER","PASCHAL","PASSION"]


class FixedLitCal:
     """
     This class holds all the fixed liturgical events and their dates.
     """

     def __init__(self,event_title,event_desc,event_month,event_day,event_rank,event_color,event_optcolor):
          self.event_title=event_title
          self.event_desc=event.desc
          self.event_month=event.month
          self.event_day=event_day
          self.event_rank=event_rank
          self.event_color=event_color
          self.event_optcolor=opt_color

     def get_event_cal(fyle);
     """
     This function will get all the events and their information from a file for he church, diocese or parish.
     """

class LiturgicalEvent:
     """
     This class holds all the information for a specific Liturgical Event.  Note that some days, like Christmas, which
     have multiple events.  Christmas day has Christmas at Midnight, Christmas at Dawn and Christmas during the day.
     Also some events have required and optional readings like Easter Vigil.  Since this is being designed for people
     who are planning liturgies then all the events for a day are available.  The Liturgical Calendar Generation will
     handle which events are to be included for a given liturgical year and on what date.
     """

     def __init__(self, event, rank, color[], readings[], rdval[], psalm, gospel):
          self.event=event
          self.rank
          self.color=color[0]
          self.optcolor=color[1]
          self.readings=readings[]
          self.rdval=rdval[]
          self.psalm=psalm
          self.gospel=gospel

     def get_events(fyle):
          """ This function reads all events in a given file.  It returns a dict of event title(event), 
               rank and colors
          """

     def get_readings(fyle)
          """ This function reads all the readings for all event in a given file.  It returns a list which has a dict;
               of event title, reading title, reading, required/optional), psalm, gospel.  The fyle should be one of
               the set of five files; ReadingsA, ReadingsB, ReadingsC, ReadingsI, and ReadingsII.
          """

     def set_event