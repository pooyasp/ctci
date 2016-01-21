def countPresentation(n, pattern):
	if pattern[2] != None:
		return 1

	if pattern[1] != None:
		remaining = n - pattern[0] * 25 - pattern[1] * 10
		p = 0
		counter = countPresentation(n, [pattern[0], pattern[1], p])
		while(remaining >= 5):
			p +=1
			remaining -= 5
			counter += countPresentation(n, [pattern[0], pattern[1], p])
		return counter

	if pattern[0] != None:
		remaining = n - pattern[0] * 25
		p = 0
		counter = countPresentation(n, [pattern[0], p, None])
		while(remaining >= 10):
			p +=1
			remaining -= 10
			counter += countPresentation(n, [pattern[0], p, None])
		return counter

	remaining = n
	p = 0
	counter = countPresentation(n, [p, None, None])
	while(remaining >= 25):
		p +=1
		remaining -= 25
		counter += countPresentation(n, [p, None, None])
	return counter	


if __name__ == '__main__':
	print(countPresentation(25, [None, None, None]))