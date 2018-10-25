""" Convert Song Table - Convert songbook text files into database records """
import argparse
import sys
import os
import sqlite3
import csv

def convert(book, infile, db):
    """ Do the conversion for a file """

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
                num, btype, title = row.split("|")
                num = num.strip()
                inum = int(num)
               # check for end line
               if num == '99999':
                    break
                btype = btype.strip()
                title = title.strip()
                entry = (book, inum, btype, title)
                dbcrsr.execute("""INSERT OR IGNORE INTO Songs
                    (book, number, type, title) VALUES (?,?,?,?)""", entry)

    dbcon.commit()
    dbcon.close()

def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load database song table from infile")
    parser.add_argument("book", help="Identifier for songbook")
    parser.add_argument("infile", nargs='?', type=argparse.FileType('r'),
        default=sys.stdin, help="Input file (stdin used if left blank)")
    parser.add_argument("database", help="Database created or updated")

    args = parser.parse_args()

    convert(args.book, args.infile, args.database)


if __name__ == "__main__":
    main()

