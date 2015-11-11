class Stack(object):

	def __init__(self, stack_size):
		self.array = [None]*stack_size
		self.heads = [-3, -2, -1]

	def push(self, stack_num, content):
		self.heads[stack_num - 1] += 3
		self.array[self.heads[stack_num - 1]] = content

	def pop(self, stack_num):
		if self.heads[stack_num - 1] < 0:
			return None

		result = self.array[self.heads[stack_num - 1]]
		self.heads[stack_num - 1] -= 3

		return result

	def peek(self):
		if self.heads[stack_num - 1] < 0:
			return None

		return self.array[self.heads[stack_num - 1]]


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
		print(' '.join(print_list[:-1]))


if __name__ == '__main__':

	s = Stack(15)
	s.push(3, "3_1")
	print(s.array)
	s.push(3, "3_2")
	print(s.array)
	s.pop(3)
	print(s.pop(3))
	print(s.pop(3))
	s.push(3,"3_3")
	print(s.arrays)
