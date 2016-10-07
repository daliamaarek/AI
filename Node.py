from NodeAbstract import NodeAbstract
from State import *
from createMaze import *

class Node(NodeAbstract):

	def __init__(self):
		self.state = State()
		self.parent = None
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

	def __eq__(self, other):
		# if((self.parent is not None and other.parent is None) or (self.parent is None and other.parent is not None)):
		# 	return False
		# self.parent == other.parent and
		return ( self.cost == other.cost and self.state == other.state)

	def expand(self, operators):
		children = []
		for i in range(0,len(operators)):
			child = Node()
			if(operators[i]=="F"):
				child.state.direction = self.state.direction
				child.operators = "F"
				child.cost = self.cost + 1
				self.adjustLocation(child)		
				self.newChild(child)
			elif(operators[i]=="RL"):
				child.state.direction = (self.state.direction +3)%4 
				child.cost = self.cost 
				child.operators = "RL"
				child.state.row = self.state.row
				child.state.column = self.state.column
				self.newChild(child)
			elif(operators[i]=="RR"):
				child.state.direction = (self.state.direction + 1)%4
				child.operators = "RR"
				child.cost = self.cost 
				child.state.row = self.state.row
				child.state.column = self.state.column
				self.newChild(child)

			if child.state.direction is not None:
				children.append(child)
		return children
		
	def adjustLocation(self, child):
		rows = maze.rows
		columns = maze.columns
		matrix = maze.field

		if (child.state.direction == 0) and (self.state.row > 0) and ("UP" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row - 1
			child.state.column = self.state.column
		elif (child.state.direction == 1) and (self.state.column + 1 < columns) and ("RIGHT" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row
			child.state.column = self.state.column + 1
		elif (child.state.direction == 2) and (self.state.row + 1 < rows) and ("DOWN" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row + 1
			child.state.column = self.state.column
		elif (child.state.direction == 3) and (self.state.column > 0 )and ("LEFT" not in matrix[self.state.row][self.state.column].walls):
			child.state.row = self.state.row
			child.state.column = self.state.column - 1
		else:
			child.state.direction = None

	def newChild(self, child):
		child.depth = self.depth + 1
		child.parent = self
		child.state.pokemonCaptured = self.state.pokemonCaptured
		pokemonslist = list(self.state.pokemonCaptured)
		if((child.state.row,child.state.column) in maze.map):
			pokemonslist[maze.map[(child.state.row,child.state.column)]] = '1'
		child.state.pokemonCaptured = "".join(pokemonslist)

