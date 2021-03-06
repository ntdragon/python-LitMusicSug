#!/usr/bin/python3
"""
     Music Parse GUI testing before incorporation into program
"""
#import tkinter as tk
from tkinter import *
from pp4egui import *

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

class MusSugWin(Tk):
     """
     Main Window for testing and then program
     """

     PARISH = ""
     LITURGICAL_EVENT = ""
     LITURGICAL_YEAR = ""

     def __init__(self, *args, **kwargs):

          Tk.__init__(self, *args, **kwargs)
          self.geometry('1600x1800')
          self.title('Music Suggestions GUI Test')
          self.iconbitmap('@./py-blue-trans-out.xbm')
          container = Frame(self)

          container.pack(side="top", fill="both", expand=True)

          container.grid_rowconfigure(0, weight=1)
          container.grid_columnconfigure(0, weight=1)

          self.frames = {}

          for frehme in (StartPage, PageOne, PageTwo, PageThree, PageFour ):
               frame = frehme(container, self)
               self.frames[frehme] = frame
               frame.grid(row=0, column=0, sticky="nsew")

          self.show_frame(StartPage)

     def show_frame(self, cont):
          """
          """
          frame = self.frames[cont]
          frame.tkraise()

class StartPage(Frame):
     """
     MusSugWin calls this first to start things off
     """
     def __init__(self, parent, controller):
          Frame.__init__(self, parent)
          label = Label(self, text=GREETINGS, font=LARGE_FONT)
          label.pack(pady=10, padx=10)

          button = Button(self, text="Start", command=lambda: controller.show_frame(PageOne))
          button.pack()

          button2 = Button(self, text="Quit", command=lambda: Frame.quit(self))
          button2.pack()


class PageOne(Frame):
     """
     First page of gathering information
     """

     def __init__(self, parent, controller):
          Frame.__init__(self, parent)
          label = Label(self, text="Input Values for Program", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="                        ", font=LARGE_FONT).pack(pady=10, padx=10)

          # text box for parish here
          label = Label(self, text='1) Please Enter Your Parish Name', font=LARGE_FONT).pack(pady=10, padx=10)
          parnm = "St Roch Catholic Church"
          e0 = Entry(self, textvariable=parnm)
          e0.pack()
          e0.focus_set()
#         e.delete(0, END)
          e0.insert(0, "Enter parish name here")
          parnm = e0.get()
          #TODO: need more code here?

          # radio buttons for Liturgical Year here
          label = Label(self, text="2) Please Select Liturgical Year", font=LARGE_FONT).pack(pady=10, padx=10)
          lityr = "A"
          Radiobutton(self, text="Liturgical Year A", variable=lityr, value="A", indicatoron=1).pack()
          Radiobutton(self, text="Liturgical Year B", variable=lityr, value="B", indicatoron=1).pack()
          Radiobutton(self, text="Liturgical Year C", variable=lityr, value="C", indicatoron=1).pack()

          # a text box for liturgical events here - shift to listbox&scroll bar for Music Sug
          label = Label(self, text="3) Please Enter the liturgical event", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="Example: First Sunday in Advent", font=LARGE_FONT).pack(pady=10, padx=10)
          litevt = "First Sunday in Advent"
          e1 = Entry(self, textvariable=parnm)
          e1.pack()
          e1.focus_set()
#         e.delete(0, END)
          e1.insert(0, "Enter liturgical event here")
          litevt = e1.get()
          #TODO: need more code here?

          label = Label(self, text="                        ", font=LARGE_FONT).pack(pady=10, padx=10)
          button1 = Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
          button1.pack()
          button2 = Button(self, text="Next", command=lambda: controller.show_frame(PageTwo))
          button2.pack()


#          return(parnm, lityr, litevt)

