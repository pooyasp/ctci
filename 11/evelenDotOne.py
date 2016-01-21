import random

def mergeArrays(a, b):
	for i in range(len(a)-1, len(b)-1, -1):
		a[i] = a[i-len(b)]

	index = 0
	index_a = len(b)
	index_b = 0

	while index_a < len(a) and index_b < len(b):
		if a[index_a] < b[index_b]:
			a[index] = a[index_a]
			index_a += 1
		else:
			a[index] = b[index_b]
			index_b += 1

		index +=1

	while index_b < len(b):
		a[index] = b[index_b]
		index_b += 1
		index += 1


if __name__ == '__main__':
	a = []
	b = []

	n = 25
	m = 10

	for i in range(n-m):
		a.append(random.randint(1, 1000))

	a.sort()
	a += [0]*m
	print a 

	for i in range(m):
		b.append(random.randint(1, 1000))

	b.sort()
	print b

	c = a[0:len(a)-len(b)] + b[:]
	c.sort()
	print c

	mergeArrays(a, b)

	print a
