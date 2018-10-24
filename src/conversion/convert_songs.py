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

    if db_is_new:
        with open(schema_filename, 'rt') as f:
            schema = f.read()
            dbcrsr = dbcon.cursor()
            dbcrsr.executescript(schema)
        with open(infile, 'rt') as f:
            reader = csv.reader(f, dialect='pipes')
            for row in reader:
                num, btype, title = row.split("|")
                num = num.strip()
                inum = int(num)
                btype = btype.strip()
                title = title.strip()
                entry = (book, inum, btype, title)
                #TODO: finish me
                cursor.execute("""INSERT OR IGNORE INTO Songs
                    (book, number, type, title) VALUES (?,?,?,?)""", entry)
                ##TODO Finish ? 
    else:
        dbcrsr = dbcon.cursor()
        with open(infile, 'rt') as f:
            reader = csv.reader(f, dialect='pipes')
            for row in reader:
                num, btype, title = row.split("|")
                num = num.strip()
                inum = int(num)
                btype = btype.strip()
                title = title.strip()
                entry = (book, inum, btype, title)
                #TODO Finish me


    conn.commit()
    conn.close()








#-------------------------------------
        
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS songs (
        id integer primary key autoincrement not null,
        book text,
        number integer,
        type text,
        title text,
        unique(book, number, type, title)
        )''')

    # use pipe rather than csv for reader
    csv.register_dialect('pipes', delimiter='|')

    for line in infile:
        num, tipe, title = line.split("|")

        num = num.strip()
        inum = int(num)
        btype = tipe.strip()
        title = title.strip()

        # Special sentinel values at start and end are not actual songs
        # Perhaps this should be specific to first and last entry
        # but to do so I would have to structure to know if last entry
        # before adding
        #if all([v == '0' for v in num]):
        #   continue
        if all([v == '9' for v in num]) and title.startswith("End of Song"):
            continue

        # Very simple rule for determining Psalm - check with Ed.
        # btype = "Psalm" if title.startswith("Psalm") else "Song"
        
        # Could gather all entries and use an executemany
        # which would solve knowing which entry is last
        entry = (book, inum, btype, title)


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

