""" Convert Song Table - Convert songbook text files into database records """
import argparse
import sys
import sqlite3

def convert(book, infile, db):
    """ Do the conversion for a file """
         """ Ed - 10/12/2018
          Song book file for conversion format with | as delimiter:
               number - 99999 reserved for end of file line
               type - Psalm, Song or end
               title - Song title
          """

    conn = sqlite3.connect(db)

    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS songs (
        id integer primary key autoincrement not null,
        book text,
        number integer,
        type text,
        title text,
        unique(book, number, type, title)
        )''')


    for line in infile:
        num, title = line.split("|")

        num = num.strip()
        inum = int(num)
        title = title.strip()

        # Special sentinel values at start and end are not actual songs
        # Perhaps this should be specific to first and last entry
        # but to do so I would have to structure to know if last entry
        # before adding
        if all([v == '0' for v in num]):
            continue
        if all([v == '9' for v in num]) and title.startswith("End of Song"):
            continue

        # Very simple rule for determining Psalm - check with Ed.
        btype = "Psalm" if title.startswith("Psalm") else "Song"

        # Could gather all entries and use an executemany
        # which would solve knowing which entry is last
        entry = (book, inum, btype, title)
        cursor.execute("""INSERT OR IGNORE INTO Songs
            (book, number, type, title) VALUES (?,?,?,?)""", entry)

    conn.commit()
    conn.close()

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

