#!/usr/bin/env python

from numpy import *
import sys

if len(sys.argv) < 2:
        print 'parameters: file from caffe log, output file'
        exit(0)

f = open(sys.argv[1])
while True:
	line = f.readline()
	if line == '+------- PROLOGUE SCRIPT -----------------------------------------------\n':
		break
while True:
	line = f.readline()
	if line == '+------- PROLOGUE SCRIPT -----------------------------------------------\n':
		break

fout = open(sys.argv[2],'w')
j = 0
while True:
	j += 1
	print j
	line = f.readline()
	if line == '+------- EPILOGUE SCRIPT -----------------------------------------------\n':
		break
	a = map(float,line.split())
	a = map(exp,a)
	a = a/sum(a)
	#print a
	for i in range(len(a)):
		fout.write('%.15f ' %a[i])
	fout.write('\n')
