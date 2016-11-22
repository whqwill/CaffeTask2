#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
        print 'parameters: label file, correct label file'
        exit(0)

f = open(sys.argv[1])
fin = open(sys.argv[2])
n = 0
c = 0
while True:
     line1 = f.readline().strip()
     line2 = fin.readline().strip()
     if line1 in ('',None) or line2 in ('',None):
             break
     if line1 == line2:
             c += 1
     n += 1

print c*1.0/n
