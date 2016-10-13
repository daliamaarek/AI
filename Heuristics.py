from Node import *  
from Maze import * 
from State import *
from createMaze import *
import math
import sys

class Heuristics():

	def __init__ (self, maze, state):
		self.maze = maze
		self.state = state #final state 

	
	#gets distance between agent and pokemon using manhattan distance
	def H1 (self, node):
		curr_row = node.state.row 
		curr_col = node.state.column
		pokemons = getPokemonsWithinRange(node, self.maze, 0, 0, self.maze.rows, self.maze.columns)
		r = getOnePokemonInRange (pokemons, curr_row, curr_col,node)
		nearest_row = r[0]
		nearest_col = r[1]
		nearest_pokemon =  abs(curr_row - nearest_row) + abs(curr_col -nearest_col)
		for i in range(r[3]+1, len(pokemons)-1):
			if (((node.state.direction == 0) and (pokemons[i][0] < curr_row)) or ((node.state.direction == 1) and (pokemons[i][1] > curr_col)) or ((node.state.direction == 2) and (pokemons[i][0] > curr_row)) or ((node.state.direction == 3) and (pokemons[i][1] < curr_col))):
				# print pokemons[i][0]
				diff_row = abs(curr_row - pokemons[i][0])
				diff_col = abs(curr_col - pokemons[i][1])
				diff_pok = diff_row + diff_col
				if(diff_pok < nearest_pokemon ):
					nearest_row = pokemons[i][0]
					nearest_col = pokemons[i][1]
					nearest_pokemon = diff_pok
		if (nearest_row == -1):
			return 0 
		return nearest_pokemon


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
		orientation = getOrientation(node, self.maze)
		pokemon = getPokemonsWithinRange(node, self.maze, orientation[0], orientation[1], 
			orientation[2], orientation[3])
		distance = 0	
		if(pokemon):
			currentPokemon = pokemon.pop(0)
			while(pokemon):
				minDistance = sys.maxint
				for i in range(0, len(pokemon)):
					d = math.sqrt((pokemon[i][0] - currentPokemon[0])**2 + 
						(pokemon[i][1] - currentPokemon[1])**2)
					if(minDistance > d):
					 	minDistance = d
					 	index = i
				distance = distance + minDistance
				currentPokemon = pokemon.pop(index)
		return distance

	
	#gets number of Pokemon in the direction of the node
	def H4(self, node):
		orientation = getOrientation(node, self.maze)
		pokemon = getPokemonsWithinRange(node, self.maze, orientation[0], orientation[1], 
			orientation[2], orientation[3])
		return len(pokemon)



	def F1(self, node):
		return self.H1(node) + node.cost

	def F2(self, node):
		return self.H2(node) + node.cost

	def F3(self, node):
		return self.H3(node) + node.cost

	def F4(self, node):
		return self.H4(node) + node.cost

def getPokemonsWithinRange(node, maze , start_row , start_column, end_row, end_column):
		pokemons = []
		for i in range(start_row, end_row):
			for j in range(start_column,end_column):
				if(maze.field[i][j].isPokemon == True and node.state.pokemonCaptured[maze.map[(i,j)]] == '0'):
					pokemons.append((i,j))
		return pokemons				

def getOnePokemonInRange (pokemons,curr_row,curr_col,node):
	
	for i in range(0, len(pokemons)):
			if ((node.state.direction == 0 and pokemons[i][0] < curr_row) or ((node.state.direction == 1 and pokemons[i][0] > curr_col)) or ((node.state.direction == 2 and pokemons[i][0] > curr_row)) or ((node.state.direction == 3 and pokemons[i][1] < curr_col))):  
				diff_row = abs(curr_row - pokemons[i][0])
				diff_col = abs(curr_col - pokemons[i][1])
				nearest_pokemon = diff_row + diff_col
				return (pokemons[i][0], pokemons[i][1], nearest_pokemon,i)
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

#--------------------------------------------------------------
# maze.genMaze()
# fState = State()
# fState.row = 4
# fState.column = 4

# h = Heuristics(maze, fState)
# state = State()
# state.row = 5
# state.column = 5	
# state.direction = 0

# n = Node()
# n.state = state 
# print"---H1---"
# print h.H1(n)
# print"---H2---"
# print h.H2(n)
# print "---H3---"
# print h.H3(n)
# print "---H4---"
# print h.H4(n)

