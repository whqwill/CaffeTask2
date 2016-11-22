#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 3:
        print 'parameters: coarse soft, categories label, output file'
        exit(0)

category = []
fc = open(sys.argv[2])
for i in range(100):
	c = int(fc.readline().split()[1])-1
	category.append(c)

#csoft = [0 for i in range(10)]
fin = open(sys.argv[1])
fout = open(sys.argv[3],'w')

for i in range(10000):
	#print i
	csoft = [0 for k in range(10)]
	#if i == 26:
	#	print a
	a = map(float,fin.readline().split())
	for j in range(len(a)):
		if category[j] >=0:
			csoft[category[j]] += a[j]
	s = sum(csoft)
	if s == 0:
		s = 1
	#if i == 26:
	#	print i,s,len(a),a
	#print csoft[0],s,csoft[0]/s
	for j in range(len(csoft)):
		fout.write('%.15f ' %(csoft[j]/s))
	fout.write('\n')

