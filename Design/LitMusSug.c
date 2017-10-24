/********************************************************************************/
/*********************************   include    *********************************/
/********************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include ""

/********************************************************************************/
/********************************     main      *********************************/
/********************************************************************************/
main()
{
	initialize_program();
	main_menu();
	exit_program();
}
/********************************************************************************/
/*****************************     the functions     ****************************/
/********************************************************************************/

/***********************/
/* level 0 functions   */
/***********************/
void initialize_program()
{
	initialize_parish_profile(profile);
	initialize_events(events);
	initialize_suggestions_database(suggestions);
	for (i=1;i<=numSongbooks;i++)
		import_songbook(profile.songbook(i));
	initialize_templates();
}
void main_menu()
{
	display_menu();
	switch (selection) {
		case 1: /* event preparation */
		case 2: /* edit parish profile */
		case 3: /* edit template */
		case 4: /* edit songbook */
	} 
}
void exit_program()
{
}

/***********************/
/* level 1 functions   */
/***********************/
void event_preparation(char songBooks[5][4]) /* 4 songbooks with id length 5 */
{
	event_t			theEvent;
	eventSuggestion_t	theSuggestions;
	char				songBooks[5][4];
	BOOL				err;

	theEvent = ask_event();
	thePsalmSuggestions = locate_psalm_suggestions(theEvent, songBooks);
	theSongSuggestions = locate_song_suggestions(theEvent, songBooks);
	present_suggestions(thePsalmSuggestions, theSongSuggestions);
	err = FALSE;
	return(err);
}
/***********************/
/* level 2 functions   */
/***********************/
string ask_event(void)
{
	event_t	theEvent;

	return(theEvent)
}
/***********************/
/* level 3 functions   */
/***********************/

/***********************/
/* level 4 functions   */
/***********************/

/***********************/
/* level 5 functions   */
/***********************/

/********************************************************************************/
/********************************     end     ***********************************/
/********************************************************************************/
	ImportEventSongSuggestions
	ImportEventPsalmSuggestions
	ImportSongbookTitles
	ImportSongbookSearch
	FindEventSuggestions
	ReadSuggestionsDatabase
	WriteSuggestionsDaTabase
	ReadPsalmDatabase
	WritePsalmDatabase
	ReadSongbookSearch
	WriteSongbookSearch
	ReadSongbookTitle
	WriteSongbookTitle




