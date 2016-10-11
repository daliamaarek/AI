from Cell import *
from Maze import *

rows = 2
columns = 2
field = [[Cell() for j in range(columns)] for i in range(rows)]

for i in range(0,rows):
	for j in range(0,columns):
		field[i][j].row = i
		field[i][j].column = j

maze = Maze(field, rows, columns)