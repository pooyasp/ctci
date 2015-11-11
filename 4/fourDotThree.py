def makeBST(int_list):

	print(int_list)
	l = len(int_list)

	if l == 0:
		return None

	if l == 1:
		return BTNode(int_list[0])

	if l % 2 == 1:
		pivot = l/2
	else:
		pivot = l/2-1

	left_list = int_list[:pivot]
	right_list = int_list[pivot+1:]

	left = makeBST(left_list)
	right = makeBST(right_list)

	result = BTNode(int_list[pivot], left, right)

	return result
	

class BTree(object):

	def __init__(self, root = None):
		self.root = root

	def __str__(self):
		return self.in_order_traversal(self.root)

	def in_order_traversal(self, n):
		
		if n == None:
			return ''

		return  str.strip(self.in_order_traversal(n.left) + 
				' ' + 
				str(n) + 
				' ' + 
				self.in_order_traversal(n.right))

class BTNode(object):

	def __init__ (self, content = None, left = None, right = None):
		self.content = content
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.content)


if __name__ == '__main__':
	
	bt = BTree(makeBST([1,2,3,4,5,6,7]))

	print(bt)