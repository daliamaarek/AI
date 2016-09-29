from random import randint

class Maze:
	
	def __init__(self, field, rows, columns):
		self.field = field
		self.rows = rows
		self.columns = columns
		# generates a 2D rows x columns matrix having 0 in each cell 
		self.visited_cells = [[0 for x in range(columns)] for y in range(rows)]

		# for i in range(0,rows):
		# 	for j in range(0,columns):
		# 		print self.visited_cells[i][j]


	def updateNew(self):
		if(curr_wall[2] == "DOWN"):
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("DOWN")
			self.field[new_row][new_column].walls.remove("UP")
		elif(curr_wall[2] == "UP"):
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("UP")
			self.field[new_row][new_column].walls.remove("DOWN")
		elif(curr_wall[3] == "LEFT"):
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("LEFT")
			self.field[new_row][new_column].walls.remove("RIGHT")
		else:
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("RIGHT")
			self.field[new_row][new_column].walls.remove("LEFT")

	def updateOld(self):
		if(curr_wall[2] == "DOWN"):
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("UP")
			self.field[new_row][new_column].walls.remove("DOWN")
		elif(curr_wall[2] == "UP"):
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("DOWN")
			self.field[new_row][new_column].walls.remove("UP")
		elif(curr_wall[3] == "LEFT"):
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("RIGHT")
			self.field[new_row][new_column].walls.remove("LEFT")
		else:
			self.field[curr_wall[0]][curr_wall[1]].walls.remove("LEFT")
			self.field[new_row][new_column].walls.remove("RIGHT")

	# Randomized Prim's algorithm
	def genMaze(self):
		start_row = randint(0,self.rows)
		start_column = randint(0,self.columns)
		all_walls = []
		curr_walls = self.field[start_row][start_column].walls
		for i in range(0,len(cur_walls)):
			curr_walls[i] = (start_row, start_column, curr_walls[i])
		self.visited_cells[start_row][start_column] = 1
		all_walls = all_walls + curr_walls

		while (len(all_walls) != 0):
			x = randint(0,len(all_walls) - 1)
			curr_wall = all_walls[x]

			# checks for border walls
			if((curr_wall[0] == 0 and curr_wall[2] == "UP") or (curr_wall[1] == 0 and curr_wall[2] == "LEFT")
				or (curr_wall[0] == self.rows - 1 and curr_wall[2] == "DOWN") or (curr_wall[1] == self.columns - 1 and curr_wall[2] == "RIGHT")):
				continue
			new_row = curr_wall[0]
			new_column = curr_wall[1]

			if(curr_wall[2] == "DOWN"):
				new_row -= 1
			elif(curr_wall[2] == "UP"):
				new_row += 1 
			elif(curr_wall[3] == "LEFT"):
				new_column -= 1
			else:
				new_column += 1

			all_walls.remove(curr_wall)

			if(self.visited[curr_wall[0]][curr_wall[1]] == 1 and self.visited[new_row][new_column] == 0):
				updateNew()
				self.visited[new_row][new_column] = 1

				curr_walls = self.field[new_row][new_column].walls
				start_row = self.field[new_row][new_column].row
				start_row = self.field[new_row][new_column].column
				for i in range(0,len(curr_walls)):
					curr_walls[i] = (start_row, start_column, curr_walls[i])
				all_walls = all_walls + curr_walls

			if(self.visited[curr_wall[0]][curr_wall[1]] == 0 and self.visited[new_row][new_column] == 1):
				updateOld()
				self.visited[curr_wall[0]][curr_wall[1]] = 1
				curr_walls = self.field[curr_wall[0]][curr_wall[1]].walls
				start_row = self.field[curr_wall[0]][curr_wall[1]].row
				start_column = self.field[curr_wall[0]][curr_wall[1]].column
				for i in range(0,len(curr_walls)):
					curr_walls[i] = (start_row, start_column, curr_walls[i])
				all_walls = all_walls + curr_walls

			


			#print curr_wall








