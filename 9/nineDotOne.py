def countWays(n, l):
	if l[n] != 0:
		return l[n]

	if n == 1:
		l[1] = 1
		return l[1]

	if n == 2:
		l[2] = 2
		return l[2]

	if n == 3:
		l[3] = 4
		return l[3]

	l[n] = countWays(n-1, l) + countWays(n-2, l) + countWays(n-3, l)
	return l[n]


if __name__ == '__main__':

	n = 100
	l = []
	for i in range(n+1):
		l.append(0)	
	print countWays(n, l)