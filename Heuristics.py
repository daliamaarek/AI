from Node import *  
from Maze import * 
from State import *
import math

class Heuristics():

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


