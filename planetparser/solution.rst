planetparser
============

Despite considerable time, this project did not have good results.

My Issues
---------

- installing a functional tarball of my script
- all other assignment tasks resulting from the inability to make that work

I don't know where I went wrong.  I followed the instructions from the assigned reading material.  Things appeared to work, but the actual planetparser.py file never seemed to be present when the tarball was untarred and *python setup.py install* was ran (and no errors were returned in any part of the process of creation or installation).   

My hack
-------

In order to avoid turning in nothing, I did create a script that does return the title and author of the the current postings on the Fedora blog (in python of course) without any additional modules needing to be installed.  It all worked testing via ssh to another computer of mine.  But, I am sure my solution will probably be considered cheating (errr somthing).

Instructions
------------

- $ sudo apt-get install python-virtualenv (or use the package manager for your system)
- $ mkdir virtualenviro
- $ cd virtualenviro
- $ mkdir virt3
- $ cd virt3
- $ virtualenv virt3
- $ source virt3/bin/activate
- $ wget https://raw.github.com/iowabeakster/summertraining_test_repo/master/planetparser/planetparser.py
- $ chmod +x planetparser.py
- $ ./planetparser.py

Link
----

`Here <https://raw.github.com/iowabeakster/summertraining_test_repo/master/planetparser/planetparser.py>`_ 

Code
----

.. code:: python
 
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
 # printing the final strings with the colon removed and BY added where split
 bloglist_newline = []
 for j in bloglist_html_right:
     k = j.split(": ")
     k.reverse()
     l = " BY ".join(k)
     print l







