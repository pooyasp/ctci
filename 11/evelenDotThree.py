def findRotated(l, n, start, end):
	if end - start == 0:
		if a[start] == n:
			return start
		else:
			return None

	mid = (start + end) / 2
	
	if l[mid] == n:
		return mid

	if l[mid] < l[end]:
		if l[mid] < n:
			return findRotated(l, n, mid+1, end)
		else:
			return findRotated(l, n, start, mid-1) 	

	if l[start] < l[mid]:
		if n < l[mid]:
			return findRotated(l, n, start, mid-1)
		else:
			return findRotated(l, n , mid+1, end) 

if __name__ == '__main__':
	l = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
	print(findRotated(l, 5, 0, len(l)-1))