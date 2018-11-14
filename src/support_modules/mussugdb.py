#!/usr/bin/python3
"""
     Music Parse Database Operations
"""
"""
Database Tables
     songs
          book text - two or three letter code defining which song book is in use
          type text - Psalm or Song
          number integer - number of the song
          title - song title for use
     titlesearch
          book text - two or three letter code defining which song book is in use
          title text - search title
          songs integer - list of songs for that search title
     eventsugg
          lityear   text - liturgical year (A,B,C)
          event     text - liturgical event
          title     text - a song title for psalm or song
          origin    text - where suggestion was from
          date      date - date suggestion imported
     parish_information
          name      text - Parish name
          street    text - Street address
          city      text - city
          state     text - state or province
          zip       text - zip code
          masstimes text - Day:time | Day:time...
     events_history
          date text - date of sunday or event
          lityr text - liturgical year (A,B,C)
          event text - liturgical event
          ss .. - list of book:song pairs used for that day
          #TODO: need to learn best method to do this
"""
import argparse
import sys
import os
import sqlite3
import csv

class MusSugDB():
     """
     Database operations for Music Suggestion Program
     """
     def convertsong(book, infile, db_name):
         """ Do the conversion for a song book file

               Song book file for conversion format with | as delimiter:
                    number - 99999 reserved for end of file line
                    type - Psalm, Song or end(final line)
                    title - Song title ('End of Song' for final line)
          """


          # use pipe rather than csv for reader
          csv.register_dialect('pipes', delimiter='|')

          schema_filename = 'songbook_schema.sql'
          #db is songbook database filename
    
          db_is_new = not os.path.exists(db_name)         

          dbcon = sqlite3.connect(db_name)
          dbcrsr = dbcon.cursor()

          if db_is_new:
               with open(schema_filename, 'rt') as f:
                    schema = f.read()
                    dbcrsr.executescript(schema)

          with open(infile, 'rt') as f:
               reader = csv.reader(f, dialect='pipes')
               for row in reader:
                    num, btype, title = row.split("|")
                    num = num.strip()
                    inum = int(num)
                    # check for end line
                    if num == '99999':
                         break
                    btype = btype.strip()
                    title = title.strip()
                    entry = (book, inum, btype, title)
                    dbcrsr.execute("""INSERT OR IGNORE INTO songbook
                         (book, num, type, title) VALUES (?,?,?,?)""", entry)

          dbcon.commit()
          dbcon.close()

     def convertsearch(book, infile, db_name)
          """ do conversion for a file of title search for a certain book """
          # use pipe rather than csv for reader
          csv.register_dialect('pipes', delimiter='|')

          schema_filename = 'songbook_schema.sql'
          #db is songbook database filename
    
          db_is_new = not os.path.exists(db)         

          dbcon = sqlite3.connect(db)
          dbcrsr = dbcon.cursor()

          if db_is_new:
               with open(schema_filename, 'rt') as f:
                    schema = f.read()
                    dbcrsr.executescript(schema)

          with open(infile, 'rt') as f:
               reader = csv.reader(f, dialect='pipes')
               for row in reader:
                    title, num, lsongs = row.split("|",2)
                    num = num.strip()
                    inum = int(num)
                    # check for end line
                    if num == '0':
                         break
                    title = title.strip()
                    entry = (book, title, inum, lsongs)
                    dbcrsr.execute("""INSERT OR IGNORE INTO songsearch
                         (book, title, num, songs) VALUES (?,?,?,?)""", entry)

          dbcon.commit()
          dbcon.close()

     def convertevent(infile, db_name)
          """ do conversion for a file of event suggestions """
          """
          event suggestion file format
          lityear text - liturgical year (A,B,C)  E indicates last line
          event text - liturgical event  'End' indicates last line
          title text- a song title for psalm or song 'End of Events' indicates last line
          
          origin - where did the suggestion come from
          date - when was this suggestion imported
          """

          # use pipe rather than csv for reader
          csv.register_dialect('pipes', delimiter='|')

          schema_filename = 'suggestions_schema.sql'
          #db is songbook database filename
    
          db_is_new = not os.path.exists(db_name)         

          dbcon = sqlite3.connect(db_name)
          dbcrsr = dbcon.cursor()

          if db_is_new:
               with open(schema_filename, 'rt') as f:
                    schema = f.read()
                    dbcrsr.executescript(schema)

          with open(infile, 'rt') as f:
               reader = csv.reader(f, dialect='pipes')
               for row in reader:
                    ly, event, title = row.split("|")
                    ly = ly.strip()
                    # check for end line
                    if ly == 'E':
                         break
                    title = title.strip()
                    event = event.strip()
                    entry = (stype, ly, event, title, origin, date)
                    dbcrsr.execute("""INSERT OR IGNORE INTO sugg
                         (stype, ly_yr, event, title, origin, idate) VALUES (?,?,?,?,?,?)""", entry)

          dbcon.commit()
          dbcon.close()

     def titlesearch()
          """ with a title to search locate known title """
