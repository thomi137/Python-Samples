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
			
def generate(length = 8):
	characters = string.letters + string.digits + string.punctuation
	print ''.join(random.choice(characters) for x in range(length))			
			
def main(argv):
	try:
		opt, length = getopt.getopt(argv, 'l')
	except getopt.GetOptError:
		print 'create_db -l <password-length>'
		sys.exit[2]
	generate(int(length[0]))	
	
if __name__ == '__main__':
	main(sys.argv[1:])