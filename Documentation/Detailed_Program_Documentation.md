# Detailed Program Documentation

## Introduction

This document gives an in depth descriptions for the files and code used for this program.
Version 1.0 ??/2020 Edward Birdsall

## File Structures
### File Format for creating and importing Song book
     text file using | as the delimiter
     song (integer) | type (Psalm, Part or Song) | title (string)
examples
     017|Song|Evensong Final Blessing
     018|Psalm|Psalm 1: Happy Are They
last row:
      99999|end|End of Songs

### File Format for creating and importing Song book Search
     text file using | as the delimiter
     title (string)| number of songs for this title (integer)| songnumber (integer) <| songnumber(integer)>
examples
     Love Is the Sunlight| 1 | 866
     Lover of Us All| 1 | 633
     Magnificat/Canticle of Mary| 5 | 014 | 145 | 146 | 534 | 788
     Ubi Caritas| 2 | 408 | 631
     Unless a Grain of Wheat| 1 | 697
last row     
     End of Songs| 0 | 0

### File Format for Suggestions (Psalms and Songs input are all seperate)
     text file with | as the delimiter
     Liturgical Year (A B C)| event (text) | Song Title (text)
example
      B | Advent1 | In the Day of the Lord 
last row
      E | End | End of Events

### File Format Mass Parts
     text file with | as delimiter
     Setting | Part
example
     Mass of Creation | Amen

## Database Structures
### Events

This database contains a list of the standard weekend and holy day events but also allows addition of special events for the parish or musician.
         id     integer primary key autoincrement not null,
         fid    text,   File Identifier
         name   text,   Event
         title  text,   Event Printed Title
         type   text    Type of event

In more detail;
    fid File Identifier - A short id to put in the file name to help quickly identify it, normall one or two characters followed by a number.  Standard values are; A1 through A4 (Advent), O1 through O34 (Ordinary Time), L1 through L5 (Lent), E2-E7(Easter), S-- (Special Sundays), H-- (Holy Days), D--(Holy Days with Vigils like Christmas and Easter).  Additionally P-- is the prefix for parish special events like patron saint.  MW--(Weddings), MF(Funerals), M_--(Musician defined)
    name name of the event which may be identical to title or something easier to remember.  It is not shown anywhere but is searchable.
    title is the formal printed title of the event like Second Sunday of Advent or John and Mary Smith's Wedding.
    type is a categorization of the schedule of masses for the event.  Weekend, Holy Day, Single, Multiple are defined.  Using Weekend will prompt the program to use the parish's standard weekend mass schedule as will Holy Day.  Single and Multiple will prompt the user to define the day, time and for multiple masses how many and all their scheduling information.

The events file to import this has the following format and uses a vertical bar to seperate fields;
    fid | name | title | type
    Examples;    A1 | Advent 1 | First Sunday in Advent | Weekend
                D1 | Christmas | Christmas | Multiple

### Mass Parts

This database contains the various themes in the songbooks for mass parts.  The mass parts are the settings/themes in the songbook for songs like the Gloria and Lamb of God.
          id        integer primary key autoincrement not null,
          book      text,       songbook id
          theme      text,      setting/theme  May be something like Setting One, Mass of Creation or entries for both
          name    text,         name of song like Gloria
          num       integer,    number of version of song
     unique(book, theme, name, num)


### Songbooks

This database contains a catalog of all songs, psalms and mass parts in a songbook.
          id        integer primary key autoincrement not null,
          book      text,
          num       integer,
          type      text,
          title     text,
          unique(book, number, type, title)

### Songbook Searches

This database contains a listing for each songbook of all songs matching a suggestion for a song or psalm.  This is helpful where suggestions from some sources may contain only parts of a title or the songbook may have several versions.

          id        integer primary key autoincrement not null,
          book      text,
          stitle    text,
          numsongs  integer,
          songlist  text

### Suggestions for SOngs and Psalms

          id        integer primary key autoincrement not null,
          lityr     char,
          event     text,
          stype     text,
         stitle     text,
         origin     text,   who suggested this (NPM, GIA,Person or org)
          date      date    original date of suggestion

### EventHistory

This database contains all the songs that were used on a particular date or weekend for an event.  It does not say where the song was used or for multiple masses which masses it was used.
         id        integer primary key autoincrement not null,
          dayt      date;
          event     text,
          book      text,
          num       integer



## Program Structure

