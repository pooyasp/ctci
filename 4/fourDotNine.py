import copy
def findWeightedPath(root, w):

	if root == None:
		return ([], [])

	l_tree = findWeightedPath(root.left, w)
	r_tree = findWeightedPath(root.right, w)

	
	result_success = copy.deepcopy(l_tree[0] + r_tree[0])
	result_potential = []
	potential_path = copy.deepcopy(l_tree[1] + r_tree[1])


	if len(potential_path) == 0:
		if root.content < w:
			
			return (result_success, [([root], root.content)])
		if root.content == w:
			result_success.append(([root], root.content))
			return (result_success, [([root], root.content)])

		if root.content > w:
			return (result_success, [])


	for p in potential_path:

		p[0].append(root)
		new_weight = p[1] + root.content
		
		while new_weight > w:

			node = p[0].pop(0)
			new_weight -= node.content
			
		if new_weight == w:
			if (p[0], new_weight) not in result_success: 
				result_success.append((p[0], new_weight))

		if len(p[0]) > 0:
			if (p[0], new_weight) not in result_potential:
				result_potential.append((p[0], new_weight))
	
	
	return(result_success, result_potential)


	


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

	r = findWeightedPath(n4, 11)

	for p in r[0]:
		
		print_list = []
		for n in p[0]:
			print_list.append(str(n))
		print(str(p[1]) + ': '+ '<-'.join(print_list))

	