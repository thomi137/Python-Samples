#!/usr/bin/python

-*- coding:utf-8 -*-

from random import Random

generator = Random()
x = [generator.randint(1,1000) for i in range(1000)]
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
