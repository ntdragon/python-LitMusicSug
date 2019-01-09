#!/usr/bin/python3
"""
     Music Suggestions Program database module
"""

class MSPDB()
     """
     """
     def __init__(self):
     """
     Initialize databases used in program
     """
     import sqlite3

     db = 'memory:'
          schema_filename = 'song_schema.sql'
          #db is songbook database filename or for RAM ':memory:'

          dbcon = sqlite3.connect(db)
          dbcursor = dbcon.cursor()

          with open(schema_filename, 'rt') as f:
               schema = f.read()
               dbcursor.executescript(schema)

          dbcon.commit()
          dbcon.close()



     def input_songbook(songbookcode, songbookprintfile, songbooksearchfile):
     """
     """


     #create tables
     sbcrsr.execute('''CREATE TABLE songbook
                (book text, stype text, snum integer, sptitle text)''')
      sbscrsr.execute('''CREATE TABLE songsearch
                (book text, stype text, snum integer, sptitle text)''')


     def edit_songbook
     """
     """

     def