def negate(a):
	result = 0

	if a > 0:
		for i in range(0, a):
			result += -1
	else:
		for i in range(a, 0):
			result += 1

	return result


def multiply(a, b):
	
	result = 0
	
	if a > 0:
		for i in range(0, a):
			result += b

	if a < 0:
		for i in range(a, 0):
			result += b
		result = negate(result)

	return result	

def subtract(a, b):

	return a + negate(b)

def divide(a, b):
	
	s1 = 1
	if a < 0:
		s1 = -1
		a = negate(a)

	s2 = 1
	if b < 0:
		s2 = -1
		b = negate(b)

	result = 0
	while(a > b):
		result += 1
		a -= b

	if multiply(s1, s2) < 0:
		result = negate(result)
		if a > 0:
			result += -1

	return result

if __name__ == '__main__':

	a = 1
	b = 4


	print(negate(b))
	print(multiply(a, b))
	print(subtract(a, b))
	print(divide(a, b))