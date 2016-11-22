#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
        print 'parameters: correct label file, test categories, real categories label'
        exit(0)

fcluster = open(sys.argv[3])
cluster = []
for i in range(100):
	cluster.append(int(fcluster.readline().split()[1]))

flabel = open(sys.argv[1])
ftest = open(sys.argv[2])

a = [0 for i in range(10)]
n = [0 for i in range(10)]
for i in range(10000):
	label = int(flabel.readline().strip())
	test = int(ftest.readline().strip())
	if cluster[label] == test:
		a[cluster[label]-1] += 1
	n[test-1] += 1


a_all = 0
n_all = 0
for i in range(10):
	a_all += a[i]
	n_all += n[i]
	print i+1, a[i],n[i],a[i]*1.0/n[i]

print "total",a_all,n_all,a_all*1.0/n_all
	
