class Cell:
	
	def __init__(self, isPokemon, row, column):
		self.walls = ["UP","DOWN","LEFT","RIGHT"]
		self.isPokemon = isPokemon
		self.row = row
		self.column = column
	def __init__(self):
		self.walls = ["UP","DOWN","LEFT","RIGHT"]
		self.isPokemon = False
