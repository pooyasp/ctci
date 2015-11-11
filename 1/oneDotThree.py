def isPermutation(str_in1, str_in2):
	if len(str_in1) != len(str_in2):
		return False

	return sorted(str_in1) == sorted(str_in2)	

if __name__ == '__main__':

	str_in11 = "john"
	str_in12 = "johny"
	print(isPermutation(str_in11, str_in12))

	str_in21 = "john"
	str_in22 = "nhoj"
	print(isPermutation(str_in21, str_in22))

	str_in31 = "john"
	str_in32 = "johx"
	print(isPermutation(str_in31, str_in32))