#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 5:
	print 'parameters: all_label, all_label_hard, all_label_soft, all_label.correct, test_categories_label'
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
for i in range(10000):
	o  = int( fo.readline().strip())
	ha = int(fha.readline().strip())
	so = int(fso.readline().strip())
	co = int(fco.readline().strip())
	ca = int(fca.readline().strip())
	if ca == 0:
		continue
	n[ca-1] += 1
	if so == co:
		accso[ca-1] += 1
	if ha == co:
		accha[ca-1] += 1
	if o == co:
		acco[ca-1] += 1

for i in range(10):
	print "%d\t%d\t\t%d(%.4f)\t\t%d(%.4f)\t\t%d(%.4f)" %(i+1,n[i],acco[i],acco[i]*1.0/n[i],accha[i],accha[i]*1.0/n[i],accso[i],accso[i]*1.0/n[i])

