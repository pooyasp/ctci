class SetOfStacks(object):

	def __init__(self, threshold):
		self.threshold = threshold
		self.stacks = []
		self.index = -1

	def __str__(self):
		print_list = []
		
		for stack in self.stacks:
			print_list.append(str(stack))
			print_list.append('\n')
		
		return ''.join(print_list[:-1])

	def push(self, content):
		if self.index < 0 or self.stacks[self.index].getHeight() >= self.threshold:
			self.stacks.append(Stack())
			self.index += 1
		
		self.stacks[self.index].push(content)

	def pop(self):
		if self.index < 0:
			return None

		result = self.stacks[self.index].pop()

		if self.stacks[self.index].getHeight() == 0:
			self.stacks.pop()
			self.index -= 1

	def popAt(self, index):
		if self.index < index:
			return None

		return self.stacks[index].pop()



class Stack(object):

	def __init__(self):
		self.head = None
		self.height = 0

	def __str__(self):
		return self.head.printToTail()


	def push(self, content):
		new_node = Node(content, self.head)
		self.head = new_node
		self.height += 1

	def pop(self):
		if self.head == None:
			return None

		result = self.head.content
		self.head = self.head.next
		self.height -= 1

		return result 

	def peek(self):
		if self.head == None:
			return None

		return self.head.content

	def getHeight(self):
		return self.height


class Node(object):

	def __init__(self, content = None, next = None):
		self.content = content
		self.next = next

	def __str__(self):
		return str(self.content)


	def printToTail(self):
		print_list = []
		node_to_print = self
		while node_to_print:
			print_list.append(str(node_to_print))
			print_list.append('->')
			node_to_print = node_to_print.next
		#print(' '.join(print_list[:-1]))
		return ' '.join(print_list[:-1])

if __name__ == '__main__':

	sos = SetOfStacks(5)

	for i in range(1, 26):
		sos.push(i)

	print(sos)

	print sos.popAt(-1)

	print sos

	sos.push(10000)
	sos.push(10001)

	print(sos)


