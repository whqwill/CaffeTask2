#!/usr/bin/env python

from numpy import *
import sys
import random

if len(sys.argv) < 3:
        print 'parameters: the number of total numbers, the number of clusters, output file'
        exit(0)

N = int(sys.argv[1])
K = int(sys.argv[2])
fout = open(sys.argv[3],'w')

a = [i for i in range(N)] 
b = [[] for i in range(K)]
c = [0 for i in range(K)]

random.seed(23)

#print 'N','K',N,K
for i in range(N):
	n = random.randint(0,len(a)-1)
	#print 'n',n
	k = random.randint(0,K-1)
	while c[k] >= 10:
		k = random.randint(0,K-1)
	c[k] += 1
	#print 'k',k
	#print a[n]
	#print b[k]
	b[k].append(a[n])
	del a[n]

for i in range(K):
	b[i].sort()
	fout.write(" ".join(map(str,b[i]))+'\n')

