#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
	print 'parameters: confusion.maxtrix.without.index, cluster'
	exit(0)

#-----------------------------confusion maxtrix-------------------------------#

#read confusion matrix
#print 'read confusion matrix......'
f = open(sys.argv[1])
conM = []
for i in range(100):
	conM.append([x/1.0 for x in map(int,f.readline().split())])

#----------------------------clustering-------------------------------#
#L2 distance function
def L1(a,b):
	return sum(abs(a-b))

#L2 distance function
def L2(a,b):
	return sum((a-b)**2)**0.5

def avgdis(cluster):
	mean = cluster[0]
	ele = cluster[1]
	s = 0
	for i in range(len(ele)):
		s += L1(mean,conM[ele[i]])
	return s*1.0/len(ele)

#cluster
conM = array(conM)
#print 'cluster......'
cluster = []
#print conM
#print conM.size()
for i in range(100):
	cluster.append([conM[i],[i]])
finfo = open(sys.argv[2]+'.info','w')
for t in range(99):
	print t
	minDis = float(Inf)
	minIndex = (0,1)
        minDis2 = float(Inf)
        minIndex2 = (0,1)	
	for i in range(len(cluster)-1):
		for j in range(i+1,len(cluster)):
			Ni = len(cluster[i][1])
			Nj = len(cluster[j][1])
			tmp = L1(cluster[i][0],cluster[j][0])
			#tmp = L1(cluster[i][0],cluster[j][0]) 
			if tmp < minDis:
				minDis = tmp
				minIndex = (i,j)
	[i,j] = minIndex
        Ni = len(cluster[i][1])
        Nj = len(cluster[j][1])
	cluster[i][0] = (cluster[i][0]*Ni+cluster[j][0]*Nj)*1.0/(Ni+Nj)
	cluster[i][1] += cluster[j][1]
	cluster[i][1].sort()
	del cluster[j]
	fout = open(sys.argv[2]+'.'+str(len(cluster)),'w')
	#p = []
	finfo.write(str(len(cluster))+':')
	maxavg = 0
	for i in range(len(cluster)):
		if len(cluster[i][1]) == 1:
			continue
        	#fout.write('%d.(%d) ' %(i+1,len(cluster[i][1])))
        	fout.write(' '.join(map(str,cluster[i][1] ))+'\n')
		tmp = avgdis(cluster[i])
		if tmp > maxavg:
			maxavg = tmp
		finfo.write(str(len(cluster[i][1]))+'('+str(tmp)+'),')
	finfo.write('max average:'+str(maxavg))
	finfo.write('\n')
	fout.close()
finfo.close()
