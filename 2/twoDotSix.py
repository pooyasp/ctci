def loopFinder(loop_list):
	p1 = loop_list
	p2 = loop_list

	while True:
		p1 = p1.next
		p2 = p2.next.next

		if p1 == p2:
			break

	p1 = loop_list
	while True:
		if p1 == p2:
			break

		p1 = p1.next
		p2 = p2.next

	return p1

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
	
	loop = Node(1)
	pointer = loop
	start = None
	for i in range(2, 12):
		pointer.next = Node(i)
		pointer = pointer.next

		if i == 4:
			start = pointer

	pointer.next = start
	#loop.printToTail()

	print('----------------------------')

	print(loopFinder(loop))