#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 4:
	print 'parameters: all_soft_last_again_, branch range begin, branch range end, output file(all_label_hard)'
	exit(0)

#fcoarse = open(sys.argv[1])
begin = int(sys.argv[2])
end = int(sys.argv[3])
fbranch = []
for i in range(end-begin+1):
	fbranch.append(open(sys.argv[1]+str(i+begin)))
fout = open(sys.argv[4],'w')

#calculate
for i in range(10000):
	label = [0 for k in range(100)]
	for j in range(end-begin+1):
		#print j
		a = map(float,fbranch[j].readline().split())
		for k in range(100):
			label[k] += a[k]
	fout.write('%d\n' %label.index(max(label)))
