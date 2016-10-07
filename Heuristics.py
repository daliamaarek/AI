from Node import *  
from Maze import * 
from State import *

class Heuristics():

	def manhattanPokemon (self, maze, node):
		self.curr_row = node.state.row 
		self.curr_col = node.state.column
		self.pokemons = self.getPokemons(maze, 0, 0, maze.rows, maze.columns)
		
		self.nearest_row = self.pokemons[0][0]
		self.nearest_col = self.pokemons[0][1]

		self.diff_row = abs(self.curr_row - self.pokemons[0][0])
		self.diff_col = abs(self.curr_col - self.pokemons[0][1])
		self.nearest_pokemon = self.diff_row + self.diff_col

		for i in range(1, len(self.pokemons)-1):
			self.diff_row = abs(self.curr_row - self.pokemons[i][0])
			self.diff_col = abs(self.curr_col - self.pokemons[i][1])
			self.diff_pok = self.diff_row + self.diff_col
			if(self.diff_pok < self.nearest_pokemon ):
				self.nearest_row = self.pokemons[i][0]
				self.nearest_col = self.pokemons[i][1]
		
		return (self.nearest_row, self.nearest_col)


	def manhattanGoal (self,maze, node, state):
		self.curr_row = node.state.row 
		self.curr_col = node.state.column
		self.diff_col = state.column
		self.diff_row = state.row
		self.distance = abs(self.curr_col - self.diff_col) + abs(self.curr_row - self.diff_row)		
		return self.distance

	def getPokemons(self, maze , start_row , start_column, end_row, end_column):
		pokemons = []
		for i in range(start_row, end_row):
			for j in range(start_column,end_column):
				if(maze.field[i][j].isPokemon == True):
					pokemons.append((i,j))		
		return pokemons			

		def SumOfPokemonDistances(node, maze):
			row = node.state.row
			column = column.state.row
			start_row = 0 
			start_column = 0 
			end_column = 0
			end_row = 0
			if (node.state.direction == 0):
				end_column=maze.columns
				end_row = row
			elif(node.state.direction == 1):
				start_row = row
				end_column = maze.columns
				end_row = maze.rows
			elif(node.state.direction == 2):
				start_row = row
				end_column = maze.columns
				end_row = maze.rows
			elif(node.state.direction == 3):
				end_row = row
				end_column = column 
			pokemon = getPokemons(maze, start_row, start_column, end_row, end_column)
			distance = 0
			for i in range(1, len(pokemon)):
				distance += math.sqrt((pokemon[i-1].row^2 - pokemon[i].row^2) + 
					(pokemon[i-1].column^2 - pokemon[i].column^2))
			return distance