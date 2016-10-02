from Cell import *
from Maze import *

rows = 4
columns = 3
field = [[Cell() for j in range(columns)] for i in range(rows)]
for i in range(0,rows):
	for j in range(0,columns):
		field[i][j].row = i
		field[i][j].column = j



maze = Maze(field,rows,columns)