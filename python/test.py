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

a = ['(4)', '13,', '58,', '81,', '90']
b = []
for i in range(1,len(a)):
	b.append(str2int(a[i]))

print b
