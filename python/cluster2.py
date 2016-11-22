#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 5:
	print 'parameters: score, l1.cluster.all.information, l2.cluster, all_label_new, all_label.correct'
	exit(0)

f = open(sys.argv[1])
score = []
for i in range(100):
	score.append(map(int,f.readline().split()))

score_order = []
for i in range(100):
	for j in range(i+1,100):
		score_order.append([i,j,score[i][j]])

score_order.sort(key=lambda x:x[2])

finfo = open(sys.argv[2],'w')
cluster = [[i] for i in range(100)]
finfo.write('100:'+','.join(map(str,map(len,cluster)))+'\n')

fla = open(sys.argv[4])
flaco = open(sys.argv[5])
j = 0
nn = 0
for x in range(10000):
        la = int(fla.readline().strip())
        laco = int(flaco.readline().strip())
        nla = 0
        nlaco = 0
        for y in range(len(cluster)):
                if la in cluster[y]:
                        nla = y
                if laco in cluster[y]:
                        nlaco = y
        if nla == nlaco:
                nn += 1
print len(cluster),[x for x in map(len,cluster) if x >= 4],nn*1.0/10000
for i in range(99):
	while True:
		for a in range(len(cluster)):
			if score_order[j][0] in cluster[a]:
				break
        	for b in range(len(cluster)):
               		if score_order[j][1] in cluster[b]:
                       		break
		j += 1
		if a != b:
			break
	cluster[a] += cluster[b]
	cluster[a].sort()
	del cluster[b]
	fout = open(sys.argv[3]+'.'+str(len(cluster)),'w')
	for k in range(len(cluster)):
		fout.write('%d.(%d): ' %(k,len(cluster[k])))
		for l in range(len(cluster[k])):
			fout.write('%d ' %cluster[k][l])
		fout.write('\n')
	fout.close()
	finfo.write(str(len(cluster))+':'+','.join(map(str,map(len,cluster)))+'\n')
	fla = open(sys.argv[4])
	flaco = open(sys.argv[5])
	nn = 0
	for x in range(10000):
		la = int(fla.readline().strip())
		laco = int(flaco.readline().strip())
		nla = 0
		nlaco = 0
		for y in range(len(cluster)):
			if la in cluster[y]:
				nla = y
			if laco in cluster[y]:
				nlaco = y
		if nla == nlaco:
			nn += 1	
	print len(cluster),[x for x in map(len,cluster) if x >= 4],nn*1.0/10000

finfo.close()
	
