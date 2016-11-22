#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 5:
	print 'parameters: all_label, all_label_hard, tmp, all_label.correct, test_categories_label'
	exit(0)

fo = open(sys.argv[1])
fha = open(sys.argv[2])
fso = open(sys.argv[3])
fco = open(sys.argv[4])
fca = open(sys.argv[5])

accso = [0 for i in range(10)]
accha = [0 for i in range(10)]
acco = [0 for i in range(10)]
n = [0 for i in range(10)]
j = 0
for i in range(10000):
	o  = int( fo.readline().strip())
	ha = int(fha.readline().strip())
	#so = int(fso.readline().strip())
	co = int(fco.readline().strip())
	ca = int(fca.readline().strip())
	if ca == 4:
		so = int(fso.readline().strip())
		n[ca-1] += 1
		if so != ha:
			print j,so,i,ha
		if so == co:
			accso[ca-1] += 1
		if ha == co:
			accha[ca-1] += 1
		if o == co:
			acco[ca-1] += 1
		j+=1
i = 3
#for i in range(10):
print i+1, '\t',n[i], '\t\t', acco[i],'(',acco[i]*1.0/n[i],')\t\t',accha[i],'(',accha[i]*1.0/n[i],')\t\t',accso[i],'(',accso[i]*1.0/n[i],')'

