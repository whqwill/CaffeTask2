#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
        print 'parameters: cluster index, cluster label'
        exit(0)

fin = open(sys.argv[1])
cluster = [[i,0,0,0] for i in range(100)]
for i in range(10):
	a = map(int,fin.readline().split())
	for j in range(len(a)):
		cluster[a[j]] = [a[j],i+1,j,len(a)]
fout = open(sys.argv[2],'w')
for i in range(100):
	fout.write('%d %d %d %d\n' %(cluster[i][0],cluster[i][1],cluster[i][2],cluster[i][3]))

