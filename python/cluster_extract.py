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
while True:
	line = f.readline()
	if line == '+------- EPILOGUE SCRIPT -----------------------------------------------\n':
		break
	cluster = int(line.split()[0])
	fout.write('%d\n' %(cluster+1))


