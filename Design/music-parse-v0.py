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
from time import sleep
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

# Now function definitions
# ==============================
def findTitle(the_line, Cpos, Song_Title):
     pass
def findSong(the_line, Cpos, SongBook, Song_Book, Song_Number):
     pass
def setOutputLine(Line_Number, Song_Title, Song_Book, Song_Number, Lyne_Out):
     pass
#    Lyne_Out = repr(Line_Number) + '\t' + repr(Song_Book, Song_Number) + '/t' +repr(Song_Title)

# ======================================================================================================================
# =========================================
# =====     User I/O General Area     =====
# =========================================

def Greet_User():
     """
     Just a display with opening greeting and explanation of process
     """
     print(GREETINGS)
     sleep(10)

def Which_Event():
     """
     Initially just ask for the Liturgical Year and event but later will be a selector
     """
     pass
def Which_Songbook():
     """
     Initially ask but later look in profile.  Initial options are GC or G3 or both
     """
     pass
def Input_Arrays():
     """
     Input Print and Search Arrays for GC and G3
     """
     pass
# =========================================
# =====     User I/O General Area     =====
# =========================================
# ======================================================================================================================
# ========================================
# =====     NPM Suggestions Area     =====
# ========================================
def Input_NPM_Suggestions():
     """
     Set up a text box for the user to paste suggestions.  There may be sections (groupings of songs for various
     purposes).  These groupings will always have Psalm and Songs but may have others.  ?? ID by starting with a
     character (??)??  Save in a line by line array?
     """
     pass
def Search_NPM_Suggestions():
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
     """while line in InFyleLine :
          Line_Number = Line_Number +1
          the_line = line.readline()
          findTitle
          findSong
          setOutputLine
          OutFyleLine.write(Lyne_Out)
     """
     pass
def Display_NPM_Suggestions():
     """
     Display a mutable view of NPM Suggestions; first known then unknown.  Allow user to delete false positives and
     change unkown to a known format.  Allow for sections in display
     """
     pass
def Fyle_Output_NPM_Suggestions():
     """
     Save to file formatted NPM Suggestions
     """
     pass
def Print_Output_NPM_Suggestions():
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
Greet_User()
# Which_Event()
# Which_Songbook()
# Input_Arrays()
# Input_NPM_Suggestions()
# Search_NPM_Suggestions()
# Display_NPM_Suggestions()
# Fyle_Output_NPM_Suggestions()

# All Done - Goodbye
# ===================


#=======================================================================================================================
#==========          Code Ends here          ==========          ==========          Code Ends here          ===========
#=======================================================================================================================
