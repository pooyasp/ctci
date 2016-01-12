class Employee:

	def __init__(self, name):
		self.name = name
		self.isFree = True

	def __str__(self):
		return '[' + str(self.name) +  ', ' + str(self.isFree) + ']' 

class Respondent(Employee):
	def __init__(self, name):
		Employee.__init__(self, name)

class Manager(Employee):
	def __init__(self, name):
		Employee.__init__(self, name)

class Director(Employee):
	def __init__(self, name):
		Employee.__init__(self, name)


class Office:
	def __init__(self):
		self.qR = []
		self.qM = []
		self.qD = []
		self.calls = []

	def dispatchCall(self, call):
		

class Call:
	def __init__(self, number):
		self.number = number

if __name__ == '__main__':

	e = Employee('abbas')
	r = Respondent('asghar')

	print(e)
	print(r)


