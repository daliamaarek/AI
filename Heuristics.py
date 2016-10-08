from Node import *  
from Maze import * 
from State import *
import math

class Heuristics():
	
	def getPokemonsWithinRange(self, maze , start_row , start_column, end_row, end_column):
		pokemons = []
		for i in range(start_row, end_row):
			for j in range(start_column,end_column):
				if(maze.field[i][j].isPokemon == True):
					pokemons.append((i,j))	
		return pokemons				

	def getOnePokemonInRange (self, pokemons,curr_row,curr_col,node):
		
		for i in range(0, len(pokemons)):
				if ((node.state.direction == 0 and pokemons[i][0] < self.curr_row) or ((node.state.direction == 1 and pokemons[i][0] > curr_col)) or ((node.state.direction == 2 and pokemons[i][0] > curr_row)) or ((node.state.direction == 3 and pokemons[i][1] < curr_col))):  
					print "north"
					self.diff_row = abs(curr_row - pokemons[i][0])
					self.diff_col = abs(curr_col - pokemons[i][1])
					self.nearest_pokemon = self.diff_row + self.diff_col
					print "first shortest node is : " + str((pokemons[i][0], pokemons[i][1]))
					return [pokemons[i][0], pokemons[i][1], self.nearest_pokemon,i]

		return [-1,-1,-1,len(pokemons)-1]	
	
	def getOrientation(self, node, maze):
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
		return [start_row, start_column, end_row, end_column]

	#gets distance between agent and pokemon using manhattan distance
	def H1 (self, maze, node):
		self.curr_row = node.state.row 
		self.curr_col = node.state.column
		self.pokemons = self.getPokemonsWithinRange(maze, 0, 0, maze.rows, maze.columns)
		self.r = self.getOnePokemonInRange (self.pokemons,self.curr_row,self.curr_col,node)
		self.nearest_row = self.r[0]
		self.nearest_col = self.r[1]
		self.nearest_pokemon =  abs(self.curr_row - self.nearest_row) + abs(self.curr_col -self.nearest_col)

		
		for i in range(self.r[3]+1, len(self.pokemons)-1):
			if (((node.state.direction == 0) and (self.pokemons[i][0] < self.curr_row)) or ((node.state.direction == 1) and (self.pokemons[i][1] > self.curr_col)) or ((node.state.direction == 2) and (self.pokemons[i][0] > self.curr_row)) or ((node.state.direction == 3) and (self.pokemons[i][1] < self.curr_col))):
				print self.pokemons[i][0]
				self.diff_row = abs(self.curr_row - self.pokemons[i][0])
				self.diff_col = abs(self.curr_col - self.pokemons[i][1])
				self.diff_pok = self.diff_row + self.diff_col
				if(self.diff_pok < self.nearest_pokemon ):
					self.nearest_row = self.pokemons[i][0]
					self.nearest_col = self.pokemons[i][1]
			
		return (self.nearest_row, self.nearest_col)


		#gets distance between agent and goal using manhattan distance
	def H2 (self,maze, node, state):
		self.curr_row = node.state.row 
		self.curr_col = node.state.column
		self.diff_col = state.column
		self.diff_row = state.row
		self.distance = abs(self.curr_col - self.diff_col) + abs(self.curr_row - self.diff_row)		
		return self.distance


	#gets smallest sum of distances between pokemon in the direction of the node
	def H3(self, node, maze):
		orientation = self.getOrientation(node, maze)
		pokemon = self.getPokemonsWithinRange(maze, orientation[0], orientation[1], 
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
	def H4(self, node, maze):
		orientation = self.getOrientation(node, maze)
		pokemon = self.getPokemonsWithinRange(maze, orientation[0], orientation[1], 
			orientation[2], orientation[3])
		print "pokemon:"	
		print pokemon
		return len(pokemon)



