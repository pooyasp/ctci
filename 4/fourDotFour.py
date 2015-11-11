def linkListDFS(root):
	q = Queue()
	result = []

	q.enqueue((root, 1))

	while not q.isEmpty():
		n = q.dequeue()

		if len(result) < n[1]:
			result.append(LinkedList())
		
		result[n[1] - 1].addToTail(Node(n[0].content))

		if n[0].left != None:
			q.enqueue((n[0].left, n[1]+1))

		if n[0].right != None:
			q.enqueue((n[0].right, n[1]+1))

	return result



class BTNode(object):

	def __init__ (self, content = None, left = None, right = None):
		self.content = content
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.content)


class LinkedList(object):

	def __init__(self, root = None):
		self.root = root

	def __str__(self):
		if self.root == None:
			return ''

		print_list = []
		pointer = self.root
		while pointer:
			print_list.append(str(pointer))
			print_list.append('->')
			pointer = pointer.next

		return ' '.join(print_list[:-1])

	def addToTail(self, new_node):
		if self.root == None:
			self.root = new_node
			return

		pointer = self.root

		while pointer.next:
			pointer = pointer.next

		pointer.next = new_node


class Node(object):

	def __init__(self, content = None, next = None):
		self.content = content
		self.next = next

	def __str__(self):
		return str(self.content)


class Queue(object):

	def __init__(self):
		self.queue = []

	def __str__(self):
		return str(self.queue)

	def enqueue(self, content):
		self.queue.append(content)

	def dequeue(self):
		if self.isEmpty():
			return None

		return self.queue.pop(0)

	def isEmpty(self):
		return len(self.queue) == 0 

if __name__ == '__main__':
	n1 = BTNode("n1")
	n2 = BTNode("n2")
	n3 = BTNode("n3")
	n4 = BTNode("n4")
	n5 = BTNode("n5")
	n6 = BTNode("n6")
	n7 = BTNode("n7")
	n8 = BTNode("n8")
	n9 = BTNode("n9")

	n2.left = n1
	n2.right = n3
	n4.left = n2
	n4.right = n6
	n6.left = n5
	n6.right = n7
	n1.left = n8
	n5.right = n9


	result = linkListDFS(n4)
	for ll in result:
		print(ll)



