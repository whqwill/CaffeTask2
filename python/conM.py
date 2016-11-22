#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 3:
	print 'parameters: all_label_new, all_label.correct, confusion maxtrix output file'
	exit(0)

#-----------------------------confusion maxtrix-------------------------------#
#read and accumulate confusion matrix
print 'read and accumulate confusion matrix......'
f = open(sys.argv[1])
fc= open(sys.argv[2])
conM = [[0 for i in range(100)] for j in range(100)]

for i in range(10000):
	l = int( f.readline().strip())
	lc= int(fc.readline().strip())
	conM[lc][l] += 1

#write confusion matrix
print 'write confusion matrix......'
fout = open(sys.argv[3],'w')
fout.write("   ")
for j in range(100):
	fout.write("%2d " %j)
fout.write("\n")
for i in range(100):
        fout.write("%2d " %i)
	for j in range(100):
		fout.write("%2d " %(conM[i][j]))
	fout.write("\n")

#write confusion matrix without index
fout = open(sys.argv[3]+'.without.index','w')
for i in range(100):
        
        for j in range(100):
                fout.write("%2d " %(conM[i][j]))
        fout.write("\n")
