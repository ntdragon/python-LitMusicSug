# Getting Started Guide

## Introduction

Welcome to the Liturgical Music Suggestion program.  This program started life as an increasingly complicated Bash script to take suggestions from National Association of Pastoral Musicians website, find those that were in the songbook in use and format them cutting and pasting them into the weekly Mass songs sheet used by the parish musicians.  To that was
added having a database of past suggestions and songs used over the years.  This program is designed to be an assist to Roman Catholic Music Directors and musicians who are tasked with setting up music to be used at Mass on Sundays and Holy Days.  The program will get input from its own database plus allow for suggestions from NPM and other sources to be added.

## Guide to Directories and Files provided

### Documentation

This directory contains the documentation about the program.  Files here are;

* Getting Started Guide - This document gives instructions for setting up the program initially using the files provided.  Also a quick example of how to use the program when set up.
* User Guide - This document guides the user in how to use the program and features.
* Advanced User Guide - This document describes how to create and setup files for use in
     adding songbooks, creating a template for your parish and other customizations.
* Program Documention - This is a in depth detailed description of the program and how it is designed to work.

### Initial

This directory is the source directory for the initial files to set up the program and is also the directory used for files that contain customizations for your parish.

### src

This directory contains the program files themselves.

## Initial Setup files

This program comes with a few files that were used in the design, development and testing of the program but you may need to create and set up some text files for for your parish.

The initial files needed to set up the programs database are;

* Songbook file - a file containing the song numbers song titles and are they a Psalm, Part or Song.  Provided with the program should be GatherPrint.txt and Gather3Print.text which are for Gather Comprehensive and Gather Comprehensive Third Edition respectively.
* Search file - a file containing song titles or first lines of songs and which song numbers they are for a particular book.  GatherSearch.txt and Gather3Search.txt should be part of this install package.
* Event file - a file containing lines having liturgical year, liturgical event and song title suggested for that event.  SongSuggestions.txt and PsalmSuggestions.txt are provided to get you started. 
* Print template files - files that are used to create a formatted printed output from the program.  SingleMass.txt, EasterVigil.txt and Weekend.txt are provided to give you a starter set. 
## First Time Use

## Example Normal Use

## Now What

This document is to get you up and running with the Liturgical Music Suggestion Program.  More documentation on normal use is in the User Guide.  Setting up files to add more songbooks or customizing the printouts is documented in the Advanced User Guide.  Finally, Detailed Program Documentation documents all the code and design thoughts so that you could extend and enhance the program for your needs.