#!/usr/bin/env python

import urllib2
import sys

# get data from "The Fedora Project" blog site and set to list called data
url_for_fedora_blog = "http://planet.fedoraproject.org/rss10.xml"
data = urllib2.urlopen(url_for_fedora_blog).readlines()

# make new list called bloglist, with end characters stripped off
bloglist = [a.rstrip() for a in data]

# make another new list called bloglist_title reducing data to just blog entries 
bloglist_title = []
for x in bloglist:
    if x.endswith('title>') == True:
        bloglist_title.append(str(x))

# make another new list called bloglist_tab stripping off any leading tab spaces
bloglist_tab = []
for y in bloglist_title:
    y = y.strip(' \t\n\r')
    bloglist_tab.append(str(y))
    
# stil more stripping of the strings, this time the leading html tags
bloglist_html_left = []
for z in bloglist_tab:
    z = z.lstrip("<title>")
    bloglist_html_left.append(str(z))

# another stripping function to remove trailing tags     
bloglist_html_right = []
for i in bloglist_html_left:
    i = i[:-8]
    bloglist_html_right.append(str(i))

# finally the final list splitting and reversing the strings
# printing the final strings with the color removed and BY added where split
bloglist_newline = []
for j in bloglist_html_right:
    k = j.split(": ")
    k.reverse()
    l = " BY ".join(k)
    print l
        
        
        




 



