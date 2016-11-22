#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 6:
	print 'parameters: branch file, the cluster index begining, the cluster index end, clustering label file, all label, output file'
	exit(0)


B = int(sys.argv[2])
E = int(sys.argv[3])
fcluster = open(sys.argv[4])
fall = open(sys.argv[5])
fout = open(sys.argv[6],'w')

#num = [815, 407, 515, 5919, 412, 409, 403, 516, 604, 0]
#num = [0, 876, 604, 1551, 612, 503, 604, 1061, 2386, 790, 1013]
num = [0, 869, 592, 1514, 575, 477, 614, 1158, 2384, 800, 1017]
#read branch file
branch = []
for i in range(B,E+1):
	fin = open(sys.argv[1]+str(i))
	tmp = []
	for j in range(num[i]):
		tmp.append(int(fin.readline().strip()))
	branch.append(tmp)

#read clustering label
cluster = []
for i in range(100):
	cluster.append(int(fcluster.readline().split()[1]))

#write new label
index = [0 for i in range(B,E+1)]
while True:
	line = fall.readline()
	if line in ('',None):
		break
	x = int(line.strip())
	if x == 0:
		fout.write('%d\n' %x)
	else:
		fout.write('%d\n' %branch[x-1][index[x-1]])
		index[x-1] += 1

