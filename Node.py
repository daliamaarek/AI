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
		child.state.direction = self.state.direction
		child.operators = "F"
		child.cost = self.cost + 1
		newChild(child)
		adjustLocation(child)		
		if child.state.direction is not None:
			children.append(child)
	#right 
		child = Node()
		child.state.direction = (self.state.direction + 1)%4
		child.operators = "R"
		child.cost = self.cost 
		child.state.cell = self.cell
		newChild(child)
		children.append(child)
	#left
		child = Node()
		child.state.direction = (self.state.direction +3)%4 
		child.cost = self.cost 
		child.operators = "L"
		child.state.cell = self.cell
		newChild(child)
		children.append(child)
		
	def adjustLocation(self, child):
		finalDirection = (self.state.direction + child.state.direction)%4
		rows = self.state.matrix.rows
		columns = self.state.matrix.columns
		if (finalDirection == 0) and (self.state.cell.column > 0) and ("UP" not in self.state.cell.walls):
			child.state.cell = self.state.matrix[self.state.cell.row][self.state.cell.column-1]
		elif (finalDirection == 1) and (self.state.cell.row + 1 < rows) and ("RIGHT" not in self.state.cell.walls):
			child.state.cell = self.state.matrix[self.state.cell.row+1][self.state.cell.column]
		elif (finalDirection == 2) and (self.state.cell.column + 1 < columns) and ("DOWN" not in self.state.cell.walls):
			child.state.cell = self.state.matrix [self.state.cell.row][self.state.cell.column+1]
		elif (finalDirection == 3) and (self.state.cell.row > 0 )and ("LEFT" not in self.state.cell.walls):
			child.state.cell = self.state.matrix[self.state.cell.row-1][self.state.cell.column]
		else:
			finalDirection = None
		child.state.direction = finalDirection

	def newChild(self, child):
		child.depth = self.depth + 1
		child.parent = self
		child.state.matrix = self.state.matrix

n = Node()
# n.expand()