class PageTwo(Frame):
     """
     Text box entries for Psalms and Songs
     """
     def __init__(self, parent, controller):
          Frame.__init__(self, parent)
          label = Label(self, text="Suggestions from NPM", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="Psalm Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.psalm_sugs = ScrolledTextV(rows=10, parent=self, text='Psalm Suggestions entered here, vertical bar after title')
#          label = Label(self, text="                        ", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="Song Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.song_sugs = ScrolledTextV(rows=40, parent=self, text='Song Suggestions entered here, put vertical bar after title')

          button1 = Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
          button1.pack()

          button2 = Button(self, text="Initial Entry", command=lambda: controller.show_frame(PageOne))
          button2.pack()

          button3 = Button(self, text="Next", command=lambda: controller.show_frame(PageThree))
          button3.pack()


class PageThree(Frame):
     """
     This page just show progress for all the various other tasks that need to be done before
          proceding on to the the final page.  A bit crude code but slowly learning
          Tasks:
               Input Search and Print for Both Songbooks
               parse psalms into known and unknown with known into print formatted and unknown raw
               parse songs into known and unknown similar to psalms
     """
     def __init__(self, parent, controller):
          Frame.__init__(self, parent)
          label = Label(self, text="Processing Suggestions", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="Inputting information from files", font=LARGE_FONT).pack(pady=10, padx=10)
          '''
          #TODO: If db set up then input db
          gcprint = infyle_print('.gcprint.txt')
          g3print = infyle_print('.g3print.txt')
          gcsearch = infyle_search('.gcsearch.txt')
          g3search = infile_search('.g3search.txt')
          #FIXME: Input from files Songbook Print and Search files - is this code correct
          '''
          label = Label(self, text="Songbook Information read, begin parsing", font=LARGE_FONT).pack(pady=10, padx=10)
          #TODO: Parse the psalms then song suggestions

          label = Label(self, text="Ready to display", font=LARGE_FONT).pack(pady=10, padx=10)
          #FIXME: add command to go to next page here?

          button1 = Button(self, text="Back", command=lambda: controller.show_frame(PageTwo))
          button1.pack()

          button2 = Button(self, text="Next", command=lambda: controller.show_frame(PageFour))
          button2.pack()
'''
#----------------------------------------------------------------------------------------------
TABLE
     #entry for search a dictionary with title as key
     #entry for print a dictionary with inum as key
     def infyle_search(infile,?) #FIXME: need to validate this  do I need to return entry
          for line in infile:
               title, num, snums = line.split("|") #FIXME: Need to check with Mike what happens when more than 1 song

          num = num.strip()
          inum = int(num)
          title = title.strip()
          #TODO need to add code for 1 to n songs returned
          
     def infyle_print(infile,?) #FIXME: need to validate this  do I need to return entry
          for line in infile:
               num, title = line.split("|")

          num = num.strip()
          inum = int(num)
          title = title.strip()
          if all([v == '0' for v in num]):
               continue
          if all([v == '9' for v in num]) and title.startswith("End of Song"):
               continue
          entry = (inum, title)


     def parse_it(?)
     def set_print()
     '''



class PageFour(Frame):
     """
     Text box output for Psalms and Songs both known and unknown
     """
     '''
     gc = "From Gather Comprehensive"
     g3 = "From Gather 3"
     ps = "Psalm Suggestions"
     ss = "Song Suggestions"
     '''
     def __init__(self, parent, controller):
          Frame.__init__(self, parent)
          label = Label(self, text="Suggestions from NPM for ****", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="Psalm Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.psalm_sugs = ScrolledTextV(rows=10, parent=self, text='Known Psalm Suggestions will be here ')
          label = Label(self, text="Unknown Psalm Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.psalm_sugs = ScrolledTextV(rows=2, parent=self, text='Unknown Psalm Suggestions here')

          label = Label(self, text="Song Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.song_sugs = ScrolledTextV(rows=20, parent=self, text='Link to known Song Suggestions here')
          label = Label(self, text="Unknown Song Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.song_sugs = ScrolledTextV(rows=2, parent=self, text='Link to unknown Song Suggestions here')

          
          button1 = Button(self, text="Do Another", command=lambda: controller.show_frame(PageOne))
          button1.pack()

          button2 = Button(self, text="Done", command=lambda: Frame.quit(self))
          button2.pack()


#==============================================================================================

app = MusSugWin()
app.mainloop()
