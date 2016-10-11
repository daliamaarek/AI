from Node import *

class Queue:

	def __init__ (self,nodes,searchType):
		self.nodes = nodes
		self.searchType = searchType
		self.standardTypes = ["FIFO", "LIFO", "PrioritizedInsert"]

	def __init__(self):
		self.nodes = []
		self.searchType = "FIFO"
		self.standardTypes = ["FIFO", "LIFO", "PrioritizedInsert"]
	
	def dequeue(self):
		self.dequeuedValue = self.nodes.pop(0)

	def enqueue(self, element):
		if(callable(self.searchType)):
			self.nodes.append(element)
			self.nodes = sorted(self.nodes, key = lambda  node: self.searchType)
		elif(self.searchType == "FIFO"): #BFS
			self.nodes.append(element)
		elif(self.searchType == "LIFO"): #DFS
			self.nodes = [element] + self.nodes
		elif(self.searchType == "PrioritizedInsert"): #UCS
			self.nodes.append(element)
			self.nodes = sorted(self.nodes, key = lambda  node: (node.cost,node.operators))

	def len(self):
		return len(self.nodes)

