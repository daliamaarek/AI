from createMaze import * #File that contains maze initialization
from State import *
from Node import *
from Problem import *
from searchVariables import *
from SearchAlgorithms import *

 
print "Pokemons positions: "
print maze.map
print "Required Steps: " + str(maze.steps)
for i in range(0,rows):
	for j in range(0,columns):
		print field[i][j].walls
print "-------------------------------------"


node = generalSearch(maze, "BF", True)
if(node is not None):
	maze.visualize(node)
node = generalSearch(maze, "UC", True)
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H1", True)
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H2", True)
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H3", True)
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H4", True)
if(node is not None):
	maze.visualize(node)
