#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
	print 'parameters: file from caffe, output file, the number of objects'
	exit(0)

fin = open(sys.argv[1])
s = '+------- PROLOGUE SCRIPT -----------------------------------------------'
while True:
	line = fin.readline()
	if line.strip() == s:
		break
while True:
	line = fin.readline()
	if line.strip() == s:
		break
fout = open(sys.argv[2],'w')
a = 0
for i in range(int(sys.argv[3])):
	line = fin.readline()
	[x,y] = line.split()
	fout.write(line)
	if x==y:
		a+=1
print a*1.0/int(sys.argv[3])
