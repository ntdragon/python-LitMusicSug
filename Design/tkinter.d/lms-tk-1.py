"""
Liturgical Music Suggestions application using TKinter v0.1
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv

# Configure the root window
root = tk.Tk()
root.title('Liturgical Music Suggestions v0.1')
root.geometry('1000x1200')
root.columnconfigure(0, weight=1)

GREETINGS = """ Greetings
====================
     Welcome to Music Suggestions Version 0.1

     This program is to assist you in setting up your songs for an event at church with suggestions you
     gather from NPM or other sources.

     Initially you will be asked for the Liturgical Year and what event (like First Sunday of Advent)
     and then for the suggestions in the same format as the NPM webpage.
"""

LARGE_FONT = ("Times", 12)
NORMAL_FONT = ("Times", 10)
SMALL_FONT = ("Times", 8)

PARISH = ""
LITURGICAL_EVENT = ""
LITURGICAL_YEAR = ""

def PageOne















root.mainloop()
