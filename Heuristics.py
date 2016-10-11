from Node import *  
from Maze import * 
from State import *
import math

class Heuristics():
	def __init__ (self, maze, state):
		self.maze = maze
		self.state = state

	def getPokemonsWithinRange(maze , start_row , start_column, end_row, end_column):
		pokemons = []
		for i in range(start_row, end_row):
			for j in range(start_column,end_column):
				if(maze.field[i][j].isPokemon == True):
					pokemons.append((i,j))	
		return pokemons				

	def getOnePokemonInRange (pokemons,curr_row,curr_col,node):
		
		for i in range(0, len(pokemons)):
				if ((node.state.direction == 0 and pokemons[i][0] < self.curr_row) or ((node.state.direction == 1 and pokemons[i][0] > curr_col)) or ((node.state.direction == 2 and pokemons[i][0] > curr_row)) or ((node.state.direction == 3 and pokemons[i][1] < curr_col))):  
					self.diff_row = abs(curr_row - pokemons[i][0])
					self.diff_col = abs(curr_col - pokemons[i][1])
					self.nearest_pokemon = self.diff_row + self.diff_col
					return (pokemons[i][0], pokemons[i][1], self.nearest_pokemon,i)

		return (-1,-1,-1,len(pokemons)-1)
	
	def getOrientation(node, maze):
		row = node.state.row
		column = node.state.column
		start_row = 0 
		start_column = 0 
		end_column = 0
		end_row = 0
		if (node.state.direction == 0):
			end_column = maze.columns
			end_row = row 
		elif(node.state.direction == 1):
			start_column = column + 1
			end_column = maze.columns
			end_row = maze.rows
		elif(node.state.direction == 2):
			start_row = row + 1
			end_column = maze.columns
			end_row = maze.rows
		elif(node.state.direction == 3):
			end_row = maze.rows
			end_column = column
		return (start_row, start_column, end_row, end_column)

	#gets distance between agent and pokemon using manhattan distance
	def H1 (self, node):
		curr_row = node.state.row 
		curr_col = node.state.column
		pokemons = getPokemonsWithinRange(self.maze, 0, 0, self.maze.rows, self.maze.columns)
		r = self.getOnePokemonInRange (pokemons, curr_row, curr_col,node)
		nearest_row = r[0]
		nearest_col = r[1]
		nearest_pokemon =  abs(self.curr_row - self.nearest_row) + abs(self.curr_col -self.nearest_col)

		
		for i in range(r[3]+1, len(pokemons)-1):
			if (((node.state.direction == 0) and (self.pokemons[i][0] < curr_row)) or ((node.state.direction == 1) and (pokemons[i][1] > curr_col)) or ((node.state.direction == 2) and (.pokemons[i][0] > curr_row)) or ((node.state.direction == 3) and (pokemons[i][1] < self.curr_col))):
				print self.pokemons[i][0]
				diff_row = abs(curr_row - pokemons[i][0])
				diff_col = abs(curr_col - pokemons[i][1])
				diff_pok = diff_row + diff_col
				if(diff_pok < nearest_pokemon ):
					self.nearest_row = self.pokemons[i][0]
					self.nearest_col = self.pokemons[i][1]
					self.nearest_pokemon = self.diff_pok
			
		return (self.nearest_row, self.nearest_col)


	#gets distance between agent and goal using manhattan distance
	def H2 (self, node):
		curr_row = node.state.row 
		curr_col = node.state.column

		diff_col = self.state.column
		diff_row = self.state.row
		distance = abs(curr_col - diff_col) + abs(curr_row - diff_row)		
		return distance


	#gets smallest sum of distances between pokemon in the direction of the node
	def H3(self, node):
		orientation = self.getOrientation(node, self.maze)
		pokemon = self.getPokemonsWithinRange(self.maze, orientation[0], orientation[1], 
			orientation[2], orientation[3])
		distance = 0	
		print "pokemon:"	
		print pokemon
		if(pokemon):
			currentPokemon = pokemon[0]
			pokemon.pop(0)
		while(len(pokemon)>0):
			minDistance = math.sqrt((pokemon[0][0] - currentPokemon[0])**2 + 
					(pokemon[0][1] - currentPokemon[1])**2)
			index = 0
			for i in range(1, len(pokemon)):
				d = math.sqrt((pokemon[i][0] - currentPokemon[0])**2 + 
					(pokemon[i][1] - currentPokemon[1])**2)
				if(minDistance > d):
				 	minDistance = d
				 	index = i
			distance = distance + minDistance
			currentpokemon = pokemon.pop(index)
		return distance

	
	#gets number of Pokemon in the direction of the node
	def H4(self, node):
		orientation = self.getOrientation(node, self.maze)
		pokemon = self.getPokemonsWithinRange(self.maze, orientation[0], orientation[1], 
			orientation[2], orientation[3])
		print "pokemon:"	
		print pokemon
		return len(pokemon)

	def F1(self, node):
		return H1(node) + node.cost

	def F2(self, node):
		return H2(node) + node.cost

	def F3(self, node):
		return H3(node) + node.cost

	def F1(self, node):
		return H4(node) + node.cost



