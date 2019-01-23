-- schema.sql

-- Schema for song books both print and search.

-- Print is used for printouts and has title the same as in the particular songbook
create table songbook (
          id        integer primary key autoincrement not null,
          book      text,
          type      text,
          num       integer,
          title     text,
          unique(book, number, type, title)
);

--SongbookSearch is used to locate the songs for each suggestion
create table titlesearch (
          id        integer primary key autoincrement not null,
          book      text,
          stitle    text,
          songs     text
);

-- Schema for both Psalm and Songs suggestions

create table sugg (
          id        integer primary key autoincrement not null,
          ly_yr     char(1) check("lit_yr" in ('A','B','C')),
          event     text,
          stype      text check("stype" in ('Psalm','Song')),
          title     text,
          origin    text,
          idate     date
          unique(lit_yr, event, title, origin)
);

-- Schema for Saved Events for suggestions used
-- edate is date and time of mass,  stipe is where song used in mass (entrance, offertory,...)

create table savedevent (
          id        integer primary key autoincrement not null,
          edate     date,
          ly_yr     char(1)  check("lit_yr" in ('A','B','C')),
          event     text,
          stipe     text,
          book      text,
          num       integer
          unique(edate, stipe, book, num)
);