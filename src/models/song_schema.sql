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

-- Mass parts with theme containing all the standard songs used in all masses
create table mparts (
          id        integer primary key autoincrement not null,
          book      text,
          theme      text,
          name    text,
          num       integer,
     unique(book, theme, name, num)
);

-- Event is used to help in planning events throught the year
create table events (
          id        integer primary key autoincrement not null,
          fid            text,
          name      text,
          title         text,
          type    text
);

-- Suggestions is used to record suggestins eithr used or not used for the evens for songs and psalms
create table sugg (
          id        integer primary key autoincrement not null,
          event     text,
          lityr     char,
         stitle     text
);

--Used is a table recording what songs were used so they can be retrieved for quick reference
create table eventhistory (
          id        integer primary key autoincrement not null,
          dayt      date;
          event     text,
          book      text,
          num       integer
);