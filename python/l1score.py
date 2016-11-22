#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
	print 'parameters: confusion.maxtrix.without.index, l1.score'
	exit(0)

#-----------------------------confusion maxtrix-------------------------------#

#read confusion matrix
print 'read confusion matrix......'
f = open(sys.argv[1])
conM = []
for i in range(100):
	conM.append(map(int,f.readline().split()))

fout = open(sys.argv[2],'w')

for i in range(100):
	for j in range(100):
		score = 0
		for k in range(100):
			score += abs(conM[i][k]-conM[j][k])	
		fout.write('%d ' %score)
	fout.write('\n')
