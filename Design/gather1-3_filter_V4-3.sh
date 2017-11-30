#! /bin/bash
#
# current version 4.2 altered for G3
# Version 4.2a August 2017 Edward Birdsall
# Version 4.2 July-August 2017 Edward Birdsall 
# Version 4.1 July 2017 Edward Birdsall
# Version 4.0 July 2017 Edward Birdsall
# Version 3.0 February 2017 Kris Kehrer and Edward Birdsall 
# Version 2.0 November 2016 Edward Birdsall
# Version 1.0 Kris Kehrer
#===============================================================================
# Introduction
#-------------
# This script is to assist the Music Director in taking the list of songs for
# an event from the http://www,npm.org site and paring it down to just those
# songs found in Gather Comprehensive third edition.  It does this by;
#     1. deleting old version of the files in use
#     2. opening vim so that the user can paste the list of songs from the
#            website into a text file for parsing
#     3. using grep to remove all the songs not found in Gather Comprehensive
#     4. check to see if grep removed all songs.  If it did set altPath
#     5. go through the file and find all the song titles and then print out all
#          songs with that title.  If using altPath take the resulting into and
# 	   the normal file will have the found songs and others will go into another file
#     6. Tell the user if using normal or altPath 
#     7. using mousepad open up the new file so the user can cut and paste
#
#===============================================================================
# Version 2 added parsing of the grep'd file to remove all but the Gather
# Comprehensive listing for the song and formatting the line for easier use
# by Kris Kehrer.  It also added comments and user operating informtion.
#===============================================================================
# Version 3 corrected a problem with version which gave incorrect results while
# trying to allow multiple song values with the same title in the same songbook.
# Version 3-1 accounted for more than one space preceding GC but still had an
# error if there was no number.
# Version 3-2 added the songCheck function which eliminated preceding spaces from
# the SONG title and also checked that the resulting SONG was long enough to have
# a number.  This simplified the checking of SONG and eliminated songs without
# numbers.  Hopefully no song book will be ever coded by NPM as ZZ ;-)
# Version 3-3 fixed a minor formatting error in the printf statement.
# Version 3-4 turned out to be a debug test of NPM and printed out a test files
# to see if the NPM format issues could be overcome.  COUNTER now begins at 1 and
# there is a check to see if something printed for the song and if not print a
# line with GC ? and the songtitle to indicate "need a human to resolve".
# Version 3-5 just removed a lot of commmented out lines from prior versions and
#  the debug printf statements.  Inconsistant Formatting Requires AI or Human to
#  overcome.
# Version 3-6 was a major function revamp to try and handle the inconsistant
#     formatting on the NPM site.
# Version 3.6a was a stopgap edition to take care of things while puzzling out
#     how to handle bad formatting and bad data.
# Version 3.6b is a patch and added a step to open mouspad to let the user check
#     the grepped file to look for human errors on input to allow the script to
#     function.
# Version 3-7 was an editorial version where major commented out code was removed
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Version 4 takes a new tact in trying to get this accomplished.  The humans, no
#  script would be so poor in output, are so bad at setting up the NPM output that
#  earlier versions could not possibly figure out all the typo's, misprints and
#  erratic format.  However it appears that the one thing that stays consistant is
#  the titles.  So version 4 will take the grep'd file determine the title and then
#  from data and title set up the output with number and title.  4-00 has lots of
#  unused code and 4-0 has the unused code removed for clarity.  Uses GCSongs.txt
#  to go from title to title and song number(s).  GCSongs.txt was initially compiled
#  using the information from the 2016-2017 Year A data.  Ideally it will eventually
#  contain all the song titles in Gather Comprehensive.
# Version 4-0 is a 95% solution.  The humans entering the data still botch and typo
#    the titles but near as much as the rest of the line.  Some songs are entered
#    for Gather Comprehensive that are not there.
# Version 4.1 shifted the file structure of GCSongs to allow for standardized output
#     in spite of the multiple search titles used. 
# Version 4.2 checks to see if npm-list1 is empty, i.e. no GC songs were noted. If
#	npm-list1 is not empty then proceed else altPath is TRUE.  With AltPath TRUE
#       then the usual title search and printout is done but songs not found are dumped
#       into npm-list3 for the user's review.  Both list3 and list2 are combined into
#       npm-list4.txt so the user can see found and not found all at once
#===============================================================================   
#Proposed or under consideration updates
# Version 5 - add profile file which will contain which song books in use
#             also add profile setup script to set up and update profiles
#             may also output a file with the date for use so many can be done 
# Version 6 - may add python script to get the information from web pages
#             check LibreOffice to see if a template file which will automatically
#             add if the songs and such if properly denotes in a song file
#===============================================================================
#Files used(all hidden in . files):
#     npm-list   file with copied input from npm.org
#     npm-list1  file with npm-list passed through grep filter
#     npm-list2  file with parsed output
#     npm-list3  file with no located songs from altPath TRUE
#     npm-list4  file that has the contents of npm-list2 and npm-list3
#     GCSongs    file with GC song search titles and numbers
#     GCSIndex	 file with GC songs and Print titles
#===============================================================================
#
# Step 0 - set up necessary function(s)
# =====================================
inputSongs4Search ()
{
IN_FILE=$SearchFyle

# Link filedescriptor 10 with stdin
exec 10<&0
# stdin replaced with a file supplied as a first argument
exec < $IN_FILE

	oldIFS=$IFS  #In case the directory name has a space in it need to reset IFS 
#					for a moment
	IFS=$(echo -en "|\n")
	COUNTER=0
	GSNUM[0]='0'
	while read -a LINE
	do
		let COUNTER=COUNTER+1
		G3S2[COUNTER]="0"
		G3S3[COUNTER]="0"
		G3S4[COUNTER]="0"
		G3S5[COUNTER]="0"
		STITLE[COUNTER]=${LINE[0]}
		GSNUM[COUNTER]=${LINE[1]}
		G3S1[COUNTER]=${LINE[2]}
		if [ "${GSNUM[COUNTER]}" -gt "1" ] ; then
			G3S2[COUNTER]=${LINE[3]}
		fi 
		if [ "${GSNUM[COUNTER]}" -gt "2" ] ; then
			G3S3[COUNTER]=${LINE[4]}
		fi 
		if [ "${GSNUM[COUNTER]}" -gt "3" ] ; then
			G3S4[COUNTER]=${LINE[5]}
		fi 
		if [ "${GSNUM[COUNTER]}" -gt "4" ] ; then
			G3S5[COUNTER]=${LINE[6]}
		fi 
	done
	ARRLEN=$COUNTER
     	IFS=$oldIFS
}
#-------------------------------------
inputSongTitles ()
{
IN_FILE=$PrintFyle

# Link filedescriptor 10 with stdin
exec 10<&0
# stdin replaced with a file supplied as a first argument
exec < $IN_FILE

	oldIFS=$IFS  #In case the directory name has a space in it need to reset IFS 
#					for a moment
	IFS=$(echo -en "|\n")
	COUNTER=0
	GSNUM[0]='0'
	while read -a LINE
	do
		let COUNTER=COUNTER+1
		GINUM[COUNTER]=${LINE[0]}
		PTITLE[COUNTER]=${LINE[1]}
	done
	IARLEN=$COUNTER
     	IFS=$oldIFS
}
#-------------------------------------
locateSTitle ()
{
	FoundIt='FALSE'
	if [ "${FLINE:0:1}" == '*' ] ; then
		STARTPOS=1
	else
		STARTPOS=0
	fi
	LOC=0
	while [ "$FoundIt" == "FALSE" ] ; do
		let LOC=LOC+1
		TLEN=${#STITLE[LOC]}
		if [ "${FLINE:$STARTPOS:$TLEN}" == "${STITLE[LOC]}" ] ; then
			FoundIt='TRUE'
		fi
		if [ "${LOC}" -eq "${ARRLEN}" ] ; then
			LOC=0
			FoundIt='TRUE'
		fi
	done
}
#------------------------------------
locateSNum ()
{
	GotIt='FALSE'
	POS=0
	while [ "$GotIt" == "FALSE" ] ; do
		let POS=POS+1
		if [ "${SNUM}" -eq "${GINUM[POS]}" ] ; then
			GotIt='TRUE'
		fi
		if [ "${POS}" -eq "${IARLEN}" ] ; then
			POS=0
			GotIt='TRUE'
		fi
	done
}
#------------------------------------
outputLines ()
{
	SNUM="0"
	if [ ${GSNUM[LOC]} -eq "0" ] ; then
		printf "$FLINE\n" >> .npm-list3.txt
	fi
	if [ ${GSNUM[LOC]} -gt "0" ] ; then
		SNUM="${G3S1[LOC]}"
		locateSNum
		printf "\t$GS# ${GINUM[POS]}\t${PTITLE[POS]}\n" >> .npm-list2.txt
	fi
	if [ ${GSNUM[LOC]} -gt "1" ] ; then
		SNUM="${G3S2[LOC]}"
		locateSNum
		printf "\t$GS# ${GINUM[POS]}\t${PTITLE[POS]}\n" >> .npm-list2.txt
	fi
	if [ ${GSNUM[LOC]} -gt "2" ] ; then
		SNUM="${G3S3[LOC]}"
		locateSNum
		printf "\t$GS# ${GINUM[POS]}\t${PTITLE[POS]}\n" >> .npm-list2.txt
	fi
	if [ ${GSNUM[LOC]} -gt "3" ] ; then
		SNUM="${G3S4[LOC]}"
		locateSNum
		printf "\t$GS# ${GINUM[POS]}\t${PTITLE[POS]}\n" >> .npm-list2.txt
	fi
	if [ ${GSNUM[LOC]} -gt "4" ] ; then
		SNUM="${G3S5[LOC]}"
		locateSNum
		printf "\t$GS# ${GINUM[POS]}\t${PTITLE[POS]}\n" >> .npm-list2.txt
	fi
}
#===============================================================================================
#===============================================================================================
#
# Step 1 - remove previous used files and set a print variable
# ============================================================
cd
rm -f .npm-list.txt
rm -f .npm-list1.txt
rm -f .npm-list2.txt
rm -f .npm-list3.txt
rm -f .npm-list4.txt
PSep='------------------------------------------------------------------'

# Step 2 - Have user open up a browser and go to the correct web page
# ===================================================================
echo 'Greetings'
echo 'Welcome to gather3_filter Version 4.2'
echo '===================================='
echo 'This script is to help you set up your songs for an event like Easter or a Sunday.'
echo 'I have cleaned out older files that have been used.'
echo 'Which Liturgical Year is this for (A, B, C)?'
read LYR 
#echo "Liturgical year is $LYR"
echo 'Which Sunday or Event is this for? Example Advent 1, Easter:'
read Event
#echo "Event is $Event"
     printf "Song list for Liturgical Year $LYR  $Event \n $PSep \n" > .npm-list2.txt
     printf "\n $PSep \n Songs not found for this week \n $PSep \n" > .npm-list3.txt
echo 'WHich songbook are you using?'
echo '     1) Gather Comprehensive (default)'
echo '     2) Gather 3'
read songBook
if [ $songBook -eq "2" ] ; then
	SearchFyle='.Gather3Search.txt'
	PrintFyle='.Gather3Print.txt'
	GS='G3'
else
	SearchFyle='.GatherSearch.txt'
	PrintFyle='.GatherPrint.txt'
	GS='GC'
fi 

echo 'First step is to get your browser to the right web page to copy out song suggestions.'
echo 'Please open up a browser and go to http://www.npm.org/Planning/index.html.'
echo 'Then select the correct liturgical year and then select the event of interest.'
echo 'Finally scroll down to Music Suggestions Songs for the liturgy'
echo ' '
echo 'When this is done press return'

read KYE

# Step 3 - Using vim set up the file with the pasted info from the browser 
# ========================================================================
echo 'Now that you are ready with the browser we will open a file for input using vim'
echo 'First enter insert mode by typing  i   and then cut and paste from the web page'
echo 'into the document the suggested songs listing.  Then hit the Escape key to exit insert'
echo 'mode and type    :wq   to write the file and exit.'
echo ' '
echo 'press return to begin'

read KYE

vim .npm-list.txt

# Step 4 - grep file and have user check it
# ==========================================
echo 'I am now going to use grep to eliminate all lines that do not have songs in'
echo 'Your chosen songbhook.  The I am going to parse that file to set the entries'
echo 'for copying into your final document'
echo ' '
echo ' '
echo 'Invoking grep now'

#grep "G3 " .npm-list.txt > .npm-list1.txt
grep "ZZZZ " .npm-list.txt > .npm-list1.txt

if [ -s .npm-list1.txt ] ; then
	altPath='FALSE'
	echo ' '
	echo ' ' 
	echo 'finished with grep and now proceeding'
	echo "You should see at least: `wc -l .npm-list1.txt` songs"
else
	altPath='TRUE'
	echo ' '
	echo 'Drat it all!  Drat it all!  Drat it all! Drat it all! ' 
	echo 'finished with grep  *********** grep did not find GC so'
	echo 'Now proceeding with alternate search method'
	echo 'The resulting file will show you what I could locate and then all the rest'
	echo '**************************************************************************' 
	cp .npm-list.txt .npm-list1.txt
fi


#Step 5 - parsing the file
#=========================
echo 'Now to parse the file for you' 
echo 'Reading in files of Gather Comprehensive song titles and numbers'
	inputSongs4Search
	inputSongTitles

# Begin parsing .npm-list1.txt and output to .npm-list2.txt and .npm-list3.txt
IN_FILE=".npm-list1.txt"

while read line ;
do
	FLINE="$line"
	locateSTitle
	outputLines
done   < "$IN_FILE"

echo 'parsing complete!  Now to show you the results'
echo ' '

cat .npm-list2.txt .npm-list3.txt > .npm-list4.txt

# Step 6 - open file up with mousepad so can cut and paste into final document
# =======================================================================
#echo ' '
#echo ' Now open up your document and get ready to start cutting and pasting'
#echo ' hit return when ready to edit and I will open the parsed file for you'
#echo ' Do not forget to close mousepad when done'
#echo ' '
#read KYE

mousepad .npm-list4.txt

echo 'Goodbye     Goodbye     Goodbye   End of script'
echo '==============================================='

exit 0
