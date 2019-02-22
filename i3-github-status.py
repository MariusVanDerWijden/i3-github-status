
#!/usr/bin/python
import json
import urllib2
import os
import time
import sys

#insert your github token here: 
#create it via https://github.com/settings/tokens
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXX"
FILE = ".ghnotes"
SLEEP = 60

while True:
    response_part = urllib2.urlopen('https://api.github.com/notifications?access_token={}&participating=true'.format(TOKEN))
    notes_part = json.load(response_part)

    response = urllib2.urlopen('https://api.github.com/notifications?access_token={}'.format(TOKEN))
    notes = json.load(response)

    response_all = urllib2.urlopen('https://api.github.com/notifications?access_token={}&all=true'.format(TOKEN))
    notes_all = json.load(response_all)

    f = open(FILE, 'w')
    f.write("GH: %d : %d : %d" % (len(notes_part), len(notes), len(notes_all)))
    print "GH: %d : %d : %d" % (len(notes_part), len(notes), len(notes_all))
    f.close()
    time.sleep(SLEEP)
