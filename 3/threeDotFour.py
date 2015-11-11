def hanoi(start, end, temp):
	if start.getHeight() == 0:
		return
	solveHanoi(start.getHeight(), start, end, temp)

def solveHanoi(height, start, end, temp):

	if height == 1:
		move(start, end)
		return

	solveHanoi(height-1, start, temp, end)
	move(start, end)
	solveHanoi(height-1, temp, end, start)

def move(start, end):
	end.push(start.pop())


class Stack(object):

	def __init__(self):
		self.head = None
		self.height = 0

	def __str__(self):
		if self.head == None:
			return ''
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

	start = Stack()
	temp = Stack()
	end = Stack()

	start.push(5)
	start.push(4)
	start.push(3)
	start.push(2)
	start.push(1)

	print('s: ' + str(start))
	print('e: ' + str(end))
	print('t: ' + str(temp))
	print('#######')
	hanoi(start, end, temp)
	print('s: ' + str(start))
	print('e: ' + str(end))
	print('t: ' + str(temp))
	print('#######')
	