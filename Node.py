from NodeAbstract import NodeAbstract
from State import *


class Node(NodeAbstract):

	def __init__(self):
		self.state = State()
		self.parent = None
		self.operators = ["RL","RR","F"]
		self.depth = 0
		self.cost = 0

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
		self.newChild(child)
		self.adjustLocation(child)		
		if child.state.direction is not None:
			children.append(child)
	#right 
		child = Node()
		child.state.direction = (self.state.direction + 1)%4
		child.operators = "R"
		child.cost = self.cost 
		child.state.row = self.state.row
		child.state.column = self.state.column
		self.newChild(child)
		children.append(child)
	#left
		child = Node()
		child.state.direction = (self.state.direction +3)%4 
		child.cost = self.cost 
		child.operators = "L"
		child.state.row = self.state.row
		child.state.column = self.state.column
		self.newChild(child)
		children.append(child)
		
		return children
		
	def adjustLocation(self, child):
		rows = maze.field.rows
		columns = maze.field.columns

		if (child.state.direction == 0) and (self.state.column > 0) and ("UP" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row
			child.state.column = self.state.column - 1
		elif (child.state.direction == 1) and (self.state.row + 1 < rows) and ("RIGHT" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row + 1
			child.state.column = self.state.column
		elif (child.state.direction == 2) and (self.state.column + 1 < columns) and ("DOWN" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row
			child.state.column = self.state.column + 1
		elif (child.state.direction == 3) and (self.state.row > 0 )and ("LEFT" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row - 1
			child.state.column = self.state.column
		else:
			child.state.direction = None

	def newChild(self, child):
		child.depth = self.depth + 1
		child.parent = self
		child.state.matrix = self.state.matrix

n = Node()
# n.expand()
