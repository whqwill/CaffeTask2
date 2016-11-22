#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 4:
	print 'parameters: file from caffe, the cluster label, clustering file, output file'
	exit(0)

fcaffe = open(sys.argv[1])
K = int(sys.argv[2])
fcluster = open(sys.argv[3])
fout = open(sys.argv[4],'w')

def str2int(s):
        i = 0
        while True:
                if s[i] >= '0' and s[i] <= '9':
                        break
                i += 1
        sum = 0
        while True:
                sum = sum * 10 + int(s[i])
                i += 1
                if i==len(s) or s[i] < '0' or s[i] > '9':
                        break
        return sum

cluster = []

while True:
	line = fcluster.readline()
	if line in ('',None):
		break
	a = line.split()
	if len(a) < 3:
		continue
	b = []
	for i in range(1,len(a)):
		b.append(str2int(a[i]))
	cluster.append(b)
		
while True:
        line = fcaffe.readline()
        if line == '+------- PROLOGUE SCRIPT -----------------------------------------------\n':
                break
while True:
        line = fcaffe.readline()
        if line == '+------- PROLOGUE SCRIPT -----------------------------------------------\n':
                break
if K == 0:
	fout_label = open(sys.argv[4]+'.correct','w')

while True:
	line = fcaffe.readline()
	if line == '+------- EPILOGUE SCRIPT -----------------------------------------------\n':
		break
	x = int(line.split()[0])
	if K > 0:
		fout.write('%d\n' %(cluster[K-1][x]))
	else: #write all labels
		fout.write('%d\n' %x)
		fout_label.write('%d\n' %int(line.split()[1]))
