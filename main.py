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
print " TTT BF elhamdullaah "
if(node is not None):
	maze.visualize(node)
node = generalSearch(maze, "UC", True)
print " TTT UC insha'allah "
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H1", True)
print " TTT H1 yarab "
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H2", True)
print " TTT H2 yarab "
if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H3", True)
print " TTT H3 yarab "

if(node is not None):
	maze.visualize(node)

node = Astar(maze, "H4", True)
print " 	TTT H4 yarab "
if(node is not None):
	maze.visualize(node)
