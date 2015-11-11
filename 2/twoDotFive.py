import random 

def addV1(num1, num2):
	c = 0
	head = Node('#')

	while num1 or num2:
		n1 = 0
		n2 = 0 
		
		if num1:
			n1 = num1.content
			num1 = num1.next

		if num2:
			n2 = num2.content
			num2 = num2.next

		s = n1 + n2 + c
		c = s / 10
		if head.content == '#':
			head = Node(s % 10)
		else:
			head.appnedToTail(s % 10)

	if c != 0:
		head.appnedToTail(c)

	return head


def addV2(num1, num2):
	return reverse(addV1(reverse(num1), reverse(num2)))

def reverse(num):
	head = None

	while num:
		temp = num.next
		num.next = head
		head = num
		num = temp

	return head



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
	
	num1 = Node(random.randint(1,9))
	pointer = num1
	for i in range(2, 6):
		pointer.next = Node(random.randint(0,9))
		pointer = pointer.next

	num1.printToTail()


	num2 = Node(random.randint(1,9))
	pointer = num2
	for i in range(2, 6):
		pointer.next = Node(random.randint(0,9))
		pointer = pointer.next

	num2.printToTail()

	print('----------------------------')

	addV1(num1, num2).printToTail()

	addV2(num1, num2).printToTail()