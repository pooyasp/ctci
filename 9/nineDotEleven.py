def parenthesize(e, result, dic):
	if (e, result) in dic:
		return dic[(e, result)]

	if e == '1':
		dic[(e, True)] = (1, ['1'])
		dic[(e, False)] = (0, [])
		return dic[(e, result)]

	if e == '0':
		dic[(e, True)] = (0, [])
		dic[(e, False)] = (1, ['0'])
		return dic[(e, result)]
	
	l = []
	for i in range(1 , len(e), 2):
		operator = e[i]
		p1 = e[:i]
		p2 = e[i+1:]
	
		if operator == '|':
			if result == True:
				c1p1 = parenthesize(p1, True, dic)
				c1p2 = parenthesize(p2, True, dic)
				l += combineResults(c1p1, c1p2, operator)

				c2p1 = parenthesize(p1, False, dic)
				c2p2 = parenthesize(p2, True, dic)
				l += combineResults(c2p1, c2p2, operator)

				c3p1 = parenthesize(p1, True, dic)
				c3p2 = parenthesize(p2, False, dic)
				l += combineResults(c3p1, c3p2, operator)


			if result == False:
				cp1 = parenthesize(p1, False, dic)
				cp2 = parenthesize(p2, False, dic)
				l += combineResults(cp1, cp2, operator)


		if operator == '&':
			if result == False:
				c1p1 = parenthesize(p1, False, dic)
				c1p2 = parenthesize(p2, False, dic)
				l += combineResults(c1p1, c1p2, operator)

				c2p1 = parenthesize(p1, False, dic)
				c2p2 = parenthesize(p2, True, dic)
				l += combineResults(c2p1, c2p2, operator)

				c3p1 = parenthesize(p1, True, dic)
				c3p2 = parenthesize(p2, False, dic)
				l += combineResults(c3p1, c3p2, operator)


			if result == True:
				cp1 = parenthesize(p1, True, dic)
				cp2 = parenthesize(p2, True, dic)
				l += combineResults(cp1, cp2, operator)


		if operator == '^':
			if result == True:
				c1p1 = parenthesize(p1, True, dic)
				c1p2 = parenthesize(p2, False, dic)
				l += combineResults(c1p1, c1p2, operator)

				c2p1 = parenthesize(p1, False, dic)
				c2p2 = parenthesize(p2, True, dic)
				l += combineResults(c2p1, c2p2, operator)


			if result == False:
				c1p1 = parenthesize(p1, True, dic)
				c1p2 = parenthesize(p2, True, dic)
				l += combineResults(c1p1, c1p2, operator)

				c2p1 = parenthesize(p1, False, dic)
				c2p2 = parenthesize(p2, False, dic)
				l += combineResults(c2p1, c2p2, operator)


	dic[(e, result)] = (len(l), l)
	return dic[(e, result)]

def combineResults(tup1, tup2, operator):
	l = []	
	if tup1[0] * tup2[0] > 0:
		for a in tup1[1]:
			for b in tup2[1]:
				if len(a) > 1:
					a = '(' + a + ')'
				if len(b) > 1:
					b =  '(' + b + ')'
				l.append( a + operator + b)
	return l

		

if __name__ == '__main__':
	d = {}
	print(parenthesize('1^0|0|1', False, d))
