class AnimalQueue(object):

	def __init__(self):
		self.dog_queue = Queue()
		self.cat_queue = Queue()
		self.t = 0

	def __str__(self):
		return str(self.dog_queue) + '\n-----\n' + str(self.cat_queue) + '\n######'

	def enqueue(self, name, animal_type):
		if animal_type == 'cat':
			self.cat_queue.enqueue((name, self.t))
		else:
			self.dog_queue.enqueue((name, self.t))

		self.t += 1

	def dequeueAny(self):
		if self.dog_queue.isEmpty():
			return self.cat_queue.dequeue()

		if self.cat_queue.isEmpty():
			return self.dog_queue.dequeue()

		if self.dog_queue.peek()[1] <= self.cat_queue.peek()[1]:
			return self.dog_queue.dequeue()
		else:
			return self.cat_queue.dequeue()


	def dequeueDog(self):
		return self.dog_queue.dequeue()

	def dequeueCat(self):
		return self.cat_queue.dequeue()


class Queue(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def __str__(self):
		print_list = []

		pointer = self.head
		while pointer:
			print_list.append(str(pointer))
			print_list.append('->')
			pointer = pointer.next

		return ' '.join(print_list[:-1])

	def enqueue(self, content):
		new_node = Node(content)
		if self.isEmpty(): 
			self.head = new_node
		else:
			self.tail.next = new_node
		self.tail = new_node

	def dequeue(self):
		if self.isEmpty():
			return None

		result = self.head.content
		self.head = self.head.next
		return result

	def peek(self):
		if self.isEmpty():
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

	q = Queue()
