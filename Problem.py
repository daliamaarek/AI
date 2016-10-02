from ProblemAbstract import ProblemAbstract
from Node import *

class Problem(ProblemAbstract):

	def operators(self, operatorsValue):
		self.operators = operatorsValue

	def initialState(self, initialStateValue):
		self.initialState = initialStateValue

	def pathCost(self, pathCostValue):
		self.pathCost = pathCostValue

	def __init__(self, operators, initial_state, path_cost, steps):
		self.operators = operators
		self.initialState = initial_state
		self.pathCost = path_cost
		self.steps = steps

	def goalTest(self, node):
		if(self.pathCost >= self.steps):
			if(node.pokemonCaptured == 1):
				return True
		return False

p = Problem([],[],[],0)
n = Node()
n.pokemonCaptured = 1
b = p.goalTest(n)
print(b)
