/* ****************************************************************************************************************** */
/*	Program: Liturgical Music Suggestions
/*	Date of Current Revision: 2017
/*	Current Revision: 0.1
/*
/*	Program Function
/*		This programs is to assist a Roman Catholic Music Director in preparing music for events for his parish.    */
/*		It will have a database listing of all standard events in the Roman Catholic Liturgical Year along with any */
/*		additional that the parish may observe.  For each event, comprised of liturgical year and event such as Year*/
/*		B, Second Sunday in Ordinary Time, there will be a growing database of suggestions for the event.  For all  */
/*		the songbooks in use by the parish there will be a database of a) song number, title and b)search titles and*/
/*		related song numbers.  
/* ****************************************************************************************************************** */
/* A few Definitions */
typedef struct event{
				char	litYr;
				char	title[];
				} event_t;

typedef struct suggestion{
				char songBook[5];
				int	songNumber;
				char songTitle[];
				} suggestion_t;

typedef struct searchSong{
				char	searchTitle[];
				char songBook[5];
				int	songNumber[5];
				} searchSong_t;

typedef	struct eventSuggestion{
				event_t		theEvent;
				suggestion_t	theSuggestion;
				} eventSuggestion_t;