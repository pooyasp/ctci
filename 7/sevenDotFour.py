def lineIntersect(line1, line2):
	if line1.slope == line2.slope and line1.y == line2.y:
		return True

	return line1.slope != line2.slope
	

class Line(object):
	def __init__(self, slope, y):
		self.slope = slope
		self.y = y

if __name__ == '__main__':
	
	l1 = Line(2, 3)
	l2 = Line(2, 3)
	print(lineIntersect(l1, l2))