-- song_schema.sql

-- Schema for song books both print and search.

-- Print is used for printouts and has title the same as in the particular songbook
create table songbook (
          id        integer primary key autoincrement not null,
          book      text,
          num       integer,
          type      text,
          title     text,
          unique(book, number, type, title)
);

--SongbookSearch is used to locate the songs for each suggestion
create table songsearch (
          id        integer primary key autoincrement not null,
          book      text,
          stitle    text,
          num       integer,
          songs     text
);