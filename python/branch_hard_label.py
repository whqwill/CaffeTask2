#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 6:
	print 'parameters: all.soft, branch.soft., branch range begin, branch range end, categories_null, categories label, output file(all_label_soft)'
	exit(0)

fcoarse = open(sys.argv[1])
begin = int(sys.argv[3])
end = int(sys.argv[4])
fbranch = []
for i in range(end-begin+1):
	fbranch.append(open(sys.argv[2]+str(i+begin)))
fca = open(sys.argv[5])
fcala = open(sys.argv[6])
fout = open(sys.argv[7],'w')

#read category
category = []
for i in range(10):
	a = map(int,fca.readline().strip().split(', '))
	category.append(a)

#read category label 
category_la = []
for i in range(100):
	c = int(fcala.readline().split()[1])-1
	category_la.append(c)

#print category

#max_p = 0
#index = 0
#index_ca = 0

#calculate
for i in range(10000):
	#max_p = 0
	#index = 0
	#index_ca = 0
	c = map(float,fcoarse.readline().split())
	#print '!!!'
	#print i
	#print c
	#print '!'
	index_ca = category_la[c.index(max(c))]
	#index_ca = c.index(max(c))
	#j = index_ca
	for j in range(end-begin+1):
		#print j
		a = map(float,fbranch[j].readline().split())
		
	#print c.index(max(c)),index_ca,index
	##print a
		#print j
		#print a
		if j == index_ca:
		#if max(a)*c[j] > max_p:
	#max_p = max(a)*c[j]
			index = a.index(max(a))
	#index_ca = j
	fout.write('%d\n' %category[index_ca][index])
	#print index_ca
	#print index_ca,index
	#print c.index(max(c)),index_ca,index
	#if i == 10:
	#	break
