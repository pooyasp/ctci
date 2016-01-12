import copy

def countWays(x, y, d):
	if (x, y) in d:
		return d[(x, y)]

	if x == 0 and y == 0:
		d[(0, 0)] = 1
		return d[(0, 0)]
	
	if x < 0 or y < 0:
		return 0

	d[(x, y)] = countWays(x-1, y, d) + countWays(x, y-1, d)
	return d[(x, y)]

def findWay(x, y, board, d):
	if (x, y) in d:
		return d[(x, y)]

	if x == 0 and y == 0:
		d[(0, 0)] = (True, [(0, 0)])
		return d[(0, 0)]

	if x < 0 or y < 0:
		return (False, [])

	if board[x][y] == -1:
		d[(x, y)] = (False, [])
		return d[(x, y)]

	p1 = findWay(x-1, y, board, d)
	if p1[0]:
		p = copy.copy(p1[1])
		p.append((x, y))
		d[(x, y)] = (True, p)
		return d[(x, y)]

	p2 = findWay(x, y-1, board, d)
	if p2[0]:
		p = copy.copy(p2[1])
		p.append((x, y))
		d[(x, y)] = (True, p)
		return d[(x, y)]

	d[(x, y)] = (False, [])
	return d[(x, y)]



if __name__ == '__main__':
	print(countWays(2, 100, {}))

	board = [[1, 1, -1, -1, -1], 
			 [-1, 1, 1, -1, -1], 
			 [-1, -1, 1, -1, -1], 
			 [-1, -1, 1, 1, -1], 
			 [-1, -1, -1, 1, 1]]

	print(findWay(4, 4, board, {}))