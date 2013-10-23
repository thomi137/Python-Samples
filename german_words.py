#!/usr/bin/python
# -* coding: utf-8 -*-

#########################################################################################
# 	
#	Fun with german words... Oh yeah and Python classes, albeit a complete overkill
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

import urllib2

'''
Top 10000 words in the german language
Nasty iso something encoding. Should be able to strip that in the future
'''
URL_DE = 'http://wortschatz.uni-leipzig.de/Papers/top10000de.txt'

class German_words:	

	def __init__(self, max_num = 10000):
		if max_num > 10000:
			print 'Truncating, maximum wordcount is 10000'
			max_num = 10000
		self.max_num = max_num
		self.page = urllib2.urlopen(URL_DE)
		self.word_list = [item.decode('latin-1').replace('\n','') 
							for item in self.page][:max_num]
						
	def is_in_list(self, word):
		return word.decode('utf-8') in self.word_list
		
#########################################################################################
# Test code follows here 	
#########################################################################################

def get_test(max_num = 10000):
	gw = German_words(max_num)
	print gw.word_list

def is_in_test(string, max_num = 10000):
	gw = German_words(max_num)
	print gw.is_in_list(string)
	
if __name__ == '__main__':
	get_test(1)
	get_test(2)
	get_test(4)
	is_in_test('über')
	is_in_test('Elefant')
	