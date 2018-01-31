#!\usr/bin/python3
"""
GUI Classes for use from Programming Python 4th Edition by Mark Lutz
"""

from tkinter import *

# ---------------------------------------------------------------------------------------------
def fetch1():
     """
     Fetch of a single entry from an entry box
     """
     print('Input => "%s"' % ent.get())             # get text

def fetch(entries):
     """
     Fetch of a set of entries from a set of entry boxed.  See makeform
     """
     for entry in entries:
          print('Input => "%s"' % entry.get())        # get text

def makeform(root, fields):
     """
     fields = 'Name', 'Job', 'Pay'   in PPE4 example need to set up fields as necessary
     """
     entries = []
     for field in fields:
          row = Frame(root)                           # make a new row
          lab = Label(row, width=5, text=field)       # add label, entry
          ent = Entry(row)
          row.pack(side=TOP, fill=X)                  # pack row on top
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
          entries.append(ent)
     return entries

def show(entries, popup):
     """
     For modal entries using a popup window fetchiong a set of entries
     """
     fetch(entries)                  # must fetch before window destroyed!
     popup.destroy()                 # fails with msgs if stmt order is reversed

def ask():
     """
     For modal entries using a popup window,  fields referenced are noted in makeform
     """
     popup = Toplevel()              # show form in modal dialog window
     ents = makeform(popup, fields)
     Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
     popup.grab_set()
     popup.focus_set()
     popup.wait_window()             # wait for destroy here

def makeform1(root, fields):
     """
     Two column form
     """
     form = Frame(root)                              # make outer frame
     left = Frame(form)                              # make two columns
     rite = Frame(form)
     form.pack(fill=X)
     left.pack(side=LEFT)
     rite.pack(side=RIGHT, expand=YES, fill=X)       # grow horizontal

     variables = []
     for field in fields:
          lab = Label(left, width=5, text=field)      # add to columns
          ent = Entry(rite)
          lab.pack(side=TOP)
          ent.pack(side=TOP, fill=X)                  # grow horizontal
          var = StringVar()
          ent.config(textvariable=var)                # link field to var
          var.set('enter here')
          variables.append(var)
     return variables

#==============================================================================================

class ScrolledText(Frame):
     """
     Scrollable Text Frame
     """
     def __init__(self, parent=None, text='', file=None):
          Frame.__init__(self, parent)
          self.pack(expand=YES, fill=BOTH)                 # make me expandable
          self.makewidgets()
          self.settext(text, file)

     def makewidgets(self):
          sbar = Scrollbar(self)
          text = Text(self, relief=SUNKEN)
          sbar.config(command=text.yview)                  # xlink sbar and text
          text.config(height=20)
          text.config(yscrollcommand=sbar.set)             # move one moves other
          sbar.pack(side=RIGHT, fill=Y)                    # pack first=clip last
          text.pack(side=LEFT, expand=YES, fill=BOTH)         # text clipped first
          self.text = text

     def settext(self, text='', file=None):
          if file:
               text = open(file, 'r').read()
          self.text.delete('1.0', END)                     # delete current text
          self.text.insert('1.0', text)                    # add at line 1, col 0
          self.text.mark_set(INSERT, '1.0')                # set insert cursor
          self.text.focus()                                # save user a click

     def gettext(self):                                   # returns a string
          return self.text.get('1.0', END+'-1c')          # first through last

#==============================================================================================

class ScrolledTextV(Frame):
     """
     Scrollable Text Frame with variable height
     """
     def __init__(self, rows=5, parent=None, text='', file=None):
          Frame.__init__(self, parent)
          #self.geometry('1200x350')
          self.pack(expand=YES, fill=BOTH)                 # make me expandable
          self.makewidgets(rows)
          self.settext(text, file)

     def makewidgets(self, rows=3):
          sbar = Scrollbar(self)
          text = Text(self, relief=SUNKEN)
          sbar.config(command=text.yview)                  # xlink sbar and text
          text.config(height=rows)
          text.config(yscrollcommand=sbar.set)             # move one moves other
          sbar.pack(side=RIGHT, fill=Y)                    # pack first=clip last
          text.pack(side=LEFT, expand=YES, fill=BOTH)         # text clipped first
          self.text = text

     def settext(self, text='', file=None):
          if file:
               text = open(file, 'r').read()
          self.text.delete('1.0', END)                     # delete current text
          self.text.insert('1.0', text)                    # add at line 1, col 0
          self.text.mark_set(INSERT, '1.0')                # set insert cursor
          self.text.focus()                                # save user a click

     def gettext(self):                                   # returns a string
          return self.text.get('1.0', END+'-1c')          # first through last

#==============================================================================================

class ScrolledList(Frame):
     """
     Scrollable List Frame
     """
     def __init__(self, options, parent=None):
          Frame.__init__(self, parent)
          self.pack(expand=YES, fill=BOTH)                   # make me expandable
          self.makeWidgets(options)

     def handleList(self, event):
          index = self.listbox.curselection()                # on list double-click
          label = self.listbox.get(index)                    # fetch selection text
          self.runCommand(label)                             # and call action here
                                                           # or get(ACTIVE)
     def makeWidgets(self, options):
          sbar = Scrollbar(self)
          list = Listbox(self, relief=SUNKEN)
          sbar.config(command=list.yview)                    # xlink sbar and list
          list.config(yscrollcommand=sbar.set)               # move one moves other
          sbar.pack(side=RIGHT, fill=Y)                      # pack first=clip last
          list.pack(side=LEFT, expand=YES, fill=BOTH)        # list clipped first
          pos = 0
          for label in options:                              # add to listbox
               list.insert(pos, label)                        # or insert(END,label)
               pos += 1                                       # or enumerate(options)
          #list.config(selectmode=SINGLE, setgrid=1)          # select,resize modes
          list.bind('<Double-1>', self.handleList)           # set event handler
          self.listbox = list

     def runCommand(self, selection):                       # redefine me lower
          print('You selected:', selection)

#==============================================================================================



