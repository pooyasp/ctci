
from random import randint

class Stack(object):

	def __init__(self):
		self.head = None
		self.min = None

	def push(self, content):
		new_node = Node(content, self.head)
		self.head = new_node

		if self.min == None:
			self.min = self.head
		else:
			if self.min.content > self.head.content:
				self.head.next_min = self.min
				self.min = self.head

	def pop(self):
		if self.head == None:
			return None

		result = self.head.content

		if self.head == self.min:
			self.min = self.head.next_min
		
		self.head = self.head.next

		return result 

	def peek(self):
		if self.head == None:
			return None

		return self.head.content

	def getMin(self):
		if self.min != None:
			return self.min.content
		return None



class Node(object):

	def __init__(self, content = None, next = None, next_min = None):
		self.content = content
		self.next = next
		self.next_min = next_min

	def __str__(self):
		return str(self.content)


	def printToTail(self):
		print_list = []
		node_to_print = self
		while node_to_print:
			print_list.append(str(node_to_print))
			print_list.append('->')
			node_to_print = node_to_print.next
		print(' '.join(print_list[:-1]))


if __name__ == '__main__':

	s = Stack()

	for i in range(1, 16):
		s.push(randint(1,10))
		s.head.printToTail()
		print s.getMin()

	for i in range(1, 16):
		s.pop()
		#s.head.printToTail()
		print s.getMin()	

	for i in range(1, 16):
		s.push(randint(1,10))
		s.head.printToTail()
		print s.getMin()