def rotate(matrix):
	size = len(matrix)
	
	for i in range(size/2):
		skip = i

		for j in range(skip, size-1-skip):
			swap = matrix[i][j]
			
			#print('(' + str(i) + ', ' + str(j) + ')')

			for k in range(4):
				temp = matrix[j][size-1-i]
				matrix[j][size-1-i] = swap
				temp_i = j
				temp_j = size-1-i
				i = temp_i
				j = temp_j
				swap = temp

	return matrix

def matrixPrinter(matrix):

	max_len = len(str(len(matrix)*len(matrix)))
	for row in matrix:
		row_list = []
		for num in row:
			num_str = str(num)
			len_diff = max_len - len(num_str)
			row_list.append('0'*len_diff + num_str)
		print(' '.join(row_list))

if __name__ == '__main__':
	m1 = [[1]]
	m2 = [[1,2],[3,4]]
	m3 = [[1,2,3],[4,5,6],[7,8,9]]
	m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	m5 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


	

	matrixPrinter(m1)
	print('->')
	matrixPrinter(rotate(m1))
	print("----------")
	
	matrixPrinter(m2)
	print('->')
	matrixPrinter(rotate(m2))
	print("----------")

	matrixPrinter(m3)
	print('->')
	matrixPrinter(rotate(m3))
	print("----------")

	matrixPrinter(m4)
	print('->')
	matrixPrinter(rotate(m4))
	print("----------")

	matrixPrinter(m5)
	print('->')
	matrixPrinter(rotate(m5))
	print("----------")