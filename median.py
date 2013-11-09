#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################################################
#  Some implementations for stats. Not tested for performance
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


from random import Random

generator = Random()
x = [generator.randint(1,100000000) for i in range(1000000)]
k = ((len(x)//2) + (len(x)//n +1))//2 if len(x)%2  else len(x)//2

def quickselect(array, k):
	pivot = generator.choice(array)
	index = array.index(pivot)
	a1, a2, a3 = [], [], []
	# do three list comprehensions run faster than one for loop???
	for a in array:
		if a < pivot: a1.append(a)
		if a == pivot: a2.append(a)
		if a > pivot: a3.append(a)
	if k < len(a1): return quickselect(a1, k)
	if k > len(a1) + len(a2): return quickselect(a3, k - len(a1) - len(a2))
	return pivot
	
if __name__ == '__main__':
	median = quickselect(x, k)
	print median
