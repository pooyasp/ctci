import copy

def tallestStack(boxes, bottom, dic):
	if bottom in dic:
		return dic[bottom]

	max_height = 0 
	max_stack = []
	for b in boxes:
		if bottom > b:
			(above_height, above_stack) = tallestStack(boxes, b, dic)
			if above_height > max_height:
				max_height = above_height
				max_stack = copy.copy(above_stack)

	if bottom != None:
		max_stack = [bottom] + max_stack
		max_height = max_height + bottom.h
	dic[bottom] = (max_height, max_stack)

	return dic[bottom]


class Box:
	def __init__(self, h, w, d):
		self.h = h
		self.w = w
		self.d = d

	def __gt__(self, box):
		if box == None:
			return False
		return self.h > box.h and self.w > box.w and self.d > box.d

	def __lt__(self, box):
		if box == None:
			return True
		return self.h < box.h and self.w < box.w and self.d < box.d	
	
	def __str__(self):
		return str(self.h) + '-' + str(self.w) + '-' + str(self.d)


if __name__ == '__main__':
	b1 = Box(10, 20, 30)
	b2 = Box(1, 2, 3)
	d = {}
	print(tallestStack([b2, b1], None, d)[1][0])
