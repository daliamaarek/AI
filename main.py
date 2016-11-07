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

Visualize = False
node = generalSearch(maze, "BF", Visualize)
if(node is not None and Visualize):
	maze.visualize(node)

# node = generalSearch(maze, "UC", Visualize)
# print " TTT UC insha'allah "
# if(node is not None and Visualize):
# 	maze.visualize(node)

# node = Astar(maze, "H1", Visualize)
# if(node is not None and Visualize):
# 	maze.visualize(node)

# node = Astar(maze, "H2", Visualize)
# if(node is not None and Visualize):
# 	maze.visualize(node)

# node = Astar(maze, "H3", Visualize)

# if(node is not None and  Visualize):
# 	maze.visualize(node)

node = Astar(maze, "H4", Visualize)
if(node is not None and  Visualize):
	maze.visualize(node)

dd = ['UP', 'RIGHT', 'DOWN', 'LEFT']
maze.visualize(node)
writeFacts(maze, dd)
