#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 4:
        print 'parameters: label file, label file(hard or soft), test.categories.label, correct label file'
        exit(0)

f = open(sys.argv[1])
ff = open(sys.argv[2])
fc = open(sys.argv[3])
fin = open(sys.argv[4])
n = 0
c = 0
while True:
     line1 = f.readline().strip()
     line2 = ff.readline().strip()
     line3 = fc.readline().strip()
     line4 = fin.readline().strip()
     if line1 in ('',None) or line4 in ('',None):
             break
     if line3 == '0':
	     if line1 == line4:
             	    c +=1
     else:
     	     if line2 == line4:
             	    c += 1
     n += 1

print c*1.0/n
