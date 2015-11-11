def partition(head, x):
	
	h_l = None
	l_current = h_l
	l_last = None
	h_be = None
	be_current = h_be
	be_last = None

	current = head
	
	while current:

		temp = current
		current = current.next

		if temp.content < x:
			if h_l:
				l_current.next = temp
				l_current = l_current.next
				l_current.next = None
				l_last = l_current
			else:
				l_current = temp
				l_current.next = None
				h_l = l_current
				l_last = l_current
		else:
			if h_be:
				be_current.next = temp
				be_current = be_current.next
				be_current.next = None
				be_last = be_current
			else:
				be_current = temp
				be_current.next = None
				h_be = be_current
				be_last = be_current

	l_last.next = h_be

	return h_l


import random

class Node(object):
	def __init__(self, content = None, next = None):
		self.content = content
		self.next = next

	def __str__(self):
		return str(self.content)

	def appnedToTail(self, content):
		node_to_append = self
		while node_to_append.next:
			node_to_append = node_to_append.next
		new_node = Node(content)
		node_to_append.next = new_node

	def printToTail(self):
		print_list = []
		node_to_print = self
		while node_to_print:
			print_list.append(str(node_to_print))
			print_list.append('->')
			node_to_print = node_to_print.next
		print(' '.join(print_list[:-1]))

if __name__ == '__main__':
	
	head = Node(1)
	pointer = head
	for i in range(20):
		pointer.next = Node(random.randint(1,100))
		pointer = pointer.next

	head.printToTail()

	print('----------------------------')

	head = partition(head, 50)
	head.printToTail()