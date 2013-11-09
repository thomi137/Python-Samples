#!/usr/bin/python

#########################################################################################
#	Finding trends via the twitter API. Currently runs in an infinite loop and updates
#	a local CouchDB installation so I can relax. The Map/Reduce on this can be coded in 
# 	in python as well. How this is done can be found e.g. under:
#	   https://github.com/ptwobrussell/Mining-the-Social-Web or the newer repo:
#	   https://github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition
#
#	Also, for security reasons, I did not include the login module from the book above...
#	the source for that (except my Oauth secrets ;-)) is also contained in the repos above
#	Use the twitter python module and assign a Twitter object to t for the auth method
#	of your choice. The rest should work...
#
# 	Copyright 2013 by Thomas Prosser, thomas@prosser.ch
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#########################################################################################

# -*- coding: utf-8 -*-

import time
import couchdb
from twitter_login import login

try:
    import jsonlib2 as json
except ImportError:
    import json

t = login()

server = couchdb.Server('http://localhost:5984')
db = couchdb.Database('twitter_trends')
while True:
	print 'Sending requests...\n'
	"""
	This is getting a Yahoo! WOEID for the Zurich area.
	Unfortunately, the next location Twitter reports is Strassbourg...
	No longer in Switzerland and therefore not really relevant for local ongoings. So
	instead, I switched to the whole world... Equally interesting
	
	#trendsloc = t.trends.closest(lat=47.382253,long=8.535275)
	#woeid = trendsloc[-1]['woeid']
	"""
	trendsresponse =t.trends.place(_id=1)
	db.save(trendsresponse[0])
	"""
	Trends API allows 15 requests in a window of 15 minutes. So I just wait for two
	"""
	time.sleep(120)