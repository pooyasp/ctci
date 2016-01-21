def haveAWinner(board):
	#print 'case1'
	for i in range(len(board)):
		c = board[i][0]
		if c!= '':
			haveWinner = True
			for j in range(len(board[0])):
				if board[i][j] != c:
					haveWinner = False
					break
			if haveWinner == True:
				return c

	#print 'case2'
	for j in range(len(board[0])):
		c = board[0][j]
		if c!= '':
			haveWinner = True
			for i in range(len(board)):
				if board[i][j] != c:
					haveWinner = False
					break
			if haveWinner:
				return c

	#print 'case3'
	i = 0
	j = 0
	c = board[i][j]
	if c!= '':
		haveWinner = True
		while i < len(board):
			if board[i][j] != c:
				haveWinner = False
				break
			i += 1
			j += 1
		if haveWinner:
			return c


	#print 'case4'
	i = 0
	j = len(board[0])-1
	c = board[i][j]
	if c!= '':
		haveWinner = True
		while i < len(board):
			if board[i][j] != c:
				haveWinner = False
				break
			i += 1
			j -= 1
		if haveWinner:
			return c

	#print 'case5'
	return None


if __name__ == '__main__':
	board = [['x','','o'],
			 ['x','o',''],
			 ['x','','x']
			]

	print haveAWinner(board)