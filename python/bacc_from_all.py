#!/usr/bin/env python

import sys

s = '+------- PROLOGUE SCRIPT -----------------------------------------------'
fc = open(sys.argv[3])
cluster = []

print "reading cluster"
for i in range(10000):
	#print i,int(fc.readline().strip())
	cluster.append(int(fc.readline().strip()))


ff = open("tmp",'w')
for i in range(len(cluster)):
	ff.write("%d\n" %(cluster[i]))

ff.close()
print "cluster done"

fin = open(sys.argv[1])
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
n = 0

print "begin to read"
for i in range(10000):
	line = fin.readline()
	if cluster[i] != 7:
		continue
	[x,y] = line.split()
	fout.write(line)
	if x==y:
		a+=1
	n += 1
print a*1.0/1061
print a,n
