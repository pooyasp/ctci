

def costumeMaxV1(n1, n2):
	return (n1 + n2 + abs(n1-n2)) / 2

def costumeMaxV2(n1, n2):
	a = getSign(n1 - n2)
	b = flip(a)
	return a * n1 + b * n2

	# n1n2s = sign(n1 - n2)
	# n1s = sign(n1)
	# n2s = sign(n2)

	

def getSign(n):
	return flip((n >> 31 & 1))

def flip(n):
	return 1 ^ n

if __name__ == '__main__':
	print(costumeMaxV2(160, 150))