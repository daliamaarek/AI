from NodeAbstract import NodeAbstract
class Node(NodeAbstract):

	def state(self, stateValue):
		self.state = stateValue

	def parent(self, parentValue):
		self.parent = parentValue

	def operators(self, operatorsValue):
		self.operators = operatorsValue

	def depth(self, depthValue):
		self.depth = depthValue

	def cost(self, costValue):
		self.cost = costValue

	def expand(self):
			children = []
		#forward
			child = Node()
			child.state.direction = 0
			child.operators = "F"
			newChild(child)
			adjustLocation(child)
			children.append(child)
		#east 
			child = Node()
			child.state.direction = 1
			child.operators = "RR".append("F")
			newChild(child)
			adjustLocation(child)
			children.append(child)
		#south
			child = Node()
			child.state.direction = 2
			child.operators = "RR".append("RR").append("F")
			newChild(child)
			adjustLocation(child)
			children.append(child)
		#west
			child = Node()
			child.state.direction = 3
			child.operators = "RL".append("F")
			newChild(child)
			adjustLocation(child)
			children.append(child)
		
	def adjustLocation(self, child):
		finalDirection = (self.state.direction + child.state.direction)%3
		if finalDirection == 0:
			child.state.cell = self.state.matrix[self.state.cell.row][self.state.cell.column+1]
		elif finalDirection == 1:
			child.state.cell = self.state.matrix[self.state.cell.row+1][self.state.cell.column]
		elif finalDirection == 2:
			child.state.cell = self.state.matrix [self.state.cell.row][self.state.cell.column-1]
		elif finalDirection == 3:
			child.state.cell = self.state.matrix[self.state.cell.row-1][self.state.cell.column]
		child.state.direction = finalDirection

	def newChild(self, child):
			child.depth = self.depth + 1
			child.cost = self.cost + 1
			child.parent = self
			child.state.matrix = self.state.matrix

n = Node()
# n.expand()
