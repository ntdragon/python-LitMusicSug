#Music Parsing - V4
#
#python3
#
# Assumptions:
# ============
# File from NPM web page has been copied, grepped ?and reviewed?
# .npm-1.txt for input, .npm-2.txt for output
#
# Process
# =======
# From First to last line
# Steps 1 - Read in line
#       2 - find title
#       3 - locate songbook and song number
#       4 - write out line number, tab, song book, song, tab title
# end
#
#===============================================================================
# 
# Imports here

#Now function definitions
def findTitle(the_line, Cpos, Song_Title):

def findSong(the_line, Cpos, SongBook, Song_Book, Song_Number):

def setOutputLine(Line_Number, Song_Title, Song_Book, Song_Number, Lyne_Out):
    Lyne_Out = repr(Line_Number) + '\t' + repr(Song_Book, Song_Number) + '/t' +repr(Song_Title)  


#A few variable definitions here
Input_Fyle = '.npm-1.txt'
Output_Fyle = '.npm-2.txt'
Song_Title = ''
Song_Book = ''
Song_Number = ''
Line_Number = 0
Num_Songbooks = 1
SongBook_1 = 'GC '
InFyleLine = open(Input_Fyle,'r')
OutFyleLine = open(Output_Fyle,'w')

#Now let us get it done
while line in InFyleLine :
    Line_Number = Line_Number +1
    the_line = line.readline()
    findTitle
    findSong
    setOutputLine
    OutFyleLine.write(Lyne_Out)
    .
lyneOut = '