from sets import Set

def isConntected(start, end):
	q = Queue()
	visited = Set()
	
	q.enqueue(start)
	while not q.isEmpty():
		n = q.dequeue()

		if not n in visited:
			if n == end: return True
			visited.add(n)
			for c in n.children:
				q.enqueue(c)

	return False 


class DirectedGraph(object):

	def __init__(self, nodes = []):
		self.nodes = nodes

	def __str__(self):
		print_list = []
		for node in self.nodes:
			children_list = []
			for child in node.children:
				children_list.append(str(child))

			print_list.append(str(node) + ' -> ' + ', '.join(children_list))

		return '\n'.join(print_list)


class Node(object):

	def __init__(self, content = None, children = []):

		self.content = content
		self.children = children

	def __str__(self):
		return str(self.content)


class Queue(object):

	def __init__(self):
		self.queue = []

	def __str__(self):
		return str(self.queue)

	def enqueue(self, content):
		self.queue.append(content)

	def dequeue(self):
		if self.isEmpty():
			return None

		return self.queue.pop(0)

	def isEmpty(self):
		return len(self.queue) == 0 

if __name__ == '__main__':
	n1 = Node('n1')
	n2 = Node('n2')
	n3 = Node('n3')
	n4 = Node('n4')
	n5 = Node('n5')
	n6 = Node('n6')
	n7 = Node('n7')

	n1.children = [n2, n4]
	n2.children = [n3, n5, n7]
	n3.children = [n4]
	n4.children = []
	n5.children = [n3, n6, n7]
	n6.children = []
	n7.children = [n1, n5]

	g = DirectedGraph([n1, n2, n3, n4, n5, n6, n7])

	print(g)

	print(isConntected(n5, n1))
	
