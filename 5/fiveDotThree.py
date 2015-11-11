def nextSmallest(n):
	zeros = 0
	ones = 0
	sequence_observed_flag = False
	while not sequence_observed_flag:
		if n % 2 == 1:
			ones += 1
			if zeros != 0:
				sequence_observed_flag = True
		else:
			zeros += 1

		n = n >> 1
	
	zeros -= 1
	n = n << 1

	n = n << (ones + zeros)
	mask = ~((0 - 1) << ones) << zeros
	n = n | mask

	return n

def nextLargest(n):
	zeros = 0
	ones = 0
	sequence_observed_flag = False
	while not sequence_observed_flag:
		if n % 2 == 0:
			zeros += 1
			if ones != 0:
				sequence_observed_flag = True
		else:
			ones += 1

		n = n >> 1
	
	ones -= 1
	n = (n << 1) + 1

	n = n << (ones + zeros)
	mask = ~((0 - 1) << ones)
	n = n | mask

	return n


if __name__ == '__main__':
	print(bin(nextLargest(int('100011110000', 2))))
	print(bin(nextSmallest(int('111100001111', 2))))