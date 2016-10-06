from Node import *  
from Maze import * 
from State import *

class Heuristics():

	def getPokemons(self, maze , start_row , start_column, end_row, end_column):
		pokemons = []
		for i in range(start_row, end_row):
			for j in range(start_column,end_column):
				if(maze.field[i][j].isPokemon == True):
					pokemons.append(str((i,j)))			
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