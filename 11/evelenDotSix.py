import random

def findInMatrix(l, sx, sy, ex, ey, n):
	if sx == ex and sy == ey:
		if l[sx][sy] == n:
			return (sx, sy)
		else:
			return None

	if ex - sx == 1 and ey - sy == 1:
		if l[sx][sy] == n:
			return (sx, sy)
		if l[sx][ey] == n:
			return (sx, ey)
		if l[ex][sy] == n:
			return (ex, sy)
		if l[ex][ey] == n:
			return (ex, ey)
		return None

	if ex - sx == 0 and ey - sy == 1:
		if l[sx][sy] == n:
			return (sx, sy)
		if l[ex][ey] == n:
			return (ex, ey)
		return None

	if ex - sx == 1 and ey - sy == 0:
		if l[sx][sy] == n:
			return (sx, sy)
		if l[ex][ey] == n:
			return (ex, ey)
		return None

	
	midx = (sx + ex) / 2
	midy = (sy + ey) / 2

	if l[midx][midy] == n:
		return (midx, midy)

	result = None
	if l[midx][midy] > n:
		result = findInMatrix(l, sx, sy, midx, midy, n)
	else:
		result = findInMatrix(l, midx, midy, ex, ey, n)
	if result != None:
		return result
	
	if l[sx][midy] <= n and l[midx][ey] >= n:
		result = findInMatrix(l, sx, midy, midx, ey, n) 
	if result != None:
		return result

	if l[midx][sy] <= n and l[ex][midy] >= n:
		result = findInMatrix(l, midx, sy, ex, midy, n)
	return result

def printMatrix(l):
	for e in l:
		s = []
		for n in e:
			s.append(str(n))
		print(', '.join(s))

if __name__ == '__main__':
	m = 10
	n = 5

	l = []
	num = 10
	for i in range(m):
		temp = []
		for j in range(n):
			#temp.append(random.randint((1 + i*n)*2, (n + i*n)*2))
			temp.append(num)
			num += 1
		#temp.sort()
		l.append(temp)

	printMatrix(l)

	print(findInMatrix(l, 0, 0, len(l)-1, len(l[0])-1, 137))


