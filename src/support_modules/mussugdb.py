#!/usr/bin/python3
"""
     Music Parse Database Operations
"""
"""
Database Tables
     songs
          id  - primary key
          book text - two or three letter code defining which song book is in use
          type text - Psalm or Song
          num integer - number of the song
          title - song title for use
     titlesearch
         id  - primary key
          book text - two or three letter code defining which song book is in use
          stitle text - search title or first line
          songs text - list of songs for that search title
     sugg
         id  - primary key
          ly_yr   text - liturgical year (A,B,C)
          event     text - liturgical event
          stype text - Psalm or Song 
          title     text - a song title for psalm or song
          origin    text - where suggestion was from
          idate      date - date suggestion imported
     parish_information
          name      text - Parish name
          street    text - Street address
          city      text - city
          state     text - state or province
          zip       text - zip code
          masstimes text - Day:time | Day:time..
     savedevent
         id  - primary key
          date text - date and time of mass for sunday or event
          lityr text - liturgical year (A,B,C)
          event text - liturgical event
          stipe - text  - which song/psalm in Mass
          book - text - song book code
          num - song number
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
     def __init__(self):
          if database exists then
               self.db = self.get
         ? self._get_parms()
          ?self.db = sqlite3.connect(self.args.database)

     ?def _get_parms(self):
          


     def convertsong(book, infile, db_name):
         """ Do the conversion for a song book file
               Database Table
                    songs
                         id  - primary key
                         book text - two or three letter code defining which song book is in use
                         type text - Psalm or Song
                         num integer - number of the song
                         title - song title for printing

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


     def songsearch()
          """ with a title or first line to locate possible titles"""











     def main():
          """
               Run as a command line program
          """
          schema_filename = 'schema.sql'
          db_filename = 'MSPdatabase.db'
          db_is_new = not os.path.exists(db_filename)
          if db_is_new:
               initdb(self.db, schema_filename, db_filename)
          else
               self.db = sqlite3.connect(db_filename)
          
          dbcrsr = self.db.cursor()
          self.db.close()              

if __name__ == '__main__':
    main()
