def isBalanced(root):
	if root == None:
		return (True, 0)

	left_stat = isBalanced(root.left)
	right_stat = isBalanced(root.right)

	h_result = max(left_stat[1], right_stat[1]) + 1
	b_result = left_stat[0] and right_stat[0] and abs(left_stat[1] - right_stat[1]) <= 1

	return (b_result, h_result)


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
	t = BTree(BTNode(2, BTNode(1), BTNode(3) ))
	

	print(isBalanced(t.root))