def trailingZero(n):
	fives = 0

	temp = n
	while temp > 0:
		temp = temp / 5
		fives = fives + temp

	return fives

if __name__ == '__main__':
	print(trailingZero(20))