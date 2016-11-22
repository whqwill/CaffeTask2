#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 3:
	print 'parameters: all_label, clustering label file, fine label output file'
	exit(0)

#-----------------------------confusion maxtrix-------------------------------#
#read clustering label
fcluster = open(sys.argv[2])
cluster = []
for i in range(100):
	cluster.append(map(int,fcluster.readline().split()))

#read coarse label and write fine label
fin = open(sys.argv[1])
fout = open(sys.argv[3], 'w')

for i in range(10000):
	x = int(fin.readline().strip())
	fout.write("%d\n" %(cluster[x][1]))





