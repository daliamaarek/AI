from random import randint, random, sample
from State import *

class Maze:
	
	def __init__(self, field, rows, columns):
		self.field = field
		self.rows = rows
		self.columns = columns
		self.map = dict()
		self.reverse_map = dict()
		self.count_pokemons = 0
		self.steps = 0
		# generates a 2D rows x columns matrix having 0 in each cell 
		self.visited = [[0 for x in range(columns)] for y in range(rows)]


	def update(self, start, end):
		# print self.field[start[0]][start[1]].walls
		if(start[2] == "DOWN"):
			if("DOWN" in self.field[start[0]][start[1]].walls):
				self.field[start[0]][start[1]].walls.remove("DOWN")
			if("UP" in self.field[end[0]][end[1]].walls):
				self.field[end[0]][end[1]].walls.remove("UP")
		elif(start[2] == "UP"):
			if("UP" in self.field[start[0]][start[1]].walls):
				self.field[start[0]][start[1]].walls.remove("UP")
			if("DOWN" in self.field[end[0]][end[1]].walls):
				self.field[end[0]][end[1]].walls.remove("DOWN")
		elif(start[2] == "LEFT"):
			if("LEFT" in self.field[start[0]][start[1]].walls):
				self.field[start[0]][start[1]].walls.remove("LEFT")
			if("RIGHT" in self.field[end[0]][end[1]].walls):
				self.field[end[0]][end[1]].walls.remove("RIGHT")
		else:
			if("RIGHT" in self.field[start[0]][start[1]].walls):
				self.field[start[0]][start[1]].walls.remove("RIGHT")
			if("LEFT" in self.field[end[0]][end[1]].walls):
				self.field[end[0]][end[1]].walls.remove("LEFT")

	def updateRowColumn(self,curr_wall, new_row, new_column):
		if(curr_wall[2] == "DOWN"):
			new_row += 1
		elif(curr_wall[2] == "UP"):
			new_row -= 1 
		elif(curr_wall[2] == "LEFT"):
			new_column -= 1
		else:
			new_column += 1
		return (new_row,new_column)
	
	def genMaze(self):
		self.primsAlgorithm()
		rows = self.rows
		columns = self.columns
		min_steps = int(rows*columns*(1.0/3))
		self.steps = 1 #randint(min_steps, rows*columns*2)
		self.no_of_pokemons = randint(1,int(rows*columns*(1.0/2)))
		self.pokemons = sample(range(0, rows*columns - 1), self.no_of_pokemons)
		# print self.steps
		# print self.pokemons
		for i in range(0,len(self.pokemons)):
			curr_pos = self.pokemons[i]
			row = curr_pos/columns
			column = curr_pos - row*columns
			self.map[(row,column)] = self.count_pokemons
			self.reverse_map[self.count_pokemons] = (row,column)
			self.count_pokemons = self.count_pokemons + 1
			# print str(row) + " " + str(column)
			self.field[row][column].isPokemon = True


	# Randomized Prim's algorithm
	def primsAlgorithm(self):
		start_row = randint(0,self.rows - 1)
		start_column = randint(0,self.columns - 1)
		all_walls = []

		curr_walls = self.field[start_row][start_column].walls[:]
		for i in range(0,len(curr_walls)):
			curr_walls[i] = (start_row, start_column, curr_walls[i])
		self.visited[start_row][start_column] = 1
		all_walls = all_walls + curr_walls

		while (len(all_walls) != 0):
			x = randint(0,len(all_walls) - 1)
			curr_wall = all_walls[x]
			# print len(all_walls)
			all_walls.remove(curr_wall)
			# checks for border walls
			if((curr_wall[0] == 0 and curr_wall[2] == "UP") or (curr_wall[1] == 0 and curr_wall[2] == "LEFT")
				or (curr_wall[0] == self.rows - 1 and curr_wall[2] == "DOWN") or (curr_wall[1] == self.columns - 1 and curr_wall[2] == "RIGHT")):
				continue
			
			new_row = curr_wall[0]
			new_column = curr_wall[1]
			(new_row,new_column) = self.updateRowColumn(curr_wall,new_row,new_column)
			# print str(curr_wall[0]) + " " + str(curr_wall[1])
			# print str(new_row) + " " + str(new_column)
			if(self.visited[curr_wall[0]][curr_wall[1]] == 1 and self.visited[new_row][new_column] == 0):
				self.update(curr_wall,(new_row,new_column))
				self.visited[new_row][new_column] = 1
				curr_walls = self.field[new_row][new_column].walls[:]
				start_row = self.field[new_row][new_column].row
				start_column = self.field[new_row][new_column].column
				for i in range(0,len(curr_walls)):
					curr_walls[i] = (start_row, start_column, curr_walls[i])
				all_walls = all_walls + curr_walls

			if(self.visited[curr_wall[0]][curr_wall[1]] == 0 and self.visited[new_row][new_column] == 1):
				self.update(curr_wall,(new_row,new_column))
				self.visited[curr_wall[0]][curr_wall[1]] = 1
				curr_walls = self.field[curr_wall[0]][curr_wall[1]].walls[:]
				start_row = self.field[curr_wall[0]][curr_wall[1]].row
				start_column = self.field[curr_wall[0]][curr_wall[1]].column
				for i in range(0,len(curr_walls)):
					curr_walls[i] = (start_row, start_column, curr_walls[i])
				all_walls = all_walls + curr_walls


	def visualize(self, node):
		if(node.parent is not None):
			capturedparent = node.parent.state.pokemonCaptured
		captured = node.state.pokemonCaptured

		if(self.field[node.state.row][node.state.column].isPokemon == True and ((node.parent is not None and capturedparent[self.map[(node.state.row, node.state.column)]] == '0') or (node.depth == 0 and captured[self.map[(node.state.row,node.state.column)]] == '1'))):
			print "Pokemon Captuuuuuuuured :')))!! *Tas2eef*"

		print "Required steps: " + str(self.steps)
		print "Walked steps " + str(node.state.steps)
		print "Current position = (" + str(node.state.row) + " " + str(node.state.column) + ")"
		print "Walls at curr position: " + str(self.field[node.state.row][node.state.column].walls)
		print "Direction: " + str(directions[node.state.direction])
		print "Remaining Pokemons:"
		for i in range (0,len(node.state.pokemonCaptured)):
			if(node.state.pokemonCaptured[i] == '0'):
				print str(self.field[self.reverse_map[i][0]][self.reverse_map[i][1]].row) + " " + str(self.field[self.reverse_map[i][0]][self.reverse_map[i][1]].column)
		print "----------------------------------"
		if(node.parent != None):
			self.visualize(node.parent)

			

directions = ["North", "East", "South", "West"]

		# print  str(field[i][j].isPokemon)
		# print field[i][j].row
		# print field[i][j].column