#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 5:
	print 'parameters: all_label_soft or all_label_paper, all_label.correct, test_categories_label'
	exit(0)

fso = open(sys.argv[1])
fco = open(sys.argv[2])
fca = open(sys.argv[3])

acc = [0 for i in range(10)]
n = [0 for i in range(10)]
for i in range(10000):
	so = int(fso.readline().strip())
	co = int(fco.readline().strip())
	ca = int(fca.readline().strip())
	n[ca-1] += 1
	if so == co:
		acc[ca-1] += 1

for i in range(10):
	print i+1,acc[i]*1.0/n[i],' (',acc[i],n[i],')'

