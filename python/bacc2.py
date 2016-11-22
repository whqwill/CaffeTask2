import sys

fc = open(sys.argv[3])
cluster = []
for i in range(10000):
	cluster.append(int(fc.readline().strip()))

fin = open(sys.argv[1])
while True:
	line = fin.readline()
	if line.strip() == s:
		break
while True:
	line = fin.readline()
	if line.strip() == s:
		break
fout = open(sys.argv[2],'w')
a = 0
n = 0
for i in range(10000):
	line = fin.readline()
	cluster[i] != 7:
		continue
	[x,y] = line.split()
	fout.write(line)
	if x==y:
		a+=1
	n += 1
print a*1.0/1061
print a,n
