#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 6:
	print 'parameters: coarse.merge.soft, branch.soft., branch range begin, branch range end, categories_null, output file(all_label_soft)'
	exit(0)

fcoarse = open(sys.argv[1])
begin = int(sys.argv[3])
end = int(sys.argv[4])
fbranch = []
for i in range(end-begin+1):
	fbranch.append(open(sys.argv[2]+str(i+begin)))
fca = open(sys.argv[5])
fout = open(sys.argv[6],'w')

#read category
category = []
for i in range(10):
	a = map(int,fca.readline().strip().split(', '))
	category.append(a)

#print category

max_p = 0
index = 0
index_ca = 0

#calculate
for i in range(10000):
	max_p = 0
	index = 0
	index_ca = 0
	c = map(float,fcoarse.readline().split())
	#print '!!!'
	#print i
	index_ca = c.index(max(c))
	for j in range(end-begin+1):
		a = map(float,fbranch[j].readline().split())
		#print j
		#print a
		if j == index_ca:
		#if max(a)*c[j] > max_p:
			max_p = max(a)*c[j]
			index = a.index(max(a))
			index_ca = j
	fout.write('%d\n' %category[index_ca][index])
