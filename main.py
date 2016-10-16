from createMaze import *
from State import *
from Node import *
from SearchAlgorithms import *
from Problem import *


maze.genMaze()

print "Pokemons positions: "
print maze.map

print "Required Steps: " + str(maze.steps)
for i in range(0,rows):
	for j in range(0,columns):
		print field[i][j].walls
print "-------------------------------------"
print "NODES VISITED:"


#GR and AS is missing
state = State()
state.row = 1
state.column = 1
state.direction = 3
pokemons_size = len(maze.map)
state.pokemonCaptured = ""
for i in range (0,pokemons_size):
	state.pokemonCaptured = "0" + state.pokemonCaptured

final_state = State()

final_state.row = 0
final_state.column = 0
final_state.pokemonCaptured = ""
for i in range(0,len(state.pokemonCaptured)):
	final_state.pokemonCaptured = '1' + final_state.pokemonCaptured

problem = Problem(["RL","RR","F"], state, final_state, 1, maze.steps)
# node = generalSearch(maze, "ID", False) 

print "-------------------------------------------"
print "VISUALIZEEEEE:"
res = ''
node = generalSearch(problem, "BF", True)
if(node is not None):
	maze.visualize(node)
node = generalSearch(problem, "UC", True)
if(node is not None):
	maze.visualize(node)

node = Astar(problem, "H1", True)
if(node is not None):
	maze.visualize(node)

node = Astar(problem, "H2", True)
if(node is not None):
	maze.visualize(node)

node = Astar(problem, "H3", True)
if(node is not None):
	maze.visualize(node)

node = Astar(problem, "H4", True)
if(node is not None):
	maze.visualize(node)
