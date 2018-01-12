#! /usr/bin/python3
#
# Liturgical Music Suggestions Version 0.1   2017  Edward Birdsall
# ======================================================================================================================
""" This program is to closely mimic the Bash Script gather1-3_V4-3.sh in function and use.  This is to give myself the
	basic start on writing python programs and will be the prelude to LitMusSug which will be the databased followup
	program to this.

Assumptions and defaults:
	Prior to start the NPM page for songs has been copied into npm-list.txt
	npm-list1.txt will either be a grep'd listing of songs or all the songs from npm-list.txt
	npm-list2, npm-list3 and npm-list4 to be open for write to eliminate prior entries in them
	npm-list2.txt will be located songs - if both songbooks are used then 2a and 2b will be used
	npm-list3.txt will be other songs
	npm-list4.txt will be the listing containing npm-list2.txt and npm-list3.txt
	GatherSearch.txt and Gather3Search.txt will be the search files for Gather Comprehensive and Gather 3 respectively
	GatherPrint.txt and Gather3Print.txt will be the print files for Gather Comprehensive and Gather 3 respectively

Process
	1. greet user and ask for liturgical year and event title
	2. Ask which songbook to use or both
	3. Input the search and print information for songbook(s)
	4. Now from first to last line in npm-list1.txt
		Read in line from npm-list1.txt
		Try to locate song in Search array
			if song located then grab song number(s) and write out song number and print title to npm-list2
			if song not located then write line to npm-list3
	5. Close files
	6. Now input files npm-list2 and then npm-list3 and outputthe results to npm-list4
	7. Display the contents of npm-list4 in a text box for use
	8. exit
"""
#=======================================================================================================================
#==========          Code to start here          ==========          ==========          ==========          ===========
#=======================================================================================================================
# Imports here
# ==============================
# Standard Library imports
# ------------------------
from time import sleep
#import argparse
#import sys
from tkinter import *

# Related Third Party Imports
# ---------------------------

# local imports
# -------------

# =========================================
# =====     Global Constants Here     =====
# =========================================
GREETINGS = """ Greetings
====================
     Welcome to Music Suggestions Version 0.1
     This program is to assist you in setting up your songs for an event at church with suggestions you
     gather from NPM or other sources.
     Initially you will be asked for the Liturgical Year and what event (like First Sunday of Advent)
     and then for the suggestions in the same format as the NPM webpage.
"""
LITURGICAL_YEARS = ['A', 'B', 'C']

# Now function definitions
# ==============================
def find_title():
     """ In suggestions find the title using the search info
          the_line, cpos, song_title
     """
     pass
def find_song():
     """ locate the songs in the songbook
          the_line, cpos, songbook, song_book, song_number
     """
     pass
def set_output_line():
     """ Set up the appropritate output line to file
          line_number, song_title, song_book, song_number, lyne_out
     """
     pass
#    Lyne_Out = repr(Line_Number) + '\t' + repr(Song_Book, Song_Number) + '/t' +repr(Song_Title)

# ======================================================================================================================
# =========================================
# =====     User I/O General Area     =====
# =========================================

def greet_user():
     """
     Just a display with opening greeting and explanation of process
     """
     print(GREETINGS)
     sleep(1)

def which_event():
     """
     Initially just ask for the Liturgical Year and event but later will be a selector
     """
     liturgical_year = input('Which Liturgical Year [ A, B, C ] is this for?')
     liturgical_event = input('Which Liturgical Event is this for [example; First Sunday of Advent ]?')
     print('Liurgical Year is ', liturgical_year)
     print('Liturgical Event is', liturgical_event)
     return liturgical_year, liturgical_event
# Need to check Liturgical year valid or add a selector when GUI
# Need to add selector in GUI for valid events

def which_songbook():
     """
     Initially ask but later look in profile.  Initial options are GC or G3 or both
     """
#    songbooks_available[GC, G3, GC_G3]
     songbook = input('Which songbook are you using [ GC, G3, or both]')
     if songbook == 'GC':
          song_book = 'GC'
     elif songbook == 'G3':
          song_book = 'G3'
     elif songbook == 'both':
          songbook = 'GC_G3'
     else:
          song_book = 'GC'

     return song_book

def tk_screen0():
     """
     This screen is opening screen for the program.  It greets the user, and getrs some
     initial informations.  Liturgical year, liturgical event and songbooks in use.
     """
     main_window = Label(-text "Liturgical Music Suggestions")
     main_window.pack()
     








# =========================================
# =====     User I/O General Area     =====
# =========================================
# =========================================
# =====     File I/O General Area     =====
# =========================================


