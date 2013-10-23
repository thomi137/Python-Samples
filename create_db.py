#!/usr/bin/python

#########################################################################################
# Sample program to read csv data generated from MS Excel and put it into a single table
# SQLite DB. Negative Number formatting is stripped and appended with a minus ('-') sign
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

import sys
import getopt
import csv
import sqlite3
import re

insert = 'INSERT INTO COLOR_TABLE VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

def create_db(header, dbname='RGBColors.db'):
	conn = sqlite3.connect(dbname)
	c = conn.cursor();
	query = '''CREATE TABLE IF NOT EXISTS COLOR_TABLE (%s INTEGER PRIMARY KEY not null, 
	%s TEXT,%s INTEGER,%s INTEGER,%s INTEGER,%s INTEGER, %s INTEGER,%s INTEGER,%s INTEGER,
	%s INTEGER,%s INTEGER, %s INTEGER,%s INTEGER,%s INTEGER,%s INTEGER,%s INTEGER,
	%s INTEGER,%s INTEGER,%s INTEGER,%s INTEGER,%s INTEGER,%s INTEGER)''' % tuple(header)
	c.execute(query)
	conn.commit()
	return conn
	
def read_csv(filepath):
	with open(filepath, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		header = reader.next()
		conn = create_db(header)
		cur = conn.cursor()
		records = [[re.sub(r'\((\d+)\)', r'-\1', item) for item in row] for row in reader]
		cur.executemany(insert, records)
		conn.commit()
		conn.close()
			
def main(argv):
	try:
		opt, arg = getopt.getopt(argv, 'f')
	except getopt.GetOptError:
		print 'create_db -f <inputfile>'
		sys.exit[2]
	read_csv(arg[0])	
	
if __name__ == '__main__':
	main(sys.argv[1:])