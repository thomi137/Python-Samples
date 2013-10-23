#!/usr/bin/python

#########################################################################################
# 	
#	Random password generator for secure passwords.
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

import string
import random
import sys
import getopt

class PW_gen:

	def __init__(self):
		self.options = {'letters': 0x01, 'digits': 0x02, 'punct': 0x04}				
			
	def generate_password(self, optionmask, length = 8):
		characters = ''
		if optionmask & self.options['letters']: characters += string.letters
		if optionmask & self.options['digits'] : characters += string.digits
		if optionmask & self.options['punct']  : characters += string.punctuation
		self.password = ''.join(random.choice(characters) for x in range(length))			
	
	def get_password(self):
		return self.password
		
	def get_options(self):
		return self.options
	
if __name__ == '__main__':
	gen = PW_gen()
	opts = gen.get_options()
	options = opts['letters']| opts['punct']
	gen.generate_password(options, 10)
	print gen.get_password()