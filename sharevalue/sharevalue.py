#!/usr/bin/env python


import urllib2
import sys


# a series of command line checks for sanity
# check to make sure an arg is given for the ticker symbol
if len(sys.argv) < 2:
    print "Come on dude, I need a ticker symbol to look up"
    print "For example,  $ ./sharevalue GOOG"  
    print "Try it again."
    sys.exit(1)

# set ticker symbol argv[1] to variable s for easier usage
s = sys.argv[1]

# check to make sure only one symbol is given
if len(sys.argv) > 2:
    print "Please just give me one ticker symbol to look up"
    print "For example,  $ ./sharevalue GOOG"
    print "Try it again."
    sys.exit(1)

# check to see if arg is alphanumeric
elif s.isalnum() == False:
    print "Oh come on man! this isn't that hard"
    print "For example,  $ ./sharevalue GOOG"
    print "It must be alphanumeric, try again."
    sys.exit(1)

# check to see if arg is less that 5 characters
elif len(s) > 4:
    print "Don't you know?"
    print "A ticker symbol is not more than 4 characters in length."
    print "For example,  $ ./sharevalue GOOG"
    sys.exit(1)
    
# pass the ticker symbol to the url string
ticker_name = ('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'
    % sys.argv[1])

# go get the stock quote and cast the returned data to a string and float
get_quote = urllib2.urlopen(ticker_name)
q = get_quote.read()
float(q)

# determine if it was an actual quote
if float(q) < 0.001:
    print "Whoa, either that is a real dog of stock,"
    print "or you still need to enter a vaild ticker symbol."
    print "To see the quote for Google try $ ./sharevalue goog"
    sys.exit(1)
    
# display the quote    
else:
    print q 