def input_print_file(file_name):
     """
     This inputs a file that contains two fields per line; song number then title to print
     """
     song_book_print = {}
     with open(file_name, 'r') as the_file:
          for line in the_file:
               num, title = line.split("|")
               num = num.strip()
               song_number = int(num)
               song_title = title.strip()
               song_book_print[song_number] = song_title
     return song_book_print

def input_search_file(file_name):
     """
     This inputs a file that contains a number of fields; first is search title, then number of songs matching that,
     the following fields contain the song numbers
     """
     song_book_search = {}

     with open(file_name, 'r') as the_file:
          the_lines = the_file.readlines()

     for line in the_lines:
          the_lyne = line.split("|")
          song_title = the_lyne(0)
          the_song_nums = [int(x.strip()) for x in the_lyne[2:]]
          song_book_search[song_title] = the_song_nums

     return song_book_search

def input_arrays():
     """
     Input print and search Arrays for GC and G3
     Files to import:
          GatherPrint.txt --> gc_print list
          GatherSearch.txt --> gc_search list
          Gather3Print.txt --> g3_print list
          Gather3Search.txt --> g3_search list
     """

     gc_search = input_search_file('GatherSearch.txt')
     gc_print = input_print_file('GatherPrint.txt')
     g3_search = input_search_file('Gather3Search.txt')
     g3_print = input_print_file('Gather3Print.txt')
     return gc_search, gc_print, g3_search, g3_print

# =========================================
# =====     File I/O General Area     =====
# =========================================0
# ======================================================================================================================
# ========================================
# =====     NPM Suggestions Area     =====
# ========================================
def input_suggestions():
     """
     Set up a text box for the user to paste suggestions.  There may be sections (groupings of songs for various
     purposes).  These groupings will always have Psalm and Songs but may have others.  ?? ID by starting with a
     character (??)??  Save in a line by line array?
     """
     pass
def search_suggestions():
     """
     Look through suggestions (first by title and then grep for songbook) and sort out known for the songbook
     If for both then GC first then G3
     ----------------------------------------
     For each songbook
     	for current line in npm suggestion array
          		if start of section then move to npm display array in both known and unknown areas else
     		try to see if current line starts with known suggestion
     			if known then look up and enter known(s) into npm display array
     				else loop until found or end, at end put into npm unknown part of display
     	loop till end of suggestion array
     next songbook or end
     """
     """
          while line in InFyleLine :
          Line_Number = Line_Number +1
          the_line = line.readline()
          findTitle
          findSong
          setOutputLine
          OutFyleLine.write(Lyne_Out)
     """

def display_suggestions():
     """
     Display a mutable view of NPM Suggestions; first known then unknown.  Allow user to delete false positives and
     change unkown to a known format.  Allow for sections in display
     """
     pass

def fyle_output_suggestions():
     """
     Save to file formatted NPM Suggestions
     """
     pass

def print_output_suggestions():
     """
     Print out formatted NPM Suggestions by song book
     """
     pass

# ========================================
# =====     NPM Suggestions Area     =====
# ========================================

#A few variable definitions here
#Input_Fyle1 = 'npm-1.txt'
#Output_GC_Fyle = 'npm-list2a.txt'
#Output_G3_Fyle = 'npm-list2b.txt'
#Output_un_Fyle = 'npm-list3.txt'
#Final_Output_Fyle = 'npm-list4.txt'
#Song_Title = ''
#Song_Book = ''
#Song_Number = ''
#Line_Number = 0
#Num_Songbooks = 1
#SongBook_1 = 'GC '
#SongBook_2 = 'G3 '
#InFyleLine = open(Input_Fyle, 'r')
#OutFyleLine = open(Output_Fyle, 'w')



# ==================================================================================================
# =====     MAIN Starts Here     =====     MAIN Starts Here     =====     MAIN Starts Here     =====
# ==================================================================================================
def main():
     """ Run as a command line program. """
     greet_user()
     the_year, the_event = which_event()
     the_songbook = which_songbook()
     gc_search, gc_print, g3_search, g3_print = input_arrays()
#TODO:    input_suggestions()
#TODO:    For each song book in use
#TODO:         Search_NPM_Suggestions()
#TODO:         Display_NPM_Suggestions()
#TODO:    Fyle_Output_NPM_Suggestions()

# All Done - Goodbye
# ===================

if __name__ == "__main__":
     main()
#=======================================================================================================================
#==========          Code Ends here          ==========          ==========          Code Ends here          ===========
#=======================================================================================================================
