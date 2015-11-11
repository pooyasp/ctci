class MyQueue(object):

	def __init__(self):
		self.s_enqueue = Stack()
		self.s_dequeue = Stack()

	def __str__(self):
		return str(self.s_enqueue) + '\n-------\n' + str(self.s_dequeue) + '\n######'

	def enqueuee(self, content):	
		while self.s_dequeue.peek() != None:
			self.s_enqueue.push(self.s_dequeue.pop())

		self.s_enqueue.push(content)

	def dequeue(self):
		if self.s_enqueue.peek() == None and self.s_dequeue.peek() == None:
			return None

		while self.s_enqueue.peek() != None:
			self.s_dequeue.push(self.s_enqueue.pop())

		return self.s_dequeue.pop()


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

class Node(object):

	def __init__(self, content = None, next = None):
		self.content = content
		self.next = next

	def __str__(self):
		return str(self.content)

if __name__ == '__main__':

	q = MyQueue()

	q.enqueuee(1)
	#print(q)
	q.enqueuee(2)
	q.enqueuee(3)
	#print(q)
	print(q.dequeue())
	print(q.dequeue())
	#print(q)
	q.enqueuee(4)
	q.enqueuee(5)
	print(q.dequeue())
	#print(q)
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())	
	

