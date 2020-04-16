# Advanced User Guide

## Introduction

## File Formats
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

## Customizing printouts

## Adding a new songbook

## Database Tables
### Songbook
     id             integer primary key autoincrement not null
     songbook       text
     songnum        integer
     songtype       text
     songtitle      text

### Songbook Search
     id             integer primary key autoincrement not null
     songbk         text
     songtytle      text
     numsongs       integer
     songlist       text
-------------------------------------------------------------
### Song Suggestions and Psalm Suggestions
     lityr
     event
     stype
     stitle
     origin         (who suggested this NPM, GIA, person??)
     date           (of suggestion orignally)
-------------------------------------------------------------
### Parish
     name
     
### Songs Used
     date
     time
     lityr
     event
     masspart
     songbook
     song title