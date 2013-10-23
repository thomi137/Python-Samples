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

class PW_string:
	
	options = {'letters'	: [0x01, string.letters], 
						'digits'	: [0x02, string.digits], 
						'punct'		: [0x04, string.punctuation]}				
	
	@classmethod		
	def get_allowed_chars(self, optionmask = 0x01):
		characters = ''
		for item in self.options.values():
			if optionmask & item[0]: characters += item[1]
		return characters
		
	@classmethod	
	def get_allowed_options(self):
		return {key: self.options[key][0] for key in self.options.keys()}

class PW_gen:

	def __init__(self, allowed_chars):
		self.allowed_chars = allowed_chars
	
	def generate_password(self, length = 8):
		self.password = ''.join(random.choice(self.allowed_chars) for x in range(length))			
	
	def get_password(self):
		return self.password	
	
if __name__ == '__main__':
	opts = PW_string.get_allowed_options()
	options = opts['letters']| opts['punct']|opts['digits']
	charset = PW_string.get_allowed_chars(options)
	gen = PW_gen(charset)
	gen.generate_password()
	print gen.get_password()