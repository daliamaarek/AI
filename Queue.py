from Node import *

class Queue:

	def __init__(self):
		self.nodes = []
		self.searchType = "FIFO"
	def __init__ (self,nodes,searchType):
		self.nodes = nodes
		self.searchType = searchType

	def dequeue(self):
		self.dequeuedValue = self.nodes.pop(0)

	def enqueue(self, element):
		if(self.searchType == "FIFO"): #BFS
			self.nodes.append(element)
		if(self.searchType == "LIFO"): #DFS
			self.nodes = [element] + self.nodes
		if(self.searchType == "PrioritizedInsert"): #UCS
			self.nodes.append(element)
			self.nodes = sorted(self.nodes, key = lambda  node: node.cost)



	



# x = Node()
# y = Node()
# z = Node()
# n = Node()
# nodess = []
# x.cost(3)
# y.cost(2)
# z.cost(5)
# n.cost(1)

# m = Queue(nodess,"PrioritizedInsert")


# m.enqueue(x)
# m.enqueue(y)
# m.enqueue(z)
# m.enqueue(n)

# for i in range(0,4):
# 	 print m.nodes[i].cost





