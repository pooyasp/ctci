import copy

def tallestStack(l, bottom, dic):

	if bottom in dic:
		return dic[bottom]

	h = 0
	stack = []

	for p in l:
		if bottom > p:
			(above_h, above_stack) = tallestStack(l, p, dic)
			if above_h > h:
				h = above_h
				stack = copy.copy(above_stack)

	if bottom != None:
		h = bottom.ht + h
		stack.append(bottom)
	dic[bottom] = (h, stack)

	return dic[bottom]


class Person:
	def __init__(self, ht, wt):
		self.ht = ht
		self.wt = wt

	def __gt__(self, other):
		if other == None:
			return False
		return self.ht > other.ht and self.wt > other.wt

	def __lt__(self, other):
		if other == None:
			return True
		return self.ht < other.ht and self.wt < other.wt

	def __str__(self):
		return '(' + str(self.ht) + ', ' + str(self.wt) + ')'

def printStack(l):
	result = []
	for e in l:
		result.append(str(e))

	print(', '.join(result))

if __name__ == '__main__':
	l = [Person(65, 100), Person(70, 150), Person(56, 90), Person(75, 190), Person(60, 95),
	     Person(68, 110)]

	printStack(l)

	r = tallestStack(l, None, {})

	print(r[0])
	printStack(r[1])
