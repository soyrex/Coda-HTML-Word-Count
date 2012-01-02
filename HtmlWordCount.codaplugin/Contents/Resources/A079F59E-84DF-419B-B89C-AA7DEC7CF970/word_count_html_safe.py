#!/usr/bin/env python
from os import system
from sys import stdin
from re import sub


def number_format(num, places=0):
	places = max(0,places)
	tmp = "%.*f" % (places, num)
	point = tmp.find(".")
	integer = (point == -1) and tmp or tmp[:point]
	decimal = (point != -1) and tmp[point:] or ""
	
	count = commas = 0
	formatted = []
	for i in range(len(integer) - 1, 0, -1):
	    count += 1
	    formatted.append(integer[i])
	    if count % 3 == 0:
	        formatted.append(",")
	formatted.append(integer[0]) # this misses in your part
	integer = "".join(formatted[::-1])
	return integer+decimal
	

words = number_format(len(sub('<.*?>','',' '.join(stdin.readlines())).split(None)))
system('say %s words' % (words))