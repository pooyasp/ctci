def isSubTree(t1, t2):

	if t1 == None:
		return False

	if isSubTree(t1.left, t2) or isSubTree(t1.right, t2):
		return True

	if t1.content == t2.content:
		return treeMatch(t1, t2)

	return False


def treeMatch(t1, t2):

	if t1 == None and t2 == None:
		return True

	if (t1 == None and t2 != None) or (t1 != None and t2 == None):
		return False

	

	return t1.content == t2.content and treeMatch(t1.left, t2.left) and treeMatch(t1.right, t2.right)

class BTNode(object):

	def __init__(self, content = None, left = None, right = None):
		self.content = content
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.content)

if __name__ == '__main__':
	pass


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

	print(isSubTree(n4, n4))