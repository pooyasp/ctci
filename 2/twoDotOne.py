import random
import sets

def removeDuplicateV1(head):
	values = sets.Set()
	values.add(head.content)
	pre = head
	current = head.next
	while current:
		if current.content not in values:
			values.add(current.content)
			pre = current
			current = current.next
		else:
			pre.next = current.next
			current = current.next

def removeDuplicateV2(head):
	pre = head
	current = head.next
	while current:
		
		isDuplicate = False
		pointer = head

		while pointer != current:
			if pointer.content == current.content:
				isDuplicate = True
				break
			else:
				pointer = pointer.next
		
		if not isDuplicate:
			pre = current
			current = current.next
		else:
			pre.next = current.next
			current = current.next	


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
		pointer.next = Node(random.randint(1,10))
		pointer = pointer.next

	head.printToTail()

	print('----------------------------')

	removeDuplicateV2(head)
	head.printToTail()