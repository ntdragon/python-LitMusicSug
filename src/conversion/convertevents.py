""" Convert Event Table - Convert suggestion files into database records """
import argparse
import sys
import sqlite3

def convert(book, infile, db):
    """ Do the conversion for an event file

     event suggestion file format
          lityear text - liturgical year (A,B,C)  E indicates last line
          event text - liturgical event  'End' indicates last line
          title text- a song title for psalm or song ''End of Events' indicates last line
    """

    conn = sqlite3.connect(db)

    cursor = conn.cursor()
    # TODO: Create table of legal events that even references
    cursor.execute('''CREATE TABLE IF NOT EXISTS suggestion (
        id integer primary key autoincrement not null,
        lit_year char(1) check("lit_year" in ('A','B','C')),
        event string not null,
        suggestion integer not null,
        origin string,
        FOREIGN KEY(suggestion) REFERENCES songs(id),
        unique(lit_year, event, suggestion, origin)
        )''')

    for line in infile:
        lit_year, event, num, title = line.split("|")

        num = num.strip()
        inum = int(num)
        title = title.strip()
