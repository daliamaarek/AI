from NodeAbstract import NodeAbstract
class Node(NodeAbstract):
	
	def expand(self, operators):
		print ":')"

	def state(self):
		self.state = None

	def parent(self):
		self.parent = None

	def operators(self):
		self.operators = None

	def depth(self):
		self.depth = 1

	def cost(self):
		self.cost = 1

n = Node()
n.expand([])
