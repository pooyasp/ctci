def nextNode(node):
	#case 1: has right child
	if node.right:
		down = node.right
		while down.left != None:
			down = down.left
		return down

	#case 2: no right child, left child of it's parent
	if node.parent.left == node:
		return node.parent

	#case 3: no right child, right child of it's parent
	up = node.parent
	while up:
		if up.parent and up.parent.left == up:
			return up.parent
		up = up.parent

	return None


class BTNode(object):

	def __init__ (self, content = None, left = None, right = None, parent = None):
		self.content = content
		self.left = left
		self.right = right
		self.parent = parent

	def __str__(self):
		return str(self.content)


if __name__ == '__main__':

	n1 = BTNode(1)
	n2 = BTNode(2)
	n3 = BTNode(3)
	n4 = BTNode(4)
	n5 = BTNode(5)
	n6 = BTNode(6)
	n7 = BTNode(7)
	#n8 = BTNode(8)
	#n9 = BTNode(9)

	n1.parent = n2
	n2.left = n1
	n2.right = n3
	n2.parent = n4
	n3.parent = n2
	n4.left = n2
	n4.right = n6
	n5.parent = n6
	n6.left = n5
	n6.right = n7
	n6.parent = n4
	n7.parent = n6
	#n1.left = n8
	#n5.right = n9

	print(nextNode(n7))
	