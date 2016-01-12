from sets import Set

def findLine(dots):

	lines = {}

	for i in range(0, len(dots)):
		for j in  range(i+1, len(dots)):

			a = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
			b = dots[i][1] - a * dots[i][0]

			if (a, b) not in lines:
				lines[(a, b)] = Set()
			
			lines[(a, b)].add(dots[i])
			lines[(a, b)].add(dots[j])

	max_line = None
	max_count = 0

	for k in lines:
		if len(lines[k]) > max_count:
			max_count = len(lines[k])
			max_line = k


	return (max_line, max_count)

				

if __name__ == '__main__':
	dots = [(0.0, 0.0),(1.0, 1.0),(2.0, 2.0)]
	print findLine(dots)