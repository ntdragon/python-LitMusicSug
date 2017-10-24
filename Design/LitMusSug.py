#! /usr/bin/python3

# Begin outline here
#
# Main sequence
# ------------------
# Check to see if this has been initialized, if not then start inialization process
# if profile exists then goto main menu else
#      1. Initialize profile
#         a. Parish name
#         b. songbooks in use (import npm songbooks and then ask if in there or add additional)
#              parish songbook to be set as PARISH0 initially, later on others may be assed with 0++
#                              is for original works by music Director or special collections not in
#                                 standard songbook in use by parish
#         c. Templates and event type
#              1. Weekend Masses
#              2. Holy Day with/Without Vigil
#              3. Special ones like Easter and Christmas
#      2. Initialize suggestion (song and psalm) database and import standard suggestions
#      3. Initialize songbook database and import songbook print and search files for songbooks in use
#          if songbooks unknown (ie not GC or G3) then ask user for file to import for print
#      4. Import events and set in events database, ask user for other events
#
# MAIN Menu
# =========
# suggestions for event
#     Select event, liturgical year
#     from database locate and display suggestions
#     based on event select template and present to user to put in suggestions or enter in their own
#           if entering their own then add to database for use next time
# import suggestions for event
# edit profile
#	add / change songbooks  (if add then import songbooks)
# ? 

# ======================================================================================================================
# ================================          Program View Functions          ============================================
# ======================================================================================================================
def textView
"""
"""
def screenView
"""
"""
def webVIew
"""
"""
# ======================================================================================================================
# ================================          Program Data Functions          ============================================
# ======================================================================================================================
def parishProfile
"""
"""
def parishTemplates
"""
"""
def songDatabase
"""
"""
# ======================================================================================================================
# ==================          Main Controller          ==========          Main Controller          ====================
# ======================================================================================================================
#
# Main Controller
# =====================
# Program Initialization
# ----------------------
#      Check for initialized files, if there are then import else run initialization process
#     Initialization Process - 
#          initialize profile
#          initialize suggestions
#          import parish songbooks
#
# Main menu
# ----------------------
#       How invoked - action already selected?
#       What action?
#          request suggestion
# Done - exit
# ======================
#
# ======================================================================================================================
# ==========     The End of Liturgical Music Suggestion     =====================     The End of LitMusSug     =========
#=======================================================================================================================