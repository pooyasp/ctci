class Node:

	def __init__(self, content = None, 
				 left = None, right = None,
				 parent = None,
				 self_counter = 1, 
				 left_counter = 0):
		self.content = content
		self.left = left
		self.right = right
		self.parent = parent
		self.self_counter = self_counter
		self.left_counter = left_counter
		

class BST:

	def __init__(self, root = None):
		self.root = root

	def track(self, x):
		if self.root == None:
			r = Node(x)
			self.root = r
			return

		p = None
		n = self.root

		while n != None:
			if n.content == x:
				n.self_counter += 1
				break

			p = n
			if n.content > x:
				n.left_counter += 1
				n = n.left
			else:
				n = n.right

		if n == None:
			n = Node(x, parent = p)
			if x < p.content:
				p.left = n
			else:
				p.right = n

	def getRankOfNumber(self, x):
		n = self.root

		while n != None:
			if x == n.content:
				r = n.self_counter - 1 + n.left_counter
				
				while n.parent != None:
					if n.parent.right == n:
						r += n.parent.left_counter + n.parent.self_counter
					n = n.parent

				return r

			if n.content > x:
				n = n.left
			else:
				n = n.right
		return 0



if __name__ == '__main__':
	b = BST()

	l = [5, 1, 4, 4, 5, 9, 7, 13, 3]
	
	for e in l:
		b.track(e)

	print b.getRankOfNumber(1)
	print b.getRankOfNumber(3)
	print b.getRankOfNumber(5)