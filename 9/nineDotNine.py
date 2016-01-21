import copy

def placeQueens(board, row):

	#print('&&&&&&&&')
	#print(row)
	#printBorad(board)
	#print('########')
	
	result = []

	for column in range(len(board[row])):
		
		temp_board = []
		temp_board = copy.deepcopy(board)
		
		if temp_board[row][column] == 1:
			temp_board[row][column] = 'Q'

			#row

			for c in range(len(temp_board[row])):
				if temp_board[row][c] != 'Q':
					temp_board[row][c] = 0

			#column
			for r in range(len(temp_board)):
				if temp_board[r][column] != 'Q':
					temp_board[r][column] = 0

			#diag rd
			r = row
			c = column
			while r < len(temp_board)-1 and c < len(temp_board[row])-1:
				r += 1
				c += 1
				if temp_board[r][c] != 'Q':
					temp_board[r][c] = 0

			#diag lu
			r = row
			c = column
			while r > 0 and c > 0:
				r -= 1
				c -= 1
				if temp_board[r][c] != 'Q':
					temp_board[r][c] = 0

			#diag ru
			r = row
			c = column
			while r < len(temp_board)-1 and c > 0:
				r += 1
				c -= 1
				if temp_board[r][c] != 'Q':
					temp_board[r][c] = 0

			#diag ld
			r = row
			c = column
			while r > 0 and c < len(temp_board[row])-1:
				r -= 1
				c += 1
				if temp_board[r][c] != 'Q':
					temp_board[r][c] = 0
			#printBorad(temp_board)
			if row + 1 == len(board):
				result.append(temp_board)
			else:
				result += placeQueens(temp_board, row+1)

	return result

def printBorad(borad):
	for row in borad:
		s = []
		for e in row:
			s.append(str(e))
		print ', '.join(s)
	print('------------------------')

if __name__ == '__main__':

	board = []
	for j in range(8):
		board.append([1]*8)


	result = placeQueens(board, 0)
	print(len(result))
	for r in result:
		printBorad(r)