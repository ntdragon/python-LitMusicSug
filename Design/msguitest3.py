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

PARISH = ""
LITURGICAL_EVENT = ""
LITURGICAL_YEAR = ""

class MusSugWin(Tk):
     """
     Main Window for testing and then program
     """
     def __init__(self, *args, **kwargs):

          Tk.__init__(self, *args, **kwargs)
          self.geometry('1000x1200')
          self.title('Music Suggestions GUI Test')
          self.iconbitmap('@/home/ntdgn/WIP-Programming.d/python.d/py-blue-trans-out.xbm')
          container = Frame(self)

          container.pack(side="top", fill="both", expand=True)

          container.grid_rowconfigure(0, weight=1)
          container.grid_columnconfigure(0, weight=1)

          self.frames = {}

          for frehme in (StartPage, PageOne, PageTwo):
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

          button = Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
          button.pack()

          button2 = Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
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

          button2 = Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
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
          self.psalm_sugs = ScrolledText(parent=self, text='Psalm Suggestions entered here')
#          label = Label(self, text="                        ", font=LARGE_FONT).pack(pady=10, padx=10)
          label = Label(self, text="Song Suggestions Here", font=LARGE_FONT).pack(pady=10, padx=10)
          self.song_sugs = ScrolledText(parent=self, text='Song Suggestions entered here')

          button1 = Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
          button1.pack()

          button2 = Button(self, text="Initial Entry", command=lambda: controller.show_frame(PageOne))
          button2.pack()


#==============================================================================================

app = MusSugWin()
app.mainloop()
