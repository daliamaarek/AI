

class State():

	self.row = 0
	self.column = 0
	self.direction = 0
	self.pokemonCaptured = ""

	def setRow(self, row):
		self.row = row

	def setColumn(self, column):
		self.column = column 

	def setDirection(self, direction):
		self.direction = direction
		
	def setPokemonCaptured(self, pokemonCaptured):
		self.pokemonCaptured = pokemonCaptured