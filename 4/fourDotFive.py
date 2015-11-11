last_seen = float('-inf')

def isBSTV2(root, last_seen):
	if root == None:
		return True

	if not isBSTV2(root.left): return False

	if last_seen >= root.content: return False

	last_seen = root.content

	if not isBSTV2(root.right): return False

	return True


def isBSTV1(root):
	if root == None:
		return (True, None, None)

	left_result = isBSTV1(root.left)
	right_result = isBSTV1(root.right)

	
	result_min = root.content
	result_max = root.content
	result_bool = left_result[0] and right_result[0]

	if not(left_result[1] == None and left_result[2] == None):
		result_min = min(result_min, left_result[1])
		result_max = max(result_max, left_result[2])
		result_bool = result_bool and root.content >= left_result[2]

	if not(right_result[1] == None and right_result[2] == None):
		result_min = min(result_min, right_result[1])
		result_max = max(result_max, right_result[2])
		result_bool = result_bool and root.content < right_result[1]

	return (result_bool, result_min, result_max)

	

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

	n2.left = n1
	n2.right = n3
	n4.left = n2
	n4.right = n6
	n6.left = n5
	n6.right = n7
	#n1.left = n8
	#n5.right = n9
	last_seen = float('-inf')
	print(isBSTV2(n4))