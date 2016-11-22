#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 5:
	print 'parameters: file from caffe, confusion maxtrix output file, the number of cluster, clustering output file, accuracy of each class'
	exit(0)

#-----------------------------confusion maxtrix-------------------------------#
#read and accumulate confusion matrix
print 'read and accumulate confusion matrix......'
f = open(sys.argv[1])
conM = array([0 for i in range(10000)])
while True:
        line = f.readline()
        if line == '+------- PROLOGUE SCRIPT -----------------------------------------------\n':
                break
while True:
	line = f.readline()
	if line == '+------- PROLOGUE SCRIPT -----------------------------------------------\n':
		break
for i in range(500):
	line = f.readline()
	conM += array(map(int,line.split()))
conM = conM.reshape(100,100).T


#write confusion matrix
print 'write confusion matrix......'
fout = open(sys.argv[2],'w')
fout.write("   ")
for j in range(100):
	fout.write("%2d " %j)
fout.write("\n")
for i in range(100):
        fout.write("%2d " %i)
	for j in range(100):
		fout.write("%2d " %(conM[i][j]))
	fout.write("\n")

#-----------------------------k-means clustering-------------------------------#
#L2 distance function
def L1(a,b):
	return sum(abs(a-b))

#L2 distance function
def L2(a,b):
	return sum((a-b)**2)

#cluster
print 'cluster......'
K = int(sys.argv[3])
cluster = []
print conM
#print conM.size()
for i in range(100):
	cluster.append([conM[i],[i]])
for t in range(100):
	minDis = float(Inf)
	minIndex = (0,1)
	for i in range(len(cluster)-1):
		for j in range(i+1,len(cluster)):
			Ni = len(cluster[i][1])
			Nj = len(cluster[j][1])
			tmp = Ni*Nj*1.0/(Ni+Nj)*L2(cluster[i][0],cluster[j][0]) 
			#tmp = L1(cluster[i][0],cluster[j][0]) 
			if tmp < minDis:
				minDis = tmp
				minIndex = (i,j)

	minC = float(Inf)
	for i in range(len(cluster)):
		if len(cluster[i][1]) > 1 and len(cluster[i][1]) < minC:
			minC = len(cluster[i][1])
	if minC > 3 and minC < float(Inf) and t > 20:
		break
	
	[i,j] = minIndex
        Ni = len(cluster[i][1])
        Nj = len(cluster[j][1])
        #if Ni + Nj > 20:
        #        break
	cluster[i][0] = (cluster[i][0]*Ni+cluster[j][0]*Nj)*1.0/(Ni+Nj)
	cluster[i][1] += cluster[j][1]
	del cluster[j]

#write clustering results
print 'write clustring result......'
fout = open(sys.argv[4],'w')
foutlabel = open(sys.argv[4]+'.label','w')
label = [[0,0,0] for i in range(100)]
t = 0
#accuracy_class = []
for i in range(len(cluster)):
	fout.write('(%d) ' %len(cluster[i][1]))
	fout.write(', '.join(map(str,cluster[i][1] ))+'\n')
	#accuracy_class.append((cluster[i][i],i))
	if len(cluster[i][1]) > 1:
		t += 1
		for j in range(len(cluster[i][1])):
			label[cluster[i][1][j]][0] = t
			label[cluster[i][1][j]][1] = j
			label[cluster[i][1][j]][2] = len(cluster[i][1])

for i in range(100):
	foutlabel.write('%d %d %d %d\n' %(i, label[i][0], label[i][1], label[i][2]))

#ordering the accuracy of class and write them
#def my_cmp(E1,E2):
#	return -cmp(E1[1],E2[1])

#print 'order and write accuracy of each class......'
#accuracy_class.sort(my_cmp)
#foutaccuracy = open(sys.argv[5],'w')
#for i in range(100):
#	foutaccuracy.write('%d %d\n' %(accuracy_class[i][0], accuracy_class[i][1]))

#print 'done.'
