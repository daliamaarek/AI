from Node import *

class Queue:

	def __init__ (self,nodes,searchType):
		self.nodes = nodes
		self.searchType = searchType

	def __init__(self):
		self.nodes = []
		self.searchType = "FIFO"
	

	def dequeue(self):
		self.dequeuedValue = self.nodes.pop(0)

	def enqueue(self, element):
		if(self.searchType == "FIFO"): #BFS
			self.nodes.append(element)
		if(self.searchType == "LIFO"): #DFS
			self.nodes = [element] + self.nodes
		if(self.searchType == "PrioritizedInsert"): #UCS
			self.nodes.append(element)
			self.nodes = sorted(self.nodes, key = lambda  node: (node.cost,node.operators))

	def len(self):
		return len(self.nodes)