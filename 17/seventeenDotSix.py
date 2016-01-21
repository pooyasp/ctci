def findIndex(l):
	m = 0
	while l[m] < l[m+1]:
		m += 1
	
	n = len(l) - 1
	while l[n] > l[n-1]:
		n -= 1

	n = n-1
	m = m+1

	print m, n
	
	min_v = l[m]
	max_v = l[n]

	
	for i in range(m, n+1):
		min_v = min(min_v, l[i])
		max_v = max(max_v, l[i])

	flag = True
	while flag:
		flag = False
		while l[m-1] > min_v:
			m -= 1
			if l[m] > max_v:
				max_v = l[m]
				flag = True

		while l[n+1] < max_v:
			n += 1
			if l[n] < min_v:
				min_v = l[n]
				flag = True

	return m, n



if __name__ == '__main__':
	l = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
	print findIndex(l)