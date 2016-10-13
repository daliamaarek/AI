from ProblemAbstract import ProblemAbstract


#Dalia el katabt da *Abdelreheem w Diaa msh ms2oleen*

class Problem(ProblemAbstract):

	def operators(self, operatorsValue):
		self.operators = operatorsValue

	def initialState(self, initialStateValue):
		self.initial_state = initialStateValue

	def pathCost(self, pathCostValue):
		self.path_cost = pathCostValue

	def __init__(self, operators, initial_state, final_state, path_cost, steps):
		self.operators = operators
		self.initial_state = initial_state
		self.path_cost = path_cost
		self.steps = steps
		self.final_state = final_state

	def goalTest(self, node):
		if(node.state.steps >= self.steps and node.state.row == self.final_state.row and node.state.column == self.final_state.column):
			if("0" not in node.state.pokemonCaptured):
				return True
		return False
		