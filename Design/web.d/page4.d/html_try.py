#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input


# tab and header
hd = {"loc": "Suggestions Selection"}
hdr = dict(page="Selection", today="Thursday  April 30, 2020")

#block1 dicts

# block2 dicts
evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", 
          songbook="GC", bookname="Gather Comprehensive" , theme="Mass of Creation", 
          masstime1="Saturday   4:00", masstime2="Sunday   9:00",masstime3="Sunday 11:00")

parts = dict(gloria="GC#193       Gloria", gospelacc="GC#194      Gospel Acclimation", holy="GC#198     Holy, Holy, Holy", 
     memacca="GC#199      Memorial  Acclimation A", memaccb="GC#200      Memorial  Acclimation B", memaccc="GC#201      Memorial  Acclimation C",
     amen="GC#202         Amen",  log="GC#204         Lamb of God", verses="all", cantor="name", gospelline1="line1", gospelline2="line2")

kpsalms = [
     "	GC# 085	Psalm 91: Be with Me, Lord",
     "	GC# 610	My Refuge"
]
ksongs = [
     "	GC# 382	Again We Keep This Solemn Fast",
     "	GC# 601	All That We Have",
     "	GC# 608	Be Not Afraid",
     "	GC# 821	Bread of Life, Hope of the World",
     "	GC# 824	I Myself am the Bread of Life",
     "	GC# 797	Covenant Hymn",
     "	GC# 596	Do Not Fear to Hope",
     "	GC# 385	Eternal Lord of Love",
     "	GC# 384	Forty Days and Forty Nights",
     "	GC# 391	God of Abraham",
     "	GC# 707	Guide My Feet",
     "	GC# 686	Here I Am, Lord",
     "	GC# 049	Psalm 40: Here I Am",
     "	GC# 398	Hold Us in Your Mercy",
     "	GC# 582	I Need You to Listen",
     "	GC# 393	Jesus Walked This Lonesome Valley",
     "	GC# 642	Jesus, Lead the Way",
     "	GC# 574	Lead Me, Guide Me",
     "	GC# 610	My Refuge",
     "	GC# 517	Not by Bread Alone",
     "	GC# 611	On Eagle's Wings",
     "	GC# 695	Only This I Want",
     "	GC# 689	Out of Darkness",
     "	GC# 515	Praise to You, O Christ, Our Savior",
     "	GC# 395	Somebody's Knockin' at Your Door",
     "	GC# 569	Thanks Be to You",
     "	GC# 388	The Glory of These Forty Days",
     "	GC# 613	The Lord Is My Hope",
     "	GC# 609	The Lord Is Near",
     "	GC# 619	The Lord Is Near",
     "	GC# 518	The Word Is in Your Heart",
     "	GC# 602	Though the Mountains May Fall",
     "	GC# 397	Tree of Life",
     "	GC# 665	We Will Serve the Lord",
     "	GC# 869	We Will Serve the Lord"
]

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "evt":evt, "kpsalms":kpsalms,   "ksongs":ksongs, "parts":parts}

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("page4.jhtml")


output = template.render(input_)

print(output)