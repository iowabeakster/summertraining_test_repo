#!/usr/bin/env python
 
import flask
import json
import glob 
 
# Create the application.
APP = flask.Flask(__name__)

def getlist():
    """ Retrieves list of logs currently on server.
    """
    path = '/home/kirk/summertraining_test_repo/logviewer/posts/'    
    filelist = glob.glob(path + "*.json")
    data = []
    for log in filelist:
        f = open(log, 'r').read()
        x = json.loads(f)
        data.append(x)
    return data
 

data  = getlist()

     

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    List logs available on server.
    """

    return flask.render_template('index.html', data = data)
    
    

@APP.route('/log/<log>/')
def log(log):
    """ Displays the page with log.
    """
    return flask.render_template('log.html', log = log, data = data)
 
 
if __name__ == '__main__':
    APP.debug=True
    APP.run(port=8000)
