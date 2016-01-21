from sets import Set

def allParenthesesV1(n):
	result = Set()
	if n == 0:
		result.add('')
		return result

	r = allParentheses(n-1)

	for p in r:
		result.add('()' + p)
		result.add('(' + p + ')')
		result.add(p + '()')

	return result

def allParenthesesV2(n):
	pass


if __name__ == '__main__':
	
	print(allParenthesesV1(4))