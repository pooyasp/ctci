from sets import Set

def allPermutations(s):
	
	result = Set()
	if s == '':
		result.add('')
		return result

	c = s[-1]

	pSet = allPermutations(s[:-1])
	

	results = Set()
	for p in pSet:
		for i in range(len(p)+1):
			results.add(p[:i] + c + p[i:])

	return results



if __name__ == '__main__':
	s = 'aaaaagh'

	print(allPermutations(s))