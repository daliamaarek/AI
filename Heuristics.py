from Node import *  
from Maze import * 
from State import *
import math

class Heuristics():

	def manhattanPokemon (self, maze, node):
		self.curr_row = node.state.row 
		self.curr_col = node.state.column
		self.pokemons = self.getPokemons(maze, 0, 0, maze.rows, maze.columns)
		self.r = self.getStartingValue (self.pokemons,self.curr_row,self.curr_col,node)
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

	def getStartingValue (self, pokemons,curr_row,curr_col,node):
		
		for i in range(0, len(pokemons)):
				if ((node.state.direction == 0 and pokemons[i][0] < self.curr_row) or ((node.state.direction == 1 and pokemons[i][0] > curr_col)) or ((node.state.direction == 2 and pokemons[i][0] > curr_row)) or ((node.state.direction == 3 and pokemons[i][1] < curr_col))):  
					print "north"
					self.diff_row = abs(curr_row - pokemons[i][0])
					self.diff_col = abs(curr_col - pokemons[i][1])
					self.nearest_pokemon = self.diff_row + self.diff_col
					print "first shortest node is : " + str((pokemons[i][0], pokemons[i][1]))
					return [pokemons[i][0], pokemons[i][1], self.nearest_pokemon,i]

		return [-1,-1,-1,len(pokemons)-1]





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
	
	def getOrientation(self, node, maze):
		row = node.state.row
		column = node.state.column
		self.start_row = 0 
		self.start_column = 0 
		self.end_column = 0
		self.end_row = 0
		if (node.state.direction == 0):
			self.end_column = maze.columns
			self.end_row = row 
		elif(node.state.direction == 1):
			self.start_column = column + 1
			self.end_column = maze.columns
			self.end_row = maze.rows
		elif(node.state.direction == 2):
			self.start_row = row + 1
			self.end_column = maze.columns
			self.end_row = maze.rows
		elif(node.state.direction == 3):
			self.end_row = maze.rows
			self.end_column = column

	def SumOfPokemonDistances(self, node, maze):
		self.getOrientation(node, maze)
		pokemon = self.getPokemons(maze, self.start_row, self.start_column, 
			self.end_row, self.end_column)
		distance = 0	
		print "pokemon:"	
		print pokemon
		if(len(pokemon)>0):
			for i in range(1, len(pokemon)):
				distance = distance + math.sqrt((pokemon[i-1][0] - pokemon[i][0])**2 + 
					(pokemon[i-1][1] - pokemon[i][1])**2)
		return distance

	def getPokemonNumber(self, node, maze):
		self.getOrientation(node, maze)
		pokemon = self.getPokemons(maze, self.start_row, self.start_column, 
			self.end_row, self.end_column)
		print "pokemon:"	
		print pokemon
		return len(pokemon)



