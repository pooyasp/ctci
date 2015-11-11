def isPalindromeV2(l):

	length = 0
	current = l

	while current:
		length += 1
		current = current.next
	
	return isPalindromeRecursive(l, length)[1]


def isPalindromeRecursive(l, length):

	if length == 0:
		return (l, True)
	if length == 1:
		return (l.next, True)
	if length == 2:
		if l.content == l.next.content:
			return (l.next.next, True)
		else:
			return (None, False)

	result = isPalindromeRecursive(l.next, length - 2)
	
	if result[1]:
		if l.content == result[0].content:
			return (result[0].next, True)
	return (None, False)
	



def isPalindromeV1(l1):
	l2 = reverse_copy(l1)

	while l1:
		if l1.content != l2.content:
			return False

		l1 = l1.next
		l2 = l2.next

	return True


def reverse_copy(head):


	current = head
	new_head = None
	
	while current:
		n = Node(current.content, new_head)
		new_head = n
		current = current.next
			
	return new_head


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
	
	list1 = Node(1,Node(2,Node(3,Node(2,Node(1)))))
	list2 = Node(1,Node(2,Node(3,Node(2))))
	
	list1.printToTail()
	list2.printToTail()

	print('----------------------------')

	print(isPalindromeV2(list1))
	print(isPalindromeV2(list2))

	