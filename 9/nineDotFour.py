from sets import Set
from copy import copy

def allSubSets(s):
	if len(s) == 0:
		return [[]]

	e = s.pop()
	r = allSubSets(s)

	result = []
	for l in r:
		result.append(l)
		l_temp = copy(l)
		l_temp.append(e)
		result.append(l_temp)

	return result 

if __name__ == '__main__':
	s = Set()

	for i in range(5):
		s.add(i)

	temp = copy(s)
	result = allSubSets(temp)
	print(result, len(result))

