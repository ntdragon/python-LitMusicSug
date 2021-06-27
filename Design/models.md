#Models for LitMusicSugg

##attributes

###SongbookSearch
     Title or first line: String
     songbook code: string
     Song numbers: integer
###SongbookPrint
     Songbook code: String 
     song number: integer
     Print Title: String
###EventSuggestion
     Event Title: String
     Liturgical Year: String (A,B,C, ABC)
     Song or Psalm:String
     Song Title or First Line: String
###Respnsorial Pslams
###Antiphons and Sequences
###Readings

##conversion from fyles
convertPrint(fyle,songbook,database)
     input fyle, songbook id and database
     process: input from fyle song numbers, song type and song title and load into database
     output: updated database
convertSearch(fyle,songbook,database)
     input fyle, songbook id and database
     process: input from fyle serch input, number of songs matching and list of song numbers and load into database
     output: updated database
convertEvent(fyle,database)
     input fyle, and database
     process: input from fyle LitYr, event name and song titles and load into database
     output: updated database

##database
findEvent(LitYr,event)
     input LitYr and event and returns a list of song titles
findTitle(song title, songbook)
     input a song title and songbook and returns a list of song numbers
findSong(songbook, songnumber)
     input a songbook and song number and returns a song title
findSuggestion(songbook,suggestion)
     input songbook and suggestion and returns a list of song numbers
updateEvent(Lityr,event,title)
     input Lityr, event and title and adds to database
updateSongbook(songbook,songnumber, songtype, songtitle)
     input all to add to database
updateSuggestions(songbook,searchtitle,songs)
     input all to add to database

##inputs
inputEvent(event,lityr,date)