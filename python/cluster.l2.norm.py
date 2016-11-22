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
	conM.append(map(int,f.readline().split()))

#----------------------------clustering-------------------------------#
#L2 distance function
def L1(a,b):
	return sum(abs(a-b))

#L2 distance function
def L2(a,b):
	return sum((a-b)**2)

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
	minDis = float(Inf)
	minIndex = (0,1)
	for i in range(len(cluster)-1):
		for j in range(i+1,len(cluster)):
			Ni = len(cluster[i][1])
			Nj = len(cluster[j][1])
			tmp = Ni*Nj*1.0/(Ni+Nj)*L2(cluster[i][0],cluster[j][0])**0.5
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
	p = []
	finfo.write(str(len(cluster))+':')
	for i in range(len(cluster)):
        	fout.write('%d.(%d) ' %(i+1,len(cluster[i][1])))
        	fout.write(', '.join(map(str,cluster[i][1] ))+'\n')
		finfo.write(str(len(cluster[i][1]))+',')
		if len(cluster[i][1]) >= 4:
			p.append(len(cluster[i][1]))
	finfo.write('\n')
	fout.close()
	print len(cluster),p
	#finfo.write(str(len(cluster))+':'+','.join(map(str,map(len,cluster)))+'\n')
	#print len(cluster),[x for x in map(len,cluster) if x >= 4]
finfo.close()
