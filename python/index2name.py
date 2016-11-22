#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
        print 'parameters: cluster index, index.name, cluster name(output)'
        exit(0)

f = open(sys.argv[1])
findex = open(sys.argv[2])
d = []
fout = open(sys.argv[3],'w')

def index2name(x):
	return d[x]

for i in range(100):
	d.append(findex.readline().strip())


while True:
	line = f.readline().strip()
	if line in ('',None):
		break
	[a,b] = line.split(') ')
	#print b.split(', ')
	#print map(int,b.split(' '))
	#print map(index2name,map(int,b.split(', ')))
	fout.write(a+') '+', '.join(map(index2name,map(int,b.split(', '))))+'\n')

	
