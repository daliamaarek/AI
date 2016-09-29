class Queue:

	def __init__ (self,nodes,queueType):
		self.nodes = nodes
		self.queueType = queueType

	def dequeue(self):
		self.dequeuedValue = nodes.pop(0)

	def enqueue(self, element):
		if(searchType == "LIFO"): #BFS
			self.nodes.append(element)
		if(searchType == "FIFO"): #DFS
			self.nodes = [element] + self.nodes
		if(searchType == "PrioritizedInsert"): #UCS
			self.nodes.append(element)
				



