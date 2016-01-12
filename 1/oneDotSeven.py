dimport sets

def putZeros(matrix):
	row_count = len(matrix)
	col_count = len(matrix[0])

	row_zero_set = sets.Set()
	col_zero_set = sets.Set()

	for i in range(row_count):
		for j in range(col_count):
			if matrix[i][j] == 0:
				row_zero_set.add(i)
				col_zero_set.add(j)

	for i in row_zero_set:
		for j in range(col_count):
			matrix[i][j] = 0

	for j in col_zero_set:
		for i in range(row_count):
			matrix[i][j] = 0	

	return matrix

def matrixPrinter(matrix):

	max_len = len(str(len(matrix)*len(matrix[0])))
	for row in matrix:
		row_list = []
		for num in row:
			num_str = str(num)
			len_diff = max_len - len(num_str)
			row_list.append('0'*len_diff + num_str)
		print(' '.join(row_list))


if __name__ == '__main__':

	m1 = [[1]]
	m2 = [[1,0],[3,4]]
	m3 = [[1,2,3],[0,5,6],[7,8,9]]
	m4 = [[1,2,3,4],[5,6,7,0],[9,10,11,12],[0,14,15,16]]
	m5 = [[1,2,3,4,5],[6,7,8,9,10],[0,12,13,14,15],[16,17,18,19,20]]


	

	matrixPrinter(m1)
	print('->')
	matrixPrinter(putZeros(m1))
	print("----------")
	
	matrixPrinter(m2)
	print('->')
	matrixPrinter(putZeros(m2))
	print("----------")

	matrixPrinter(m3)
	print('->')
	matrixPrinter(putZeros(m3))
	print("----------")

	matrixPrinter(m4)
	print('->')
	matrixPrinter(putZeros(m4))
	print("----------")

	matrixPrinter(m5)
	print('->')
	matrixPrinter(putZeros(m5))
	print("----------")