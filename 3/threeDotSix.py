def sortStackV1(stack, temp_stack):
	
	if stack.isEmpty():
		return

	temp_stack.push(stack.pop())

	sortStackV1(stack, temp_stack)

	pivot = temp_stack.pop()

	counter = 0
	while stack.peek() > pivot:
		temp_stack.push(stack.pop())
		counter += 1

	stack.push(pivot)

	for i in range(counter):
		stack.push(temp_stack.pop())

	return

def sortStackV2(stack, temp_stack):
	if stack.isEmpty():
		print
		return

	while not stack.isEmpty():
		temp_stack.push(stack.pop())

	while not temp_stack.isEmpty():
		pivot = temp_stack.pop()

		counter = 0 
		while stack.peek() > pivot:
			temp_stack.push(stack.pop())
			counter += 1

		stack.push(pivot)

		for i in range(counter):
			stack.push(temp_stack.pop())


class Stack(object):
 
	def __init__(self):
		self.head = None

	def __str__(self):
		if self.head == None:
			return ''

		print_list = []
		pointer = self.head
		while pointer:
			print_list.append(str(pointer))
			print_list.append('->')
			pointer = pointer.next

		return ' '.join(print_list[:-1])

	def push(self, content):
		new_node = Node(content, self.head)
		self.head = new_node

	def pop(self):
		if self.head == None:
			return None

		result = self.head.content
		self.head = self.head.next
		return result

	def peek(self):
		if self.head == None:
			return None
		
		return self.head.content


	def isEmpty(self):
		return self.head == None		

class Node(object):

	def __init__(self, content = None, next = None):
		self.content = content
		self.next = next

	def __str__(self):
		return str(self.content)

if __name__ == '__main__':

	s1 = Stack()
	s2 = Stack()

	s1.push(5)
	s1.push(4)
	s1.push(1)
	s1.push(2)
	s1.push(6)
	s1.push(3)

	print(s1)

	sortStackV2(s1, s2)

	print(s1)