from ProblemAbstract import ProblemAbstract
from Node import *

#Dalia el katabt da *Abdelreheem w Diaa msh ms2oleen*

class Problem(ProblemAbstract):

	def operators(self, operatorsValue):
		self.operators = operatorsValue

	def initialState(self, initialStateValue):
		self.initialState = initialStateValue

	def pathCost(self, pathCostValue):
		self.pathCost = pathCostValue

	def __init__(self, operators, initial_state, final_state, path_cost, steps):
		self.operators = operators
		self.initialState = initial_state
		self.pathCost = path_cost
		self.steps = steps
		self.final_state = final_state

	def goalTest(self, node):
		if(node.cost >= self.steps and node.row == self.final_state.row and node.column == self.final_state.column):
			if("0" not in node.pokemonCaptured):
				return True
		return False