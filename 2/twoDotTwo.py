def findKthToLastV1(head, k):
	current = head
	counter1 = 0
	while current:
		counter1 += 1
		current = current.next


	current = head
	counter2 = 0
	while current:
		counter2 += 1
		if counter1 - k + 1 == counter2:
			return current

		current = current.next


def findKthToLastV2(head, k):
	p1 = head
	p1_index = 1
	p2 = head
	p2_index = 1
	current = head

	counter = 0
	while current:
		counter += 1
		if counter % k == 0:
			 if p2_index != 1:
			 	p1 = p2
			 	p1_index = p2_index
			 p2 = current
			 p2_index = counter

		current = current.next

	link_list_len = counter

	if p2_index == link_list_len - k + 1:
		return p2

	current = p1
	counter = p1_index - 1
	while current:
		counter += 1
		if counter == link_list_len - k + 1:
			return current

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
	for i in range(2,21):
		pointer.next = Node(i)
		pointer = pointer.next

	head.printToTail()

	print('----------------------------')

	print(findKthToLastV1(head, 1))
	print(findKthToLastV2(head, 1))