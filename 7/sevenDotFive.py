
def intersect(l, s):

	x1 = float(s.y1 - l.b) / l.a

	if x1 >= s.x1 and x1 <= s.x2:

		x2 = float(s.y2 - l.b) / l.a
		return(x1, s.y1, x2, s.y2)

	else:
		y1 = l.a * s.x1 + l.b
		y2 = l.a * s.x2 + l.b
		return(s.x1, y1, s.x2, y2) 




def squaresCutter(s1, s2):
	s1_mid = midPoint(s1)
	s2_mid = midPoint(s2)

	if s1_mid == s2_mid:
		return (0, s1_mid[1])

	a = float(s1_mid[1] - s2_mid[1]) / (s1_mid[0] - s2_mid[0])

	b = s1_mid[1] - a * s1_mid[0]

	return Line(a, b)


def midPoint(s):
	return((s.x1 + s.x2) / 2.0, (s.y1 + s.y2) / 2.0)


class Square(object):
	def __init__(self, x1, y1, x2, y2):
		self.x1 = float(x1)
		self.y1 = float(y1)
		self.x2 = float(x2)
		self.y2 = float(y2)

	def lines(self):
		return[]

class Line(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b


if __name__ == '__main__':
	s1 = Square(0, 1, 1, 0)
	s2 = Square(2, 4, 4, 2)
	l = squaresCutter(s1, s2)
	print(intersect(l, s2))