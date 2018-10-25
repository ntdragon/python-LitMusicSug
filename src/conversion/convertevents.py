""" Convert Event Table - Convert suggestion files into database records """
import argparse
import sys
import sqlite3

def convert(stype, infile, db, origin, date):
    """ Do the conversion for an event file

     event suggestion file format
          lityear text - liturgical year (A,B,C)  E indicates last line
          event text - liturgical event  'End' indicates last line
          title text- a song title for psalm or song ''End of Events' indicates last line
          
          origin - where did the suggestion come from
          date - when was this suggestion imported
    """

    # use pipe rather than csv for reader
    csv.register_dialect('pipes', delimiter='|')

    schema_filename = 'suggestions_schema.sql'
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

def main():
    """ Run as command line program """

     parser = argparse.ArgumentParser(
        description="Load database suggestions table from infile")
     parser.add_argument("stype", help="Psalm or Song")
     parser.add_argument("infile", nargs='?', type=argparse.FileType('r'),
        default=sys.stdin, help="Input file (stdin used if left blank)")
     parser.add_argument("database", help="Database created or updated")
     parser.add_argument("origin", help="Suggestions from")
     parser.add_argument("date", help="Database created or updated date")

    args = parser.parse_args()

    convert(args.stype, args.infile, args.database, args.origin, args.date)


if __name__ == "__main__":
    main()
