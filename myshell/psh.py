from cmd2 import Cmd
import os
import pwd
import requests

__version__ = '0.1'

# function to provide the current username
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]


class Application(Cmd):
    """
    The main Application class

    """
    def __init__(self):
        Cmd.__init__(self)

# provided hello input function
    def do_hello(self, line):
        print "Hello:", line

# sayit function prints indicated test, conveying that python does "Rock!"
    def do_sayit(self, line):
        print "Python Rocks!", line

# home task assignment to repost to the input "greet" with "Hi, <username>"        
    def do_greet(self, line):
        user = get_username()
        print "Hi,", user

# home task to provide stock quote using the requests lib        
    def do_stock(self, line):
        ticker = line
        r = requests.get('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1' % ticker)
        print r.text

        


if __name__ == '__main__':
    app = Application()
    app.cmdloop()
