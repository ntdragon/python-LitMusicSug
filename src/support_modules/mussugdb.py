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
          lityear text - liturgical year (A,B,C)
          event text - liturgical event
          title text- a song title for psalm or song
     events_history
          date text - date of sunday or event
          lityr text - liturgical year (A,B,C)
          event text - liturgical event
          ss .. - list of book:song pairs used for that day
          #TODO: need to learn best method to do this
"""

class MusSugDB():
     """
     Database operations for Music Suggestion Program
     """
     def convertsong(book, infile, db):
         """ Do the conversion for a song book file

               Song book file for conversion format with | as delimiter:
                    number - 99999 reserved for end of file line
                    type - Psalm, Song or end(final line)
                    title - Song title ('End of Song' for final line)
          """

         dbcon = sqlite3.connect(db)

         cursor = dbcon.cursor()
         dbcursor.execute('''CREATE TABLE IF NOT EXISTS songs (
             id integer primary key autoincrement not null,
             book text,
             number integer,
             type text,
             title text,
             unique(book, number, type, title)
             )''')


         for line in infile:
             num, btype, title = line.split("|")

             num = num.strip()
             inum = int(num)
             btype = btype.strip()
             title = title.strip()

             # Special sentinel values at start and end are not actual songs
             # Perhaps this should be specific to first and last entry
             # but to do so I would have to structure to know if last entry
             # before adding
             #TODO: change end and beginning check to reflect file change
             if all([v == '0' for v in num]):
                 continue
             if all([v == '9' for v in num]) and title.startswith("End of Song"):
                 continue

             # Very simple rule for determining Psalm - check with Ed.
             # btype = "Psalm" if title.startswith("Psalm") else "Song"

             # Could gather all entries and use an executemany
             # which would solve knowing which entry is last
             entry = (book, inum, btype, title)
             cursor.execute("""INSERT OR IGNORE INTO Songs
                 (book, number, type, title) VALUES (?,?,?,?)""", entry)

         dbcon.commit()
         dbcon.close()

     def convertsearch()
          """ do conversion for a file of title search for a certain book """

     def convertevent()
          """ do conversion for a file of event suggestions """

     def titlesearch()
          """ with a title to search locate known title """
