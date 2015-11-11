def toBinary(n):
	result = ['0.']

	counter = 0
	while n != 0 and counter < 32:
		counter += 1
		n = n * 2
		d = int(n)
		result.append(str(d))
		n = n - d

	if n != 0:
		return None

	return ''.join(result)

if __name__ == '__main__':
	print(toBinary(0.72))
