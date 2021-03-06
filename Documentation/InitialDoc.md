# Liturgical Music Suggestions Program

## Introduction

This program is designed to be an assist to Roman Catholic Music Directors and musicians who 
are tasked with setting up music to be used at Mass on Sundays and Holy Days.  The program
will get input from its own database plus allow for suggestions from NPM and other sources
to be added.

## Guide to Directories and Files provided

### Documentation

This directory contains the documentation about the program.  Files here are;
* Getting Started Guide - This document gives instructions for setting up the program initially
     using the files provided.  Also a quick example of how to use the program when set up.
* User Guide - This document guides the user in how to use the program and features.
* Advanced User Guide - This document describes how to create and setup files for use in
     adding songbooks, creating a template for your parish and other customizations.
* Program Documention - This is a in depth detailed description of the program and how it 
     is designed to work.

### Initial

This directory is the source directory for the initial files to set up the program and is also the
directory used for files that contain customizations for your parish.

### src

This directory contains the program files themselves.

## Initial Setup files

This program comes with a few files that were used in the design, development and testing of 
the program but you may need to create and set up some text files for for your parish.

The initial files needed to set up the programs database are;
* Songbook file - a file containing the song numbers song titles and are they a Psalm, Part or Song.
     A Psalm indicates a song that may be used instead of the scriptural passage. Part is a standard
     like the Amen for Mass of Creation and is organized by theme then song.
+Provided
     with the program should be GatherPrint.txt and Gather3Print.text which are for Gather
     Comprehensive and Gather Comprehensive Third Edition respectively.
* Search file - a file containing song titles or first lines of songs and which song numbers
     they are for a particular book.  GatherSearch.txt and Gather3Search.txt should be
     part of this install package.
* Event file - a file containing lines having liturgical year, liturgical event and song title
     suggested for that event.  SongSuggestions.txt and PsalmSuggestions.txt are provided to
     get you started. 
* Readings File - a file containing lines that lists the readings for each liturgical year event and 
     a short description of the topuic of the reading.
* Antiphons and Sequences File - a file containing the sequences (or lack thereof) and antiphons for
     all liturgical events.


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

### File Format for Readings File
    text File with | as delimiter
    Liturgical year | Liturgical event | which reading | author and verses | topic
    B | 13th Sunday in Ordinary Time | First Reading | Wisdom 1:13-15; 2:23-24 | God did not make death

### File Format for Sequence and Antiphons
    text file with | as delimeter
    Liturgical year | Liturgical event | antiphon?Sequence | when | antiphon/sequence
    B | 13th Sunday of Ordinary Time | antiphon | Opening | Ps 47 (46):2
    B | 13th Sunday of Ordinary Time | sequence | none | none


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
     music book code
     Weekend Saturday mass time(s)
     Weekend SUnday Mass times
     Holyday mass times
     Holyday vigil Mass times

### Music Director
    name
    initials
    music book(s) code
    number of music books and number of songs in each music book
     
### Songs Used
     date
     time
     lityr
     event
     masspart
     songbook
     song title
### Readings
    lityr
    event
    masspart
    reading
### Responsorial Psalm
    lityr
    event
    responsorial psalm with refrain
### antiphons/sequences
    lityr
    event
    antiphon/sequence
    location
    antiphon or sequence
