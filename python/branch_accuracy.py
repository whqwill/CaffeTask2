#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 5:
        print 'parameters: label file, new label file, correct label file, clustering file file, the number of branch'
        exit(0)

f = open(sys.argv[1])
ff = open(sys.argv[2])
fin = open(sys.argv[3])
fcluster = open(sys.argv[4])
K = int(sys.argv[5])

#read clustering label
cluster = []
for i in range(100):
	data = fcluster.readline().split()
        cluster.append([int(data[1]),int(data[2])])

#calculate accuracy
n = [0 for i in range(K+1)]
c = [0 for i in range(K+1)]
cc = [0 for i in range(K+1)]
changel = [0 for i in range(K+1)]
changer = [0 for i in range(K+1)]
while True:
     	line1 = f.readline().strip()
     	line2 = ff.readline().strip()
     	line3 = fin.readline().strip()
     	if line1 in ('',None) or line2 in ('',None) or line3 in ('',None):
        	break
     	line1 = int(line1)
     	line2 = int(line2)
     	line3 = int(line3)
     	if cluster[line1][1] == cluster[line3][1] and cluster[line1][0] == cluster[line3][0]:
        	c[cluster[line1][0]] += 1
	     	if cluster[line2][1] != cluster[line3][1]:
			changel[cluster[line2][0]] += 1
     	if line2 == line3:
		if cluster[line1][1] != cluster[line3][1]:
			changer[cluster[line1][0]] += 1
	     	cc[cluster[line2][0]] += 1
     
     	n[cluster[line2][0]] += 1
     
#print 'branch index\t','the number of correct recognition\t','the number of correct recogition\t','','','
for i in range(1,K+1):
     	print i,  '\t',n[i],'(total)',  '\t\t',c[i],'(correct)', c[i]*1.0/n[i], '\t',' ---> ', cc[i], '(correct)', cc[i]*1.0/n[i], '\t', '(','-',changel[i],',', '+', changer[i],')'


