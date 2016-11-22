#!/usr/bin/env python

import sys
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
for i in range(1061):
	line = fin.readline()
	[x,y] = line.split()
	fout.write(line)
	if x==y:
		a+=1
print a*1.0/1061
