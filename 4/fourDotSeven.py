def findAncestor(root, n1, n2):
	if root == None:
		return (None, False, False)

	l_tree = findAncestor(root.left, n1, n2)
	r_tree = findAncestor(root.right, n1, n2)

	if l_tree[0]:
		return l_tree

	if r_tree[0]:
		return r_tree

	seen = (l_tree[1] or r_tree[1] or root == n1, l_tree[2] or r_tree[2] or root == n2)

	if seen[0] and seen[1]:
		return (root, True, True)

	return (None, seen[0], seen[1])


class BTNode(object):

	def __init__ (self, content = None, left = None, right = None):
		self.content = content
		self.left = left
		self.right = right

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
	n8 = BTNode(8)
	n9 = BTNode(9)
	n10 = BTNode(10)
	n11 = BTNode(11)
	n12 = BTNode(12)
	n13 = BTNode(13)
	n14 = BTNode(14)
	n15 = BTNode(15)
	n16 = BTNode(16)
	n17 = BTNode(17)

	n1.left = n8
	n2.left = n1
	n2.right = n3
	n3.left = n10
	n4.left = n2
	n4.right = n6
	n5.right = n9
	n6.left = n5
	n6.right = n7
	n7.right = n12
	n9.left = n11
	n10.left = n16
	n10.right = n15
	n12.left = n13
	n12.right = n14

	print(findAncestor(n4, n14, n17)[0])