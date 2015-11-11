def deleteNode(pointer):
	

	p1 = pointer

	while p1:
		p1.content = p1.next.content
		if p1.next.next:
			p1 = p1.next
		else:
			p1.next = None
			return

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

if  __name__ == '__main__':

	head = Node(1)
	to_be_deleted = None

	pointer = head
	for i in range(2,21):
		pointer.next = Node(i)
		if i == 10:
			to_be_deleted = pointer.next
		pointer = pointer.next

	head.printToTail()

	print('----------------------------')

	deleteNode(to_be_deleted)
	head.printToTail()