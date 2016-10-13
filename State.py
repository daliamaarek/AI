from StateAbstract import *

class State(StateAbstract):
	def __init__(self):
		self.row = 0
		self.column = 0
		self.direction = 0
		self.pokemonCaptured = ""
		self.steps = 0
	
	def __eq__(self, other):
		return (self.row == other.row and self.column == other.column and self.direction == other.direction and self.pokemonCaptured == other.pokemonCaptured)
