#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader

# page input


# tab and header
hd = {"loc": "Suggestions"}
hdr = dict(page="Suggestions", today="Wednesday  March 06, 2019")

#block1 dicts

# block2 dicts
evt = dict(parish="St Roch Catholic Church", lityr="C", des="First Sunday in Lent", songbook="GC", bookname="Gather Comprehensive" )

kpsalms = [
     "	GC# 085	Psalm 91: Be with Me, Lord",
     "	GC# 610	My Refuge"
]
upsalms = [
     "Acompáñame, Señor, Be with Me, O Lord (Schiavone)	FYC 232 , A Lectionary Psalter",
     "Acompáñame, Señor/Psalm 91: Be with Me, O Lord (Cortés)	¡Aclama, Tierra Entera! Bilingual Psalter",
     "Acompáñame, Señor/Psalm 91: Be with Me, O Lord (Guimont)	G3 1018, GC2 957, LPMG 33, OC 55, RS2 1397",
     "Acompáñame, Señor/Psalm 91: Be with Me, O Lord (Hurd)	FYC 231, Cantaré Eternamente/For Ever I Will Sing Bilingual Psalter",
     "Acompáñame/Psalm 91: Be with Me (Haugen)	G3 65, OC 54, LMGM2 35, RS2 75, SS 573, W4 68, WC 457, WS 367",
     "Acompáñame/Psalm 91: Be with Me (Krisman)	OC 55",
     "Be With Me Lord, When I Am In Trouble (Alstott)	BB-MI 82, GP3 810, H 107, RA 48",
     "Be With Me Lord, When I Am In Trouble (Booth)	SPS 273",
     "Be With Me Lord, When I Am In Trouble (Bridge)	JS3 68",
     "Be With Me Lord, When I Am In Trouble (Canado)	GP3 169, JS3 69, SPS 78",
     "Be With Me Lord, When I Am In Trouble (Honoré)	Psalms for the Church: Lent and Holy Week",
     "Be With Me Lord, When I Am In Trouble (Hunstiger)	SS 520",
     "Be With Me Lord, When I Am In Trouble (Inwood)	Collegeville Psalter",
     "Be With Me Lord, When I Am In Trouble (Joncas)	BB-MI 783, GP3 170, H 137, JS3 70, OFUV 205, UEC/UIC 127",
     "Be With Me Lord, When I Am In Trouble (Mayernik)	The Five Graces Psalter",
     "Be With Me Lord, When I Am In Trouble (McKinley)	SAP 110",
     "Be With Me Lord, When I Am In Trouble (Parker)	Psalms for the Soul",
     "Be With Me Lord, When I Am In Trouble (Peloquin)	S12, W4 69, W4 1029, RS2 1118",
     "Be With Me Lord, When I Am In Trouble (Smith)	Forever I Will Sing;",
     "Be With Me Lord, When I Am In Trouble (Stephan)	SPS 79",
     "Be With Me Lord, When I Am In Trouble (Sullivan)	OIF 270, WC 456, WS 367",
     "Be With Me Lord, When I Am In Trouble (Waddell)	Abbey of Gethsemani: Psalms for the Lenten Season",
     "Be with Me, O Lord/Salmo 90: Acompáñame, Señor (Cortés)	¡Aclama, Tierra Entera! Bilingual Psalter",
     "Be with Me, O Lord/Salmo 90: Acompáñame, Señor (Guimont)	G3 1018, GC2 957, LPMG 33, OC 55, RS2 1397",
     "Be with Me, O Lord/Salmo 90: Acompáñame, Señor (Hurd)	FYC 231, Cantaré Eternamente/For Ever I Will Sing Bilingual Psalter",
     "Be with Me/Psalm 90: Acompáñame (Krisman)	OC 55",
     "Be with Me/Salmo 90: Acompáñame (Haugen)	G3 65, OC 54, LMGM2 35, RS2 75, SS 573, W4 68, WC 457, WS 367",
     "Lord, Be with Me (Haas)	PCY9 46",
     "Mi Amparo, Mi Refugio, My Refuge, My Stronghold (Hurd)	GP 231"
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
usongs = [
     "All That Is Hidden	1,G	BB-MI 502, G3 746, GC 654, GC2 654, GP 585, GP3 553, JS 762, JS3 728",
     "At the Name of Jesus (Bolduc)	1,G	WS 623",
     "At the Name of Jesus (Clemens)	1,G	G3 569, RS2 673, W4 561",
     "At the Name of Jesus (KING'S WESTON)	1,G	BB-MI 725, CBW 428, GP 424, GP3 366, JS 400, JS 483, JS3 465, OFUV 512, SPS 268, W3 499",
     "At the Name of Jesus (Noel)	1,G	W4 563, WS 623",
     "At the Name of Jesus (Toolan)	1,G	JS 400, JS3 369",
     "At the Name of Jesus (Walker)	1,G	BB-MI 726, GP3 336, H 312, JS3 466, UEC/UIC 431",
     "Before the Fruit Is Ripened by the Sun	1,G	HG 147, W3 418, W4 468",
     "Beyond the Days	1,G	BB-MI 126, GP3 268, H 250, JS 384, JS3 360",
     "Digo “Sí,” Señor/I Say “Yes,” Lord	1,G	G3 676, GC 597, GC2 581, LMGM2 553, OC 565, RS 722, WS 685",
     "Do Not Be Afraid	1,G	GP 630, JS 731, RS2 829",
     "*From Ashes to the Living Font/Por el Sendero Cuaresmal	1,G	G3 474, GC2 402, OC 412, OIF 320, OIF 420, OIF 427, PMB 236, RS 561, SS 727, W4 463, WC 216, WC 561, WS 50, WS 469",
     "God Never Fails	1,G	LMGM 224, LMGM2 578",
     "God Will Take Care of You	1,G	LMGM 183, LMGM2 409",
     "Gracious God	 	BB-MI 118, GP3 265, SPS 157",
     "I Say 'Yes,' Lord, Digo 'Sí,' Señor	1,G	G3 676, GC 597, GC2 581, LMGM2 553, OC 565, RS 722, WS 685",
     "I Will Choose Christ	1,G	BB-MI 510, CP3 497, G3 802, GC2 683, GP 459, GP3 574, H 472, JS 775, JS3 736, SPS 220",
     "Into the Desert	 	SPS 159",
     "*Jesus, Tempted in the Desert	1,G	LMGM2 290, RS 548, W4 459",
     "Jesus, Thou Joy of Loving Hearts	2	CBW 654, W3 605, W4 705",
     "Journeysong	1,G	GP 581, JS 759",
     "*Led by the Spirit	1,G	BB-MI 124, GP3 272, OFUV 423, RS2 576",
     "*Lord, Who throughout These Forty Days/En Tu Cuaresma, Oh Salvador	1,G	BB-MI 136, CBW 367, G3 479, GC2 416, GP 348, GP3 277, JS 391, JS3 352, LMGM 40, LMGM2 285, OC 410, OFUV 415, RS 553, RS2 464, SS 720, W3 417, W4 461",
     "*Not on Bread Alone	1,G	PSL C-31, SS 372",
     "O Christ, Bright Sun of Justice	1,G	JS 389",
     "*O Lord, Throughout These Forty Days	1,G	CBW 367",
     "Praise the One Who Breaks the Darkness	1,G	CBW 582, G3 625, OIF 637, RS2 737, WC 740, WS 626",
     "Show Us Your Mercy	1,G	GP 473, GP3 418, JS 563, JS4 527",
     "Somebody’s Knockin’ at Your Door/Tocando a Tu Puerta Está	1,G	BB-MI 136, G3 470, GC 395, GC2 394, GP 354, GP3 278, JS 388, JS3 354, LMGM 34, LMGM2 283, OC 398, OIF 638, RS 547, RS2 573, W3 415, W4 462, WC 752, WS 462",
     "Thanks Be to God	1,G	W3 526",
     "Thanks to God Whose Word Was Spoken	1,G	W3 514",
     "*These Forty Days of Lent	1,G	OIF 432, PMB 240, WC 574",
     "*This Is the Time	1,G	RS 556, SS 723, W4 472",
     "This Season Calls Us	1,G	JS 382, JS3 348",
     "*Those Who Love Me	1,G	PSL C-29, SS 446",
     "Thy Way, O Lord	1,G	LMGM 39, LMGM2 518",
     "Turn to Me	1,G	BB-MI 661, GP 342, GP3 280, H 247, JS 377, JS3 345, OFUV 314",
     "Turn to the Living God	1,G	G3 485, GC2 408, RS2 561",
     "*When They Call in Tribulation	1,G	IH 15",
     "*When You Call to the Lord	1,G	BFW 61, SS 600",
     "You Stand Knocking	1,G	SPS 370"
]

# block3 dicts

# collect all the dicts and such
input_ = {"hd":hd, "hdr":hdr, "evt":evt, "kpsalms":kpsalms,  "upsalms":upsalms,  "ksongs":ksongs,  "usongs":usongs}

# now to go out and render

env = Environment(loader = FileSystemLoader("../templates.d/"))
template=env.get_template("page3.jhtml")


output = template.render(input_)

print(output)